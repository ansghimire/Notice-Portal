from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    full_name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=15)
    # re_password = serializers.CharField(max_length=15)

    # class Meta:
    #     model = User
    #     fields = ('id', 'email', 'full_name','password')
    #     read_only_fields = ['id', ]
    #     extra_kwargs = {'password': {'write_only': True}}
    

    # def create(self, validated_data):
    #     # email = validated_data['email']
    #     # full_name = validated_data['full_name']
    #     password = validated_data['password']
    #     re_password = validated_data.pop('re_password')

    #     if password != re_password:
    #         raise serializers.ValidationError("Password must be same")
    #     return User(**validated_data)

        


    