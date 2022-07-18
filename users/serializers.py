from rest_framework import serializers
from .models import User,UserDetails

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserDetails
        fields=['user','user_name','email','city','work']
        
    # def validate_user_phone_number(self, user_phone_number):
    #     if len(user_phone_number)!=13:
    #         raise serializers.ValidationError('Wrong Phone Number')
    #     return user_phone_number
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['user_phone_number','current_otp','is_phone_verified','date_joined','is_active','is_staff']
        
    def validate_user_phone_number(self, user_phone_number):
        if len(user_phone_number)!=13:
            raise serializers.ValidationError('Wrong Phone Number')
        return user_phone_number
    
    def validate_current_otp(self, current_otp):
        if len(current_otp)!=6:
            raise serializers.ValidationError('Wrong OTP')
        return current_otp