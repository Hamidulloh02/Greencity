from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.safestring import mark_safe
from import_export.admin import ExportMixin, ImportExportModelAdmin

# Register your models here.
from .models import Product,Description,Category,Productclass,Brand,Topproduct,OnlyOneProduct,PopularCategory,Images,Status

class DescriptionInline(admin.TabularInline):
    model = Description
    extra = 1
class ImagesInline(admin.TabularInline):  # Klass nomi to‘g‘ri
    model = Images
    extra = 1

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):  # ✅ `Product` emas, `ProductAdmin` bo‘lishi kerak
    list_display = ('image_tag', 'title')
    list_filter = ('category','productclass')
    inlines = [DescriptionInline,ImagesInline]
    

    def image_tag(self, obj):  # ✅ `Product` emas, `obj` bo‘lishi kerak
        if obj.img:  # Rasm borligini tekshiramiz
            return mark_safe(f'<img src="{obj.img.url}" width="80" height="80" style="object-fit:cover; border-radius:5px;" />')
        return "No Image"

# admin.site.register(Product,)
admin.site.register(Status)
admin.site.register(Brand)
admin.site.register(Productclass)
admin.site.register(Category)
admin.site.register(Topproduct)
admin.site.register(OnlyOneProduct)
admin.site.register(PopularCategory)
# admin.site.register(Special)
# admin.site.register(Bestsellers)
# admin.site.register(TopRated)
