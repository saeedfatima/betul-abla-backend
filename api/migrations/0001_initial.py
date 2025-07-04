# Generated by Django 5.2.3 on 2025-06-27 17:43

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borehole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_code', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(max_length=255)),
                ('community', models.CharField(max_length=255)),
                ('depth', models.PositiveIntegerField(default=0)),
                ('beneficiaries', models.PositiveIntegerField(default=0)),
                ('contractor', models.CharField(max_length=255)),
                ('cost', models.FloatField(default=0)),
                ('status', models.CharField(choices=[('Planning', 'Planning'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Maintenance', 'Maintenance'), ('Inactive', 'Inactive')], default='Planning', max_length=20)),
                ('water_quality', models.CharField(choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor'), ('Not Tested', 'Not Tested')], default='Not Tested', max_length=20)),
                ('construction_date', models.DateField(blank=True, null=True)),
                ('last_maintenance', models.DateField(blank=True, null=True)),
                ('coordinates', models.CharField(blank=True, max_length=100)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orphan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('location', models.CharField(max_length=255)),
                ('guardian_name', models.CharField(max_length=100)),
                ('monthly_allowance', models.FloatField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Pending', 'Pending'), ('Inactive', 'Inactive')], default='Pending', max_length=10)),
                ('registration_date', models.DateField()),
                ('last_payment', models.DateField(blank=True, null=True)),
                ('school_status', models.CharField(max_length=255)),
                ('health_status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Annual', 'Annual'), ('Impact', 'Impact'), ('Financial', 'Financial'), ('Custom', 'Custom')], max_length=20)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Review', 'Review'), ('Published', 'Published'), ('Archived', 'Archived')], max_length=20)),
                ('created_date', models.DateField()),
                ('published_date', models.DateField(blank=True, null=True)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('tags', models.CharField(max_length=255)),
                ('file_url', models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('full_name', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('coordinator', 'Coordinator'), ('staff', 'Staff')], default='staff', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('permissions', models.JSONField(blank=True, default=list)),
                ('assigned_regions', models.JSONField(blank=True, default=list)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
