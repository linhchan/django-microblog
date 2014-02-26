from django.contrib import admin
from myblog.models import Post
from myblog.models import Category, SampleModel
from django import forms
from django.db import models

class SampleModelAdmin(admin.ModelAdmin):
	formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
	class Media:
	    js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.
        
admin.site.register(SampleModel,SampleModelAdmin)
admin.site.register(Post)
admin.site.register(Category)
