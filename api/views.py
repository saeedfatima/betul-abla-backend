from .models import Borehole, Orphan, Report
from .serializers import BoreholeSerializer,UserSerializer, OrphanSerializer, ReportSerializer
from rest_framework import generics
from .models import User
# Borehole Views
class BoreholeListCreateView(generics.ListCreateAPIView):
    queryset = Borehole.objects.all().order_by('-id')
    serializer_class = BoreholeSerializer

class BoreholeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Borehole.objects.all()
    serializer_class = BoreholeSerializer

# Orphan Views
class OrphanListCreateView(generics.ListCreateAPIView):
    queryset = Orphan.objects.all().order_by('-id')
    serializer_class = OrphanSerializer

class OrphanRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orphan.objects.all()
    serializer_class = OrphanSerializer

# Report Views
class ReportListCreateView(generics.ListCreateAPIView):
    queryset = Report.objects.all().order_by('-created_date')
    serializer_class = ReportSerializer

class ReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-created_date')
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

