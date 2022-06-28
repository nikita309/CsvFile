from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class  UploadCsv(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    Phone1_Type = models.CharField(max_length=20, blank= False)
    phone1_value = PhoneNumberField()

