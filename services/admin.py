from django.contrib import admin
from .models import ServiceCategory, Quote, Product


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'resolution_dpi')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        'client_name',
        'company_email',
        'phone',
        'material_choice',
        'finish_type',
        'submitted_at',
    )
    list_filter = ('material_choice', 'finish_type', 'submitted_at')
    search_fields = ('client_name', 'company_email', 'message')
    readonly_fields = ('submitted_at',)
    date_hierarchy = 'submitted_at'
    ordering = ('-submitted_at',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)

