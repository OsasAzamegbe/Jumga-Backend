from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

from .utils import Rave, SECRET_KEY, ENCRYPTION_KEY


@api_view(['POST'])
@permission_classes((AllowAny, ))
@csrf_protect
def card_payments (request, *args, **kwargs):
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

        if "authorization" in data:
            payload["authorization"] = data["authorization"]

        rave = Rave(secret_key=SECRET_KEY, encryption_key=ENCRYPTION_KEY)
        charge_response = rave.charge_card(payload)

        if charge_response and charge_response["status"] == "success":
            return Response(data={
                "status": "successful",
                "message": "Payment initiated successfully",
                "data": charge_response
            }, status=status.HTTP_200_OK)
        
        
        return Response(data={
            "status": "error",
            "message": "There was a problem",
            "data": charge_response
        }, status=status.HTTP_400_BAD_REQUEST)

    except KeyError as e:
        return Response(data={
            "status": "error", 
            "message": f'Payload is missing the following field: {e}',
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes((AllowAny, ))
@csrf_protect
def validate_payments (request, *args, **kwargs):
    try:
        data = request.data
        flw_ref = data["flw_ref"]
        otp = data["otp"]

        rave = Rave(secret_key=SECRET_KEY, encryption_key=ENCRYPTION_KEY)
        validation_response = rave.validate_charge(flw_ref, otp)

        if validation_response and validation_response["status"] == "success":
            return Response(data={
                "status": "successful",
                "message": "Payment validated successfully",
                "data": validation_response
            }, status=status.HTTP_200_OK)
        
        
        return Response(data={
            "status": "error",
            "message": "There was a problem",
            "data": validation_response
        }, status=status.HTTP_400_BAD_REQUEST)

    except KeyError as e:
        return Response(data={
            "status": "error", 
            "message": f'Payload is missing the following field: {e}',
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes((AllowAny, ))
@csrf_protect
def verify_payment(request, *args, **kwargs):
    try:
        query_params = request.GET
        rave = Rave(SECRET_KEY, ENCRYPTION_KEY)
        verification_response = rave.verify_transaction(str(query_params["id"]))

        assert verification_response["data"]["status"] == "successful"
        assert verification_response["data"]["currency"] == query_params["currency"]
        assert verification_response["data"]["tx_ref"] == query_params["txref"]
        assert int(verification_response["data"]["charged_amount"]) >= int(query_params["amount"])
        return Response(data={
            "status": "successful",
            "message": "Payment verified",
            "data": verification_response
        }, status=status.HTTP_200_OK)

    except AssertionError:
        return Response(data={
            "status": "error",
            "message": "Payment not verified",
            "data": verification_response
        }, status=status.HTTP_409_CONFLICT)

    except KeyError:
        return Response(data={
            "status": "error",
            "message": "Check your query parameters. Bad request.",
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes((AllowAny, ))
@csrf_protect
def ng_bank_payment (request, *args, **kwargs):
    try:
        data = request.data
        payload = {
            "account_number": data["account_number"],
            "currency": data["currency"],
            "amount": data["amount"],
            "tx_ref": data["tx_ref"],
            "fullname": data["fullname"],
            "email": data["email"],
            "account_bank": data["account_bank"]
        }

        # BVN required for UBA aacounts
        if data["account_bank"] == "033":
            payload["bvn"] = data["bvn"]

        rave = Rave(secret_key=SECRET_KEY, encryption_key=ENCRYPTION_KEY)
        charge_response = rave.charge_bank_ng(payload)

        if charge_response and charge_response["status"] == "success":
            return Response(data={
                "status": "successful",
                "message": "Payment initiated successfully",
                "data": charge_response
            }, status=status.HTTP_200_OK)
        
        
        return Response(data={
            "status": "error",
            "message": "There was a problem",
            "data": charge_response
        }, status=status.HTTP_400_BAD_REQUEST)

    except KeyError as e:
        return Response(data={
            "status": "error", 
            "message": f'Payload is missing the following field: {e}',
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes((AllowAny, ))
@csrf_protect
def mpesa_payment (request, *args, **kwargs):
    try:
        data = request.data
        payload = {
            "currency": data["currency"],
            "amount": data["amount"],
            "tx_ref": data["tx_ref"],
            "fullname": data["fullname"],
            "email": data["email"],
            "phone_number": data["phone_number"]
        }

        rave = Rave(secret_key=SECRET_KEY, encryption_key=ENCRYPTION_KEY)
        charge_response = rave.charge_mpesa(payload)

        if charge_response and charge_response["status"] == "success":
            return Response(data={
                "status": "successful",
                "message": "Payment initiated successfully",
                "data": charge_response
            }, status=status.HTTP_200_OK)
        
        
        return Response(data={
            "status": "error",
            "message": "There was a problem",
            "data": charge_response
        }, status=status.HTTP_400_BAD_REQUEST)

    except KeyError as e:
        return Response(data={
            "status": "error", 
            "message": f'Payload is missing the following field: {e}',
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes((AllowAny, ))
@csrf_protect
def ghana_payment (request, *args, **kwargs):
    try:
        data = request.data
        payload = {
            "currency": data["currency"],
            "amount": data["amount"],
            "tx_ref": data["tx_ref"],
            "fullname": data["fullname"],
            "email": data["email"],
            "phone_number": data["phone_number"],
            "network": data["network"]
        }

        if payload["network"].lower() == "vodafone":
            payload["voucher"] = data["voucher"]

        rave = Rave(secret_key=SECRET_KEY, encryption_key=ENCRYPTION_KEY)
        charge_response = rave.charge_ghana_mobile(payload)

        if charge_response and charge_response["status"] == "success":
            return Response(data={
                "status": "successful",
                "message": "Payment initiated successfully",
                "data": charge_response
            }, status=status.HTTP_200_OK)
        
        
        return Response(data={
            "status": "error",
            "message": "There was a problem",
            "data": charge_response
        }, status=status.HTTP_400_BAD_REQUEST)

    except KeyError as e:
        return Response(data={
            "status": "error", 
            "message": f'Payload is missing the following field: {e}',
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes((AllowAny, ))
@csrf_protect
def payouts_transfer(request, *args, **kwargs):
    try:
        data = request.data
        payload = {}
        possible_destination = "['ng_bank', 'mpesa', 'gh_mobile', 'gh_bank', 'uk_bank']"

        try:
            query_params = request.GET
            destination = query_params["destination"].lower()
        except KeyError as e:
            return Response(data={
                "status": "error",
                "message": f"Query parameters is missing the field {e}. Possible values are: {possible_destination}.",
                "data": None
            }, status=status.HTTP_400_BAD_REQUEST)      

        if destination == "ng_bank":
            payload = {
                "debit_currency": data["debit_currency"],
                "currency": data["currency"],
                "amount": data["amount"],
                "reference": data["reference"],
                "account_bank": data["account_bank"],
                "account_number": data["account_number"],
                "narration": data["narration"],
                "callback_url": data["callback_url"]
            }
        elif destination == "mpesa":
            payload = {
                "currency": "KES",
                "amount": data["amount"],
                "reference": data["reference"],
                "account_bank": "MPS",
                "account_number": data["account_number"],
                "narration": data["narration"],
                "beneficiary_name": data["beneficiary_name"]
            }
        elif destination == "gh_mobile":
            payload = {
                "currency": "GHS",
                "amount": data["amount"],
                "reference": data["reference"],
                "account_bank": data["account_bank"],
                "account_number": data["account_number"],
                "narration": data["narration"],
                "beneficiary_name": data["beneficiary_name"]
            }
        elif destination == "gh_bank":
            payload = {
                "currency": "GHS",
                "amount": data["amount"],
                "reference": data["reference"],
                "callback_url": data["callback_url"],
                "destination_branch_code": data["destination_branch_code"],
                "account_bank": data["account_bank"],
                "account_number": data["account_number"],
                "narration": data["narration"],
                "beneficiary_name": data["beneficiary_name"]
            }
        elif destination == "uk_bank":
            payload = {
                "currency": data["currency"],
                "narration": data["narration"],
                "amount": data["amount"],
                "reference": data["reference"],
                "beneficiary_name": data["beneficiary_name"],
                "meta": [
                    {
                        "AccountNumber": data["AccountNumber"],
                        "RoutingNumber": data["RoutingNumber"],
                        "SwiftCode": data["SwiftCode"],
                        "BankName": data["BankName"],
                        "BeneficiaryName": data["beneficiary_name"],
                        "BeneficiaryCountry": data["BeneficiaryCountry"],
                        "PostalCode": data["PostalCode"],
                        "StreetNumber": data["StreetNumber"],
                        "StreetName": data["StreetName"],
                        "City": data["City"]
                    }
                ]
            }           
        else:
            return Response(data={
                "status": "error",
                "message": f"Invalid value for query parameter 'destination'. Possible values are: {possible_destination}.",
                "data": None
            }, status=status.HTTP_400_BAD_REQUEST)

        rave = Rave(secret_key=SECRET_KEY, encryption_key=ENCRYPTION_KEY)
        payout_response = rave.payouts_transfer(payload)

        if payout_response and payout_response["status"] == "success":
            return Response(data={
                "status": "successful",
                "message": "Payout initiated successfully",
                "data": payout_response
            }, status=status.HTTP_200_OK)
        
        
        return Response(data={
            "status": "error",
            "message": "There was a problem",
            "data": payout_response
        }, status=status.HTTP_400_BAD_REQUEST)

    except KeyError as e:
        return Response(data={
            "status": "error", 
            "message": f'Payload is missing the following field: {e}',
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes((AllowAny, ))
@ensure_csrf_cookie
def get_csrf(request):
    return Response(data={"message": "CSRF cookie set successfully."}, status=status.HTTP_200_OK)