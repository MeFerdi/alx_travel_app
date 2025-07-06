from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# Add your ViewSets here when you create them
# router.register(r'listings', views.ListingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Add individual API endpoints here
    path('health/', views.health_check, name='health_check'),
]
