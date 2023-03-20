from django.shortcuts import render

import jwt, datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from Accounts.models import *
from Accounts.serializer import *

# Register view for the registering user
@api_view(['GET', 'POST'],)
@permission_classes((permissions.AllowAny,))
def register(request):
    if request.method == 'POST':
        serials = UserSerializer(data=request.data)

        if serials.is_valid():
            serials.save()
            return Response(serials.data, status=status.HTTP_201_CREATED)
        return Response(serials.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        pass

@api_view(['GET', 'POST'],)
@permission_classes((permissions.AllowAny,))
def login(request):
    if request.method == 'POST':
        # Getting email and password 
        email = request.data['email']
        password = request.data['password']

        # Authenticating user
        user = User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')

        payload = {
            'id' : user.id,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=2),
            'iat' : datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256') #.decode('utf-8')

        response = Response()

        # Setting user cookie for user login

        response.set_cookie(key='jwt', value=token, max_age=60*60*60*24)
        response.data = {'jwt':token}

        return response

    else:
        pass


@api_view(['GET', 'POST'],)
@permission_classes((permissions.AllowAny,))
def logout(request):
    if request.method == 'GET':
        response = Response()
        response.delete_cookie('jwt') # Deleting set cookie
        response.data = {
            'message': 'success'
        }
            
        return response

    else:
        pass
