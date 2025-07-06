from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    host = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price_per_night', 'location', 
                 'created_at', 'updated_at', 'host']
        read_only_fields = ['id', 'created_at', 'updated_at']
