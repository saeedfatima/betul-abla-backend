from .models import Borehole, Orphan, Report
from rest_framework import serializers

class BoreholeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borehole
        fields = '__all__'


class OrphanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orphan
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'full_name', 'email', 'role',
            'is_active', 'last_login', 'created_date',
            'permissions', 'assigned_regions'
        ]
