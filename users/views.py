from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import RegisterValidateSerializer, AuthValidateSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import UserActive


@api_view(['POST'])
def registration_api_view(request):
    serializer = RegisterValidateSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            status = status.HTTP_400_BAD_REQUEST,
            data = serializer.errors
        )
    user = User.objects.create_user(
        username = serializer.validated_data.get('username'),
        password = serializer.validated_data.get('password'),
        is_active = False
        )

    code = "123456"
    UserActive.objects.create(user=user, code=code)

    return Response(status=status.HTTP_201_CREATED, data={'user_id': user.id})


@api_view(['POST'])
def authorization_api_view(request):
    serializer = AuthValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = authenticate(
        username = serializer.validated_data.get('username'),
        password = serializer.validated_data.get('password')
    )
    if user is not None:
        try:
            token_ = Token.objects.get(user=user)
        except:
            token_ = Token.objects.create(user=user)
        return Response(data={'key': token_.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def users_confirm_api_view(request):
    code = request.data.get('code')
    try:
        user_active = UserActive.objects.get(code=code)
    except UserActive.DoesNotExist:
        return Response({'error': 'Invalid code'}, status=status.HTTP_400_BAD_REQUEST)
    user = user_active.user
    if not user.is_active:
        user.is_active = True
        user.save()
        return Response({'message': 'User activated successfully'}, status=status.HTTP_200_OK)
    return Response({'message':'User is already active'},
                    status=status.HTTP_200_OK)

