from rest_framework import serializers
from .models import Messages
from .models import Account


class MessagesSerializer(serializers.ModelSerializer):

  class Meta:
    model = Messages
    fields = ("id", "message")

#new user registration
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ('email', 'username', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = Account(email = self.validated_data['email'], username = self.validated_data['username'])

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords do not match!'})
        
        user.set_password(password)
        user.save()

        return user
    
  
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'email']