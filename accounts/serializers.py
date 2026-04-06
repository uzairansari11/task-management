from django.contrib.auth import get_user_model
from rest_framework import serializers
User=get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
      confirm_password=serializers.CharField(max_length=40,write_only=True)
      
      class Meta:
            model = User
            fields= ['id','username','email','password','confirm_password']
            extra_kwargs={
                  "password":{
                        "write_only":True
                  }
            }
      
      def validate(self, attrs):
            confirm_password=attrs.get('confirm_password',None)
            password=attrs.get('password',None)
            
            if password != confirm_password :
                  raise serializers.ValidationError({
                        "confirm_password":"Password and confirm password must be same."
                  })
            return attrs
      
      def create(self, validated_data):
            
            validated_data.pop("confirm_password",None)
            password=validated_data.pop("password")
            
            user = User.objects.create_user(password=password,**validated_data)
            
            return user
      

class MeSerializer(serializers.ModelSerializer):
      class Meta:
            model=User
            fields=['id','username','email']