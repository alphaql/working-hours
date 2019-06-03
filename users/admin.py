from django.contrib import admin
from users.models import User
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class UserResouce(resources.ModelResource):
    class Meta:
        model = User


class UserAdmin(ImportExportModelAdmin):
    pass


admin.site.register(User, UserAdmin)
