from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

@swagger_auto_schema(
    method='get',
    operation_description="Health check endpoint",
    responses={200: openapi.Response('Success', openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'status': openapi.Schema(type=openapi.TYPE_STRING),
            'message': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ))}
)
@api_view(['GET'])
def health_check(request):
    """
    Simple health check endpoint to verify the API is working.
    """
    return Response({
        'status': 'healthy',
        'message': 'ALX Travel App API is running successfully!'
    }, status=status.HTTP_200_OK)
