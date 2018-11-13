from django.contrib import admin
from registration_app.models import User
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(User)

class ViewAdmin(ImportExportModelAdmin):
    pass
