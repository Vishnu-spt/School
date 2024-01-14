# admin.py

from django.contrib import admin
from .models import Department, Course, Material, Order

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'wikipedia_link')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'department', 'course', 'purpose')
    filter_horizontal = ('materials_provide',)  # for a ManyToManyField
