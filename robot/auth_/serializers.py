from rest_framework import serializers

from auth_.models import MainUser
from auth_.token import get_token


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        return MainUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    def validate(self, attrs):
        try:
            user = MainUser.objects.get(username=attrs['username'])
        except:
            raise serializers.ValidationError('User dooes not exist')
        if not user.check_password(attrs['password']):
            raise serializers.ValidationError('Useer does not exist')
        attrs['user'] = user
        return attrs

    def login(self):
        user = self.validated_data['user']
        token = get_token(user)
        return user, token
