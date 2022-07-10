from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.hashers import make_password
from rest_framework import generics,viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Accounts as User
from rest_framework.views import APIView
# from .utils import token_gen
from django.utils.encoding import force_bytes, smart_str,force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from .models import Accounts
from django.utils.encoding import force_str
force_text = force_str

from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site

from .models import Accounts
from .permissions import IsAccountOwner
from .serializers import AccountSerializer,ResetPasswordSerializer


class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            # only logged in users can see accounts
            return (permissions.IsAuthenticated(),)  

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            if 'password' not in serializer.validated_data:
                return Response({
                    'error': 'Password required for creating account.'
                }, status=status.HTTP_400_BAD_REQUEST)

            account = Accounts.objects.\
                create_account(**serializer.validated_data)

            # add JWT token to response
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(account)
            token = jwt_encode_handler(payload)

            serializer.validated_data['token'] = token

            return Response(serializer.validated_data, 
                            status=status.HTTP_201_CREATED)

        return Response({
            'error': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        # Hash password but passwords are not required
        if ('password' in self.request.data):
            password = password.encode('utf-8')
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()

    def perform_update(self, serializer):
        # Hash password but passwords are not required
        if ('password' in self.request.data):
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()


class CreateUserAPIView(generics.CreateAPIView):
    # Allow any user (authenticated or not) to access this url 
    serializer_class = AccountSerializer
    permission_classes = (AllowAny,)
 
    def post(self, request):
        print(request.data)
        user = request.data
        my_user = User.objects.create_user(user.values)
        # serializer = AccountSerializer(data=user)
        # my_user.is_valid(raise_exception=True)
        my_user.save()
        return Response(my_user.username, status=status.HTTP_201_CREATED)



class RequestPasswordReset(generics.GenericAPIView):
    """
    Handles reset password request and sends the reset link to the provided email provided it exist in the database
    """
    permission_classes = (AllowAny,)
    serializer_class = ResetPasswordSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']
        if Accounts.objects.filter(email = email).exists():
            user = Accounts.objects.get(email = email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            dormain = get_current_site(request).domain
            link = reverse('password_reset_confirm',kwargs={
            'uidb64': uidb64,
            'token': token
        })
            mydorm = 'localhost:8080'
            activate_url = 'http://'+mydorm+link
            email_sub = 'Madali Password Reset'
            email_body = 'Hello,'+'\n'+'We have received a password reset request from your email. Use this link to reset your password\n'+activate_url

            email = EmailMessage(
                email_sub,
                email_body,
                'noreply@lefla.com',
                [user.email],
            )
            email.send(fail_silently=False)
        return Response({'success': 'Password reset Link has been sent to your email'}, status=status.HTTP_200_OK )

class CurrentUserView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        serializer = AccountSerializer(request.user)
        return Response(serializer.data)