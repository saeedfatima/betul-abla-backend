from django.urls import path
from .views import (
    BoreholeListCreateView, BoreholeRetrieveUpdateDestroyView,
    OrphanListCreateView, OrphanRetrieveUpdateDestroyView,
    ReportListCreateView, ReportRetrieveUpdateDestroyView,
    UserListCreateView, UserRetrieveUpdateDestroyView
)

urlpatterns = [
    # Boreholes
    path('boreholes/', BoreholeListCreateView.as_view(), name='borehole-list'),
    path('boreholes/<int:pk>/', BoreholeRetrieveUpdateDestroyView.as_view(), name='borehole-detail'),

    # Orphans
    path('orphans/', OrphanListCreateView.as_view(), name='orphan-list'),
    path('orphans/<int:pk>/', OrphanRetrieveUpdateDestroyView.as_view(), name='orphan-detail'),

    # Reports
    path('reports/', ReportListCreateView.as_view(), name='report-list'),
    path('reports/<int:pk>/', ReportRetrieveUpdateDestroyView.as_view(), name='report-detail'),

    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
]
