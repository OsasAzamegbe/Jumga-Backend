from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

from .utils import validate_email, validate_password, CustomError
from api.models import Merchant, DispatchRider

import json



@api_view(['POST'])
@permission_classes((AllowAny, ))
@csrf_protect
def signup(request, *args, **kwargs):
    try:
        data = request.data
        query_params = request.GET

        if query_params:
            # validate query parameters
            try:
                possible_types = "['merchant', 'dispatch_rider']"
                account_type = query_params["type"].lower()
            except KeyError as e:
                return Response(data={
                    "status": "error", 
                    "message": f"Query parameters is missing the field {e}. Possible values are: {possible_types}.",
                    "data": None
                }, status=status.HTTP_400_BAD_REQUEST)

            # get user object from user_id
            user_id = data["user_id"]
            user = User.objects.get(pk=user_id)
            if not user:
                raise CustomError("No user with that user_id exists.")

            # ensure no dispatch or merchant account exists for user
            try:
                user.dispatchrider or user.merchant
                raise CustomError("User cannot create a merchant account.")
            except ObjectDoesNotExist:
                pass

            if account_type == "merchant":
                #signup merchant
                shop_name = data["shop_name"].lower()
                merchant = Merchant.objects.create(
                    user=user, shop_name=shop_name,
                    dispatch_rider=None
                )
                merchant.save()
                
            elif account_type == "dispatch_rider":
                #signup dispatch_rider
                dispatch_rider = DispatchRider.objects.create(user=user)
                dispatch_rider.save()
            else:
                return Response(data={
                    "status": "error", 
                    "message": f"Invalid value for query parameter 'type'. Possible values are: {possible_types}.",
                    "data": None
                }, status=status.HTTP_400_BAD_REQUEST)

            # get updated user object with merchant or dispatch rider object added to it
            user = User.objects.get(pk=user_id)
            
        else:
            #signup plain user
            username = data["username"]
            email = data["email"]
            first_name = data["first_name"]
            last_name = data["last_name"]
            password = data["password"]
            password_confirm = data["password_confirm"]

            # validation checks
            if not validate_password(password):
                return Response(data={
                    "status": "error", 
                    "message": "Password must be 8 - 100 characters long and must contain at least: one uppercase letter, one digit and one special character.",
                    "data": None                
                }, status=status.HTTP_400_BAD_REQUEST)
            elif password != password_confirm:
                return Response(data={
                    "status": "error", 
                    "message": "Passwords do not match.",
                    "data": None                
                }, status=status.HTTP_400_BAD_REQUEST)

            if not validate_email(email):
                return Response(data={
                    "status": "error", 
                    "message": "Email address is invalid.",
                    "data": None                
                }, status=status.HTTP_400_BAD_REQUEST)

            elif User.objects.filter(email=email).exists():
                return Response(data={
                    "status": "error", 
                    "message": "An Account with this email address already exists.",
                    "data": None                
                }, status=status.HTTP_400_BAD_REQUEST)

            elif User.objects.filter(username=username).exists():
                return Response(data={
                    "status": "error", 
                    "message": "An Account with this username already exists.",
                    "data": None                
                }, status=status.HTTP_400_BAD_REQUEST)

            # create user post validation
            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            user.set_password(password)
            user.save()
            # get saved user object from DB
            user = User.objects.get(username=username)

        # serialize new user object for json response 
        user_dict = json.loads(serializers.serialize("json", [user, ]))
        # del user_dict[0]["fields"]["password"]

        return Response(data={
            "status": "successful", 
            "message": "Account created successfully.",
            "data": user_dict
        }, status=status.HTTP_201_CREATED)


    except KeyError as e:
        return Response(data={
            "status": "error", 
            "message": f'Payload is missing the following field: {e}',
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)

    except CustomError as e:
        return Response(data={
            "status": "error", 
            "message": str(e),
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((AllowAny, ))
@csrf_protect
def login(request, *args, **kwargs):
    try:
        data = request.data
        username = data["username"]
        password = data["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return Response(data={
                "status": "successful", 
                "message": "User logged in successfully.",
                "data": None
            }, status=status.HTTP_200_OK)
        
        raise KeyError

    except KeyError:
        return Response(data={
            "status": "error", 
            "message": "Username or password Incorrect",
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_protect
def check_authenticated(request, *args, **kwargs):
    try:
        is_authenticated = User.is_authenticated

        if is_authenticated:
            return Response(data={
                "status": "successful", 
                "message": "User is authenticated",
                "data": {
                    "isAuthenticated": True
                }
            }, status=status.HTTP_200_OK)
        
        return Response(data={
            "status": "error", 
            "message": "User is not authenticated",
            "data": {
                    "isAuthenticated": False
                }
        }, status=status.HTTP_401_UNAUTHORIZED)

    except:
        return Response(data={
            "status": "error", 
            "message": "Internal Server Error",
            "data": None
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
@api_view(['POST'])
def logout(request, *args, **kwargs):
    try:
        auth.logout(request)
        return Response(data={
            "status": "successful", 
            "message": "User has been logged out",
            "data": None
        }, status=status.HTTP_200_OK)

    except:
        return Response(data={
            "status": "error", 
            "message": "User could not be logged out",
            "data": None
        }, status=status.HTTP_304_NOT_MODIFIED)


