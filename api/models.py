from django.db import models

class Borehole(models.Model):
    STATUS_CHOICES = [
        ('Planning', 'Planning'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Maintenance', 'Maintenance'),
        ('Inactive', 'Inactive'),
    ]

    WATER_QUALITY_CHOICES = [
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
        ('Not Tested', 'Not Tested'),
    ]

    project_code = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=255)
    community = models.CharField(max_length=255)
    depth = models.PositiveIntegerField(default=0)
    beneficiaries = models.PositiveIntegerField(default=0)
    contractor = models.CharField(max_length=255)
    cost = models.FloatField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Planning')
    water_quality = models.CharField(max_length=20, choices=WATER_QUALITY_CHOICES, default='Not Tested')
    construction_date = models.DateField(null=True, blank=True)
    last_maintenance = models.DateField(null=True, blank=True)
    coordinates = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.proj

class Orphan(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Pending', 'Pending'),
        ('Inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    location = models.CharField(max_length=255)
    guardian_name = models.CharField(max_length=100)
    monthly_allowance = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    registration_date = models.DateField()
    last_payment = models.DateField(null=True, blank=True)
    school_status = models.CharField(max_length=255)
    health_status = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Report(models.Model):
    TYPE_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Annual', 'Annual'),
        ('Impact', 'Impact'),
        ('Financial', 'Financial'),
        ('Custom', 'Custom'),
    ]

    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Review', 'Review'),
        ('Published', 'Published'),
        ('Archived', 'Archived'),
    ]

    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_date = models.DateField()
    published_date = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=255)
    file_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('coordinator', 'Coordinator'),
        ('staff', 'Staff'),
    ]

    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    permissions = models.JSONField(default=list, blank=True)  # or use ManyToMany with a custom Permission model
    assigned_regions = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.username
