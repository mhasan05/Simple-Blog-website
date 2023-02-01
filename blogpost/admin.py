from django.contrib import admin
from .models import BlogModel,CatagoryModel
from tinymce.widgets import TinyMCE
# Register your models here.
@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title','created','author']
    formfield_overrides = {BlogModel.description : {'widget': TinyMCE()}}


@admin.register(CatagoryModel)
class CatagoryModelAdmin(admin.ModelAdmin):
    list_display = ['name',]