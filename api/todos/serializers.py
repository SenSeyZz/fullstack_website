from rest_framework import serializers
from .models import Todo , Back


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = Todo

class BackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'number',
            'description',
        )
        model = Back

