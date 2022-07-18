from functools import partial
import json
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import UserSerializer,UserDetailsSerializer
from .models import User, UserDetails
from rest_framework import status,viewsets
from random import randint
import requests
import urllib.request
import urllib.parse
from rest_framework.renderers import JSONRenderer

def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

# class OtpAPI(APIView):
#     def get(self,request,user_phone_number=None,format=None):
#         if user_phone_number is not None:
#             otp=User.objects.get(user_phone_number=user_phone_number)
#             serializer=UserSerializer(otp)
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         otp=User.objects.all()
#         serializer=UserSerializer(otp,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def post(self,request,format=None):
#         serializer=UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self,request,user_phone_number,format=None):
#         otp=User.objects.get(user_phone_number=user_phone_number)
#         serializer=UserSerializer(otp,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated'},status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self,request,user_phone_number,format=None):
#         otp=User.objects.get(user_phone_number=user_phone_number)
#         serializer=UserSerializer(otp,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data Updated'},status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,user_phone_number,format=None):
#         otp=User.objects.get(user_phone_number=user_phone_number)
#         otp.delete()
#         return Response({'msg':'Data Deleted'},status=status.HTTP_200_OK)
# class TranspeOtpAPI(APIView):
@api_view(['POST','PUT','PATCH'])
def OtpAPI(request):
    res = {'msg':'OTP Sent Successfully!!'}
    # json_data = JSONRenderer().render(res)
    # return Response(res,status=status.HTTP_200_OK)
    data = json.loads(request.body.decode("utf-8"))
    # return Response(request,status=status.HTTP_200_OK)
    user_phone_number:str=data['user_phone_number']
    # return Response(user_phone_number,status=status.HTTP_200_OK)
    if request.method == 'POST' or 'PUT' or 'PATCH':
        try:
            otp=User.objects.get(user_phone_number=user_phone_number)
            # serializer=UserSerializer(otp)
            # return Response(serializer.data,status=status.HTTP_200_OK)
            
        except:
            current_otp=randint(100000,999999)
            user={
                        'user_phone_number':user_phone_number,
                        'is_phone_verified':False,
                        'current_otp': current_otp,
                        'is_active': True,
                        
                    }
            serializer=UserSerializer(data=user)
            if serializer.is_valid():
                serializer.save()
                requests.post('https://textbelt.com/intl',{
                    'phone':f'+91{user_phone_number}',
                    'message':f'TransPe-{current_otp} is verification code for your number {user_phone_number}',
                    'key':'textbelt',
                    'carrier':'%s@airtelmail.com'
                })
                resp=sendSMS('NDM2Zjc4NGEzMjc3NzU0MjQ5NWE1MTM2NmE0YTQ0NTk=', user_phone_number,
                        'TransPe', f'TransPe-{current_otp} is verification code for your number {user_phone_number}')
                # print(resp)
                return Response({'msg':'OTP Sent Successfully!!'},status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            current_otp=randint(100000,999999)
            user={
                        'user_phone_number':user_phone_number,
                        'is_phone_verified':False,
                        'current_otp': current_otp,
                        'is_active': True,
                }
            serializer=UserSerializer(otp,data=user)
            if serializer.is_valid():
                serializer.save()
                # requests.post('https://textbelt.com/text',{
                #         'phone':f'+91{user_phone_number}',
                #         'message':f'TransPe-{current_otp} is verification code for your number {user_phone_number}',
                #         'key':'textbelt'
                # })
                resp=sendSMS('NDM2Zjc4NGEzMjc3NzU0MjQ5NWE1MTM2NmE0YTQ0NTk=', user_phone_number,
                        'TransPe', f'TransPe-{current_otp} is verification code for your number {user_phone_number}')
                print(resp)
                return Response({'msg':'OTP Sent Successfully!!'},status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method =='GET':
        if user_phone_number is not None:
            otp=User.objects.get(user_phone_number=user_phone_number)
            serializer=UserSerializer(otp)
            return Response(serializer.data.get("current_otp"),status=status.HTTP_200_OK)
        otp=User.objects.all()
        serializer=UserSerializer(otp,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class USerReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetailsModelViewSet(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer