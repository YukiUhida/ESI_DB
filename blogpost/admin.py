from django.contrib import admin
from .models import BlogModel , question_Model
# Register your models here.

#admin.site.register(SampleModel)
admin.site.register(BlogModel)
admin.site.register(question_Model)