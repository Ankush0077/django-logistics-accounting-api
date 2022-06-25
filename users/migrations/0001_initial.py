# Generated by Django 4.0.5 on 2022-06-25 21:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_phone_number', models.CharField(max_length=13, primary_key=True, serialize=False, unique=True, verbose_name='phone number of the user')),
                ('is_phone_verified', models.BooleanField(default=False, verbose_name='verification status of phone number')),
                ('current_otp', models.CharField(max_length=6, verbose_name='current otp of the phone number in the database')),
                ('date_joined', models.DateTimeField(default=datetime.datetime(2022, 6, 25, 21, 32, 8, 774017, tzinfo=utc), verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name='name of user')),
                ('email', models.EmailField(max_length=200, verbose_name='email of user')),
                ('city', models.CharField(max_length=100, verbose_name='city of residence')),
                ('work', multiselectfield.db.fields.MultiSelectField(choices=[('Transport Contractor', 'Transport Contractor'), ('Truck Owner', 'Truck Owner'), ('Commission Agent', 'Commission Agent')], max_length=49, verbose_name='occupation of user')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
