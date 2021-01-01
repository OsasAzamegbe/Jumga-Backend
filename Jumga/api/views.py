from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


#Test view for payments route
def payments (request):
    try:
        data = request.POST
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(data={"recieved": data}, status=status.HTTP_200_OK)