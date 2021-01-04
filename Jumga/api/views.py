from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

from .utils import Rave, SECRET_KEY, ENCRYPTION_KEY


#Test view for payments route
@api_view(['POST'])
@permission_classes((AllowAny, ))
@csrf_protect
def card_payments (request):
    try:
        data = request.data
        payload = {
            "card_number": data["card_number"],
            "cvv": data["cvv"],
            "expiry_month": data["expiry_month"],
            "expiry_year": data["expiry_year"],
            "currency": data["currency"],
            "amount": data["amount"],
            "tx_ref": data["tx_ref"],
            "fullname": data["fullname"],
            "email": data["email"],
            "redirect_url": data["redirect_url"]
        }

        rave = Rave(secret_key=SECRET_KEY, encryption_key=ENCRYPTION_KEY)
        charge_response = rave.charge_card(payload)

        if charge_response and charge_response["status"] == "success":
            return Response(data={
                "status": "successful",
                "message": "Payment initiated successfully",
                "data": charge_response
            }, status=status.HTTP_202_ACCEPTED)
        
        
        return Response(data={
            "status": "error",
            "message": "There was a problem",
            "data": charge_response
        }, status=status.HTTP_400_BAD_REQUEST)

    except KeyError as e:
        return Response(data={
            "status": "failed", 
            "message": f'Payload is missing the following field: {e}',
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((AllowAny, ))
@ensure_csrf_cookie
def get_csrf(request):
    return Response(data={"success": "CSRF cookie set successfully."})