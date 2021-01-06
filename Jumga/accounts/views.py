from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.contrib.auth.models import User
from django.core import serializers

from .utils import validate_email, validate_password

import json



@api_view(['POST'])
@permission_classes((AllowAny, ))
@csrf_protect
def signup(request):
    try:
        data = request.data
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

        # create user post validation
        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        user.save()

        user = User.objects.get(username=username)
        user_json = json.loads(serializers.serialize("json", [user, ]))

        return Response(data={
            "status": "successful", 
            "message": "Account created successfully.",
            "data": user_json
        }, status=status.HTTP_201_CREATED)


    except KeyError as e:
        return Response(data={
            "status": "error", 
            "message": f'Payload is missing the following field: {e}',
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)
