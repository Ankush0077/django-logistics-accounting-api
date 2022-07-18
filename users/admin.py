from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# @admin.register(User)
# class User(admin.ModelAdmin):
#     list_display=['user_phone_number','date_joined','is_phone_verified']

# from django import forms
# from django.contrib.auth.models import Group
# from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User,UserDetails


# class UserCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     # password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

#     class Meta:
#         model = User,UserDetails
#         fields = ()

#     # def clean_password2(self):
#     #     # Check that the two password entries match
#     #     password1 = self.cleaned_data.get("password1")
#     #     password2 = self.cleaned_data.get("password2")
#     #     if password1 and password2 and password1 != password2:
#     #         raise forms.ValidationError("Passwords don't match")
#     #     return password2

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         # user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class UserChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = User
#         fields = ('user_phone_number', 'current_otp','is_phone_verified', 'date_joined', 'is_active', 'is_staff')

    # def clean_password(self):
    #     # Regardless of what the user provides, return the initial value.
    #     # This is done here, rather than on the field, because the
    #     # field does not have access to the initial value
    #     return self.initial["password"]
    
class UserAdminConfig(UserAdmin):
    # form = UserChangeForm
    # add_form = UserCreationForm
    model = User
    
    search_fields = ('user_phone_number','date_joined')
    list_filter = ('user_phone_number','date_joined','is_phone_verified','is_active','is_staff')
    ordering = ('date_joined',)
    list_display = ('user_phone_number','date_joined','is_phone_verified','is_active','is_staff')
    fieldsets = (
        ('UserCredentials', {'fields' : ('user_phone_number','date_joined','is_phone_verified',)}),
        ('Permissions', {'fields' : ('is_staff','is_active',)}),
        ('Personal Information', {'fields' : ('current_otp','password')}),
    )
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('user_phone_number','current_otp','is_phone_verified','password1','password2','is_active','is_staff',),
        }),
    )
    
admin.site.register(User,UserAdminConfig)

class UserDetailsAdminConfig(UserAdmin):
    # form = UserChangeForm
    # add_form = UserCreationForm
    model = UserDetails
    
    search_fields = ('user','user_name','email','city','work')
    list_filter = ('user','user_name','email','city','work')
    ordering = ('user',)
    list_display = ('user','user_name','email','city','work')
    fieldsets = (
        ('UserCredentials', {'fields' : ('user',)}),
        # ('Permissions', {'fields' : ('is_staff','is_active',)}),
        ('Personal Information', {'fields' : ('user_name','email','city','work',)}),
    )
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('user','user_name','email','city','work',),
        }),
    )
    filter_horizontal = ()
    
admin.site.register(UserDetails,UserDetailsAdminConfig)