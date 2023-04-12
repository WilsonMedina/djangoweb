from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
#--------------------------Own folfer----------------------------------------#
from .models import About, Experience, RrSs

#--------------View in admin for model about button import and export----------------------------------------#
class AboutResource(resources.ModelResource):
    class Meta:
        model = About

class AboutAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'state']
    readonly_fields = ['created', 'updated']
    resource_class = AboutResource

admin.site.register(About, AboutAdmin)

#--------------View in admin for model rrss button import and export----------------------------------------#
class RrSsResource(resources.ModelResource):
    class Meta:
        model = RrSs

class RrSsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'url', 'state']
    readonly_fields = ['created', 'updated']
    resource_class = RrSsResource

admin.site.register(RrSs, RrSsAdmin)

#--------------View in admin for model experience button import and export----------------------------------------#
class ExperienceResource(resources.ModelResource):
    class Meta:
        model = Experience

class ExperienceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['position', 'company', 'state']
    readonly_fields = ['created', 'updated']
    resource_class = ExperienceResource

admin.site.register(Experience, ExperienceAdmin)
