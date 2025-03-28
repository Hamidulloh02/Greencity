from modeltranslation.translator import register, TranslationOptions
from .models import Product, PopularCategory,Productclass
@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'info', 'descript_text')

@register(PopularCategory)
class PopularCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'info', 'descript_text')

@register(Productclass)
class ProductclassTranslationOptions(TranslationOptions):
    fields = ('name',)


