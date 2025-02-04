from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from .views import ProductListView,CategoryListView,SingleCategoryListView,ProductPagination,SingleProductListView,ClassListApiView,BrandListapiview,TopproductAPiView,OnlyProListView,main,shop_list,shop_detail,PopularCategoryView

urlpatterns = [
    path('',main),
    path('shop/',shop_list, name='shop_list'),
    path('shop/<int:pk>',shop_detail,name='shop_detail'),
    path('<int:pk>',SingleProductListView.as_view()),
    path('category',CategoryListView.as_view()),
    path('category/<int:pk>',SingleCategoryListView.as_view()),
    path('class',ClassListApiView.as_view()),
    path('brand',BrandListapiview.as_view()),
    path('topproduct',TopproductAPiView.as_view()),
    path('pagination',ProductPagination.as_view()),
    path('producclass',OnlyProListView.as_view()),
    path('popular', PopularCategoryView.as_view())

]
# if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)