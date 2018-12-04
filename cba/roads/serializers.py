from rest_framework import serializers

from .models import Section


class BaseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
