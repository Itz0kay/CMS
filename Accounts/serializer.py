from rest_framework import serializers
from Accounts.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email', 'password', 'firstname',
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
    