from django.contrib import admin
from contact.models import Contact, Category

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name', 'last_name', 'phone', 'email',
    ordering = '-id', # o - na frente deixa em ordem decrescente
    search_fields = 'id', 'first_name', 'last_name'
    list_per_page = 20
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name'
    list_display_links = 'id', 'phone'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-name', # o - na frente deixa em ordem decrescente
