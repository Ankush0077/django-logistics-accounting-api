from django.utils import timezone
from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Party(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    party_name= models.CharField(_('name of party'),max_length=100)
    party_phone_number=models.CharField(_('phone number of party'),max_length=13,unique=True,primary_key=True)
    
    USERNAME_FIELD = 'party_phone_number'
    REQUIRED_FIELDS = ['user','party_name']
    
    def __str__(self):
        return self.party_phone_number

class Supplier(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    supplier_name= models.CharField(_('name of supplier'),max_length=100)
    supplier_phone_number=models.CharField(_('phone number of supplier'),max_length=13,unique=True,primary_key=True)
    
    USERNAME_FIELD = 'supplier_phone_number'
    REQUIRED_FIELDS = ['user','supplier_name']
    
    def __str__(self):
        return self.supplier_phone_number

    
class Driver(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)   
    driver_name= models.CharField(_('name of driver'),max_length=100)
    driver_phone_number=models.CharField(_('phone number of driver'),max_length=13,unique=True,primary_key=True)
    
    USERNAME_FIELD = 'driver_phone_number'
    REQUIRED_FIELDS = ['user','driver_name']
    
    def __str__(self):
        return self.driver_phone_number

    

class PartyTransaction(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    party=models.ForeignKey(Party,on_delete=models.CASCADE)
    transaction_amount=models.IntegerField(_('amount of transaction'))
    transaction_date=models.DateTimeField(_("date of transaction"), default=timezone.now())
    is_received=models.BooleanField(_('amount given or received(if received tick the check box)'))
    
    USERNAME_FIELD = 'party'
    REQUIRED_FIELDS = ['transaction_amount','is_received']
    
    def __str__(self):
        return self.phone_number
    
class SupplierTransaction(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    supplier=models.ForeignKey(Party,on_delete=models.CASCADE)
    transaction_amount=models.IntegerField(_('amount of transaction'))
    transaction_date=models.DateTimeField(_("date of transaction"), default=timezone.now())
    is_received=models.BooleanField(_('amount given or received(if received tick the check box)'))
    
    USERNAME_FIELD = 'supplier'
    REQUIRED_FIELDS = ['transaction_amount','is_received']
    
    def __str__(self):
        return self.phone_number
    
class DriverTransaction(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    driver=models.ForeignKey(Party,on_delete=models.CASCADE)
    transaction_amount=models.IntegerField(_('amount of transaction'))
    transaction_date=models.DateTimeField(_("date of transaction"), default=timezone.now())
    is_received=models.BooleanField(_('amount given or received(if received tick the check box)'))
    
    USERNAME_FIELD = 'driver'
    REQUIRED_FIELDS = ['transaction_amount','is_received']
    
    def __str__(self):
        return self.phone_number