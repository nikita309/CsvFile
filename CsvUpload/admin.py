from django.contrib import admin
from . models import UploadCsv
from CsvUpload.models import UploadCsv

class FileAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "Phone1_Type", "phone1_value"]
admin.site.register(UploadCsv, FileAdmin)