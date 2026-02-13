from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions 
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import authenticate, login, logout


class UserRegister(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = RegisterSerializer(data= request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)

class UserLogin(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            return Response({"message":"Login success"})
        else:
            return Response({"error":"Invalid Credentials"},status=status.HTTP_401_UNAUTHORIZED)

class Logout(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"})

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)