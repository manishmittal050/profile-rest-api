from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers  a name filed"""
    name = serializers.CharField(max_length=10)
    