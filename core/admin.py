from django.contrib import admin
from .models import Category, Flier, Profile, UserFlier
# Register your models here.
admin.site.register(Profile)
admin.site.register(Flier)
admin.site.register(Category)
admin.site.register(UserFlier)