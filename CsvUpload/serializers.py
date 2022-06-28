from django.db.models.base import Model
from rest_framework import serializers
from . models import UploadCsv

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class SaveFileSerializer(serializers.Serializer):

    class Meta:
        model = UploadCsv
        fieldS = "__all__"

