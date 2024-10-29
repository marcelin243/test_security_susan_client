from user_app.modules.admin_user.serialisers import *
from user_app.models import admin_user
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.hashers import check_password,make_password
from semence_app.modules.proprietaires.serialisers import insert_proprietairesSerializers
import jwt
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serialisers import CustomTokenObtainPairSerializer

user=get_user_model()
 
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# ===========================================
# CLASS DE PAGINATION
# ===========================================
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
class admin_userAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = admin_user.objects.all().order_by('-id')
    serializer_class= joint_admin_userSerializers
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        serialiser=insert_proprietairesSerializers(data=data)
        serialiser.is_valid(raise_exception=True)
        serialiser.save()
        
        data["password"] = make_password(request.data["password"])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
   

    def perform_create(self, serializer):
        serializer.save()


secret_key="lkjhgfdertyuioufghjkfgoiuytrghjjkPOOJJH"
@api_view(['POST'])
def create_admin(request):
    request.data["password"]=make_password(request.data["password"])
    serializer=insert_admin_userSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_admin(request):
     
    def set_cookie_in_response(response,key,value,max_age=None,expires=None,path="/",domain=None,secure=False,httponly=False,samesite=None):
        if not isinstance(response,Response):
            raise ValueError("la reponse doit etre une instance de la classe Response")
        response.set_cookie(key,value,max_age=max_age,expires=expires,path=path,domain=domain,secure=secure,httponly=httponly,samesite=samesite)
        return response
    
    try:
        user=admin_user.objects.get(email=request.data['email'])
        if not check_password(request.data['password'],user.password):
            return Response({"detail":"mot de passe incorrect "},status=status.HTTP_404_NOT_FOUND)
        serialiser=joint_admin_userSerializers(instance=user)
        payload= serialiser.data
        token=jwt.encode(payload,secret_key,algorithm='HS256')
        serialiser_=joint_admin_userSerializers(user)
        response=Response({"token":token,"admin_user":serialiser_.data},status=status.HTTP_200_OK)
        response=set_cookie_in_response(response,"jwt",token,max_age=3600,secure=True,httponly=True)
        return response
    
    except admin_user.DoesNotExist:
        return Response({"detail":"l'utilisateur n'existe pas "},status=status.HTTP_404_NOT_FOUND)
    
# LOGOUT OU DECONNECTION DES UTILISATEURS
# ===========================================================================================
@api_view(['GET'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = { "message": "Cookie supprimé." }
    return response    
    
@api_view(['PUT'])
def change_password_admin(request):
    try:
        user = admin_user.objects.get(id=request.data.get("user_id"))
    except admin_user.DoesNotExist:
        return Response({"errors": "Utilisateur introuvable"},status=status.HTTP_404_NOT_FOUND)
  
    if not check_password(request.data.get('ancien_pass_word'),user.password):
        return Response({"detail":" Ancien mot de passe incorrect "},status=status.HTTP_404_NOT_FOUND)
    new_hashed_password = make_password(request.data.get("new_pass_word"))
    data={"password":new_hashed_password}
    serializer = insert_admin_userSerializers(user, data=data ,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)