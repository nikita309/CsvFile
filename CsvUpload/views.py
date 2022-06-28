from _typeshed import Self
from django.shortcuts import render
from rest_framework import generics, status
import io, csv, pandas as pd
from rest_framework.response import Response
from .models import UploadCsv
from .serializers import FileUploadSerializer, SaveFileSerializer
from django.core.mail import send_mail

class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = UploadCsv(
                id = row['id'],
                name = row['name'],
                Phone1_Type = row['Phone1_Type'],
                phone1_value = row['phone1_value']
                )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)

