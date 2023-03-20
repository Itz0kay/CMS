from rest_framework import serializers
from Accounts.models import *
from rest_framework.validators import UniqueValidator

from coolname import generate_slug

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=3, max_length=50, validators=[UniqueValidator(queryset=User.objects.all())], 
        allow_null=True, default=None)

    class Meta:
        model = User
        fields = [
            'email', 'password', 'firstname', 'username',
            'lastname', 'address', 'phone',
            'city', 'state', 'country', 'pincode'
        ]
        extra_kwargs = {
            'password' : {'write_only' : True }
        }

    def create(self, validated_data): # Updating password 
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    def validate_username(self, val):
        return val or generate_slug()

    