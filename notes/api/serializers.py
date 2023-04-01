from rest_framework import serializers
from . models import Note

class noteserial(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields='__all__'
