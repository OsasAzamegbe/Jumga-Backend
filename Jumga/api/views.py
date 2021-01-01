from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect


#Test view for payments route
@api_view(['POST'])
@permission_classes((AllowAny, ))
@csrf_protect
def payments (request):
    try:
        data = request.data
        return Response(data={"recieved": data}, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((AllowAny, ))
@ensure_csrf_cookie
def get_csrf(request):
    return Response(data={"success": "CSRF cookie set successfully."})