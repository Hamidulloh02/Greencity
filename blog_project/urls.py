from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.views.i18n import set_language
from django.shortcuts import redirect

# 404 sahifasi uchun funksiya
def custom_page_not_found(request, exception):
    return redirect('/')  # Barcha noto‘g‘ri URL'lar asosiy sahifaga yo‘naltiriladi

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # Tarjima URL
    path('set_language/', set_language, name='set_language'),  # Til o'zgartirish
]

# 🌍 Barcha sahifalarni `i18n_patterns` ichida qo‘shamiz!
urlpatterns += i18n_patterns(
    path('', include('product.urls')),  # Asosiy sahifalar
    path('admin/', admin.site.urls),  # Django admin panel
)

# Statik fayllarni qo‘shish
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 404 error uchun sozlama
handler404 = custom_page_not_found
