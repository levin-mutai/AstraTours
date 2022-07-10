from rest_framework import serializers
from .models import Accounts
from rest_framework.serializers import (
    CharField,
    ModelSerializer)

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Accounts
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at',)



class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length = 2)
    class Meta:
        fields = ['email']
