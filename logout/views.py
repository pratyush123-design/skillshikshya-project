from django.shortcuts import render

# Create your views here.
# logout/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from logout.serializers.serializers import LogoutSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()  # if using token auth
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
