from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Party,Supplier,Driver,PartyTransaction,SupplierTransaction,DriverTransaction


class PartyAdminConfig(UserAdmin):
    model = Party
    
    business_partner_name_type="party_name"
    business_partner_phone_number_type='party_phone_number'
    
    search_fields = ('user',f'{business_partner_name_type}',f'{business_partner_phone_number_type}')
    list_filter = ('user',f'{business_partner_name_type}',f'{business_partner_phone_number_type}')
    ordering = (f'{business_partner_name_type}',)
    list_display = ('user',f'{business_partner_name_type}',f'{business_partner_phone_number_type}')
    fieldsets = (
        ('PartyCredentials', {'fields' : ('user',f'{business_partner_phone_number_type}',)}),
        ('Personal Information', {'fields' : (f'{business_partner_name_type}',)}),
    )
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('user',f'{business_partner_name_type}',f'{business_partner_phone_number_type}',),
        }),
    )
    filter_horizontal = ()
    
admin.site.register(Party,PartyAdminConfig)


class SupplierAdminConfig(UserAdmin):
    model = Supplier
    
    business_partner_name_type="supplier_name"
    business_partner_phone_number_type='supplier_phone_number'
    
    search_fields = ('user',f'{business_partner_name_type}',f'{business_partner_phone_number_type}')
    list_filter = ('user',f'{business_partner_name_type}',f'{business_partner_phone_number_type}')
    ordering = (f'{business_partner_name_type}',)
    list_display = ('user',f'{business_partner_name_type}',f'{business_partner_phone_number_type}')
    fieldsets = (
        ('SupplierCredentials', {'fields' : ('user',f'{business_partner_phone_number_type}',)}),
        ('Personal Information', {'fields' : (f'{business_partner_name_type}',)}),
    )
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('user',f'{business_partner_name_type}',f'{business_partner_phone_number_type}',),
        }),
    )
    filter_horizontal = ()
    
admin.site.register(Supplier,SupplierAdminConfig)

class DriverAdminConfig(UserAdmin):
    model = Driver
    
    business_partner_name_type="driver_name"
    business_partner_phone_number_type='driver_phone_number'
    
    search_fields = ('user',f'{business_partner_name_type}',f'{business_partner_phone_number_type}')
    list_filter = ('user',f'{business_partner_name_type}',f'{business_partner_phone_number_type}')
    ordering = (f'{business_partner_name_type}',)
    list_display = ('user',f'{business_partner_name_type}',f'{business_partner_phone_number_type}')
    fieldsets = (
        ('DriverCredentials', {'fields' : ('user',f'{business_partner_phone_number_type}',)}),
        ('Personal Information', {'fields' : (f'{business_partner_name_type}',)}),
    )
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('user',f'{business_partner_name_type}',f'{business_partner_phone_number_type}',),
        }),
    )
    filter_horizontal = ()
    
admin.site.register(Driver,DriverAdminConfig)

class DriverTransactionAdminConfig(UserAdmin):
    model = DriverTransaction
    
    business_partner_type="driver"
    
    search_fields = ('user',f'{business_partner_type}','transaction_amount','transaction_date','is_received')
    list_filter = ('user',f'{business_partner_type}','transaction_amount','transaction_date','is_received')
    ordering = ('transaction_date',)
    list_display = ('user',f'{business_partner_type}','transaction_amount','transaction_date','is_received')
    fieldsets = (
        ('DriverCredentials', {'fields' : ('user',f'{business_partner_type}',)}),
        ('Personal Information', {'fields' : ('transaction_amount','transaction_date','is_received',)}),
    )
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('user',f'{business_partner_type}','transaction_amount','transaction_date','is_received',),
        }),
    )
    filter_horizontal = ()
    
admin.site.register(DriverTransaction,DriverTransactionAdminConfig)

class SupplierTransactionAdminConfig(UserAdmin):
    model = SupplierTransaction
    
    business_partner_type="supplier"
    
    search_fields = ('user',f'{business_partner_type}','transaction_amount','transaction_date','is_received')
    list_filter = ('user',f'{business_partner_type}','transaction_amount','transaction_date','is_received')
    ordering = ('transaction_date',)
    list_display = ('user',f'{business_partner_type}','transaction_amount','transaction_date','is_received')
    fieldsets = (
        ('SupplierCredentials', {'fields' : ('user',f'{business_partner_type}',)}),
        ('Personal Information', {'fields' : ('transaction_amount','transaction_date','is_received',)}),
    )
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('user',f'{business_partner_type}','transaction_amount','transaction_date','is_received',),
        }),
    )
    filter_horizontal = ()
    
admin.site.register(SupplierTransaction,SupplierTransactionAdminConfig)

class PartyTransactionAdminConfig(UserAdmin):
    model = PartyTransaction
    
    business_partner_type="party"
    
    search_fields = ('user',f'{business_partner_type}','transaction_amount','transaction_date','is_received')
    list_filter = ('user',f'{business_partner_type}','transaction_amount','transaction_date','is_received')
    ordering = ('transaction_date',)
    list_display = ('user',f'{business_partner_type}','transaction_amount','transaction_date','is_received')
    fieldsets = (
        ('PartyCredentials', {'fields' : ('user',f'{business_partner_type}',)}),
        ('Personal Information', {'fields' : ('transaction_amount','transaction_date','is_received',)}),
    )
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('user',f'{business_partner_type}','transaction_amount','transaction_date','is_received',),
        }),
    )
    filter_horizontal = ()
    
admin.site.register(PartyTransaction,PartyTransactionAdminConfig)