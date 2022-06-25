from rest_framework import serializers
from .models import Party,Supplier,Driver,PartyTransaction,SupplierTransaction,DriverTransaction

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ['user','party_name','party_phone_number']
        
        def validate_party_phone_number(self, phone_number):
            if len(phone_number)!=13 or phone_number!=None:
                raise serializers.ValidationError('Wrong Phone Number')
            return phone_number
        
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['user','supplier_name','supplier_phone_number']
        
        def validate_supplier_phone_number(self, phone_number):
            if len(phone_number)!=13 or phone_number!=None:
                raise serializers.ValidationError('Wrong Phone Number')
            return phone_number
        
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['user','driver_name','driver_phone_number']
        
        def validate_driver_phone_number(self, phone_number):
            if len(phone_number)!=13 or phone_number!=None:
                raise serializers.ValidationError('Wrong Phone Number')
            return phone_number
        

class PartyTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyTransaction
        fields = ['party','transaction_amount','is_received']
        
class SupplierTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierTransaction
        fields = ['supplier','transaction_amount','is_received']
        
class DriverTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverTransaction
        fields = ['driver','transaction_amount','is_received']