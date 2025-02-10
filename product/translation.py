from modeltranslation.translator import register, TranslationOptions
from .models import Product, PopularCategory,TopRated,Special,Bestsellers
@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'info', 'descript_text')

@register(PopularCategory)
class PopularCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'info', 'descript_text')

@register(TopRated)
class TopRatedTranslationOptions(TranslationOptions):
    fields = ('title', 'info', 'descript_text')

@register(Special)
class SpecialTranslationOptions(TranslationOptions):
    fields = ('title', 'info', 'descript_text')

@register(Bestsellers)
class BestsellersTranslationOptions(TranslationOptions):
    fields = ('title', 'info', 'descript_text')