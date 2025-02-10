from django.contrib import admin

# Register your models here.
from .models import Product,Description,Category,Productclass,Brand,Topproduct,OnlyOneProduct,PopularCategory,Special,Bestsellers,TopRated

class DescriptionInline(admin.TabularInline):
    model = Description
    extra = 1

class Technical_specifications(admin.ModelAdmin):
    inlines = [DescriptionInline]
    readonly_fields = ('updated_at','created_at')
    
admin.site.register(Product,Technical_specifications)
admin.site.register(Brand)
admin.site.register(Productclass)
admin.site.register(Category)
admin.site.register(Topproduct)
admin.site.register(OnlyOneProduct)
admin.site.register(PopularCategory)
admin.site.register(Special)
admin.site.register(Bestsellers)
admin.site.register(TopRated)
