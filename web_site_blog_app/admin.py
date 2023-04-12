from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
#-----------------------------------Own files-----------------------------------------------#
from .models import ProfileAuthor, Category, Post

#--------------View in admin for model profile button import and export----------------------------------------#
class ProfileAuthorResource(resources.ModelResource):
    class Meta:
        model = ProfileAuthor

class ProfileAuthorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['author']
    readonly_fields = ['created', 'updated']
    resource_class = ProfileAuthorResource

admin.site.register(ProfileAuthor, ProfileAuthorAdmin)

#--------------View in admin for model category button import and export----------------------------------------#
class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'state']
    readonly_fields = ['created', 'updated']
    resource_class = CategoryResource

admin.site.register(Category, CategoryAdmin)

#--------------View in admin for model post button import and export----------------------------------------#
class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['author', 'timestamp', 'category', 'state']
    readonly_fields = ['created', 'updated']
    resource_class = PostResource

admin.site.register(Post, PostAdmin)

