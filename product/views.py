from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from .models import Product, Description, Category, Productclass, Brand, Topproduct, OnlyOneProduct, PopularCategory
from .serializers import productSerializers, descriptionSerializers, CategorySerializer, ClassSerializers, BrandSerializers, TopproductSerializers, OnlyOneProSerializers
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf.urls import handler404
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.utils.deprecation import MiddlewareMixin

# from rest_framework.authentication import BaseAuthentication

# Pagination import
from rest_framework.pagination import PageNumberPagination

# Import filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.
def main(request, template_name='index.html'):
    products = Product.objects.all().order_by('-id')  # Fetch all products
    top_products = Product.objects.filter(status__name='new').order_by('-id')[:12]  # Fetch all top products
    top_rateds = Product.objects.filter(status__name='top')
    specials = Product.objects.filter(status__name='special')
    bestsellers = Product.objects.filter(status__name='bestseller')
    latest_products = Product.objects.all().order_by('-id')[:5]
    popularCategorys = PopularCategory.objects.all()
    onlyoneproduct = OnlyOneProduct.objects.all()

    context = {
        'products': products,
        'top_products': top_products,
        'top_rateds': top_rateds,
        'specials': specials,
        'bestsellers': bestsellers,
        'latest_products': latest_products,
        'popularCategorys': popularCategorys,
        'onlyoneproduct': onlyoneproduct,
        'title': _('Main Page'),
        'welcome_message': _('Welcome to our store!'),
    }

    return render(request, template_name, context)

def index(request):
    return main(request, 'index.html')

# # Shop sahifasi

def shop(request):
    return main(request, 'shop.html')

# # Boshqa sahifalar

# def about(request):
#     return main(request, 'shop_detail.html')

def handler404(request,exception):
    return render(request, '404.html',status=404)
def product_list(request):
    products = Product.objects.all().order_by('-id')  # Fetch all products
    return render(request, 'product_list.html', {'products': products})
def shop_list(request):
    products_list = Product.objects.all().order_by('-id')  # Fetch all products
    latest_products = Product.objects.all().order_by('-id')[:5]
    
    # Set up pagination: 10 products per page (you can change this number)
    paginator = Paginator(products_list, 12)
    
    # Get the current page number from the request
    page = request.GET.get('page')
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., page 9999), deliver the last page
        products = paginator.page(paginator.num_pages)
    
    # Pass paginated products to the template
    return render(request, 'shop.html', {'products': products,'latest_products':latest_products})
def shop_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Mahsulotni olib keling
    slidproduct = Product.objects.all()
    categories = Category.objects.all()  # Barcha kategoriyalarni olib keling
    productclass = Productclass.objects.all()
    onlyoneproduct = OnlyOneProduct.objects.all()
    latest_products = Product.objects.all().order_by('-id')[:5]
    return render(request, 'shop_detail.html', {'product': product, 'categories': categories,'productclass':productclass,'onlyoneproduct':onlyoneproduct,'slidproduct':slidproduct,'latest_products':latest_products})

class ProductListView(ListAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = productSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['category__name','category__id','brand__name','productclass__name','title']

    # def get_search_fields(self, request):
    #     search_param = request.GET.get('search', '')
    #     search_list = eval(search_param) if search_param else []
        
    #     search_fields = []
    #     for term in search_list:
    #         search_fields.extend(['title','category__id__icontains', 'category__name__icontains', 'brand__name__icontains'])
    #     return search_fields

    # def get(self, request, *args, **kwargs):
    #     self.search_fields = self.get_search_fields(request)
    #     return super().get(request, *args, **kwargs)

class SingleProductListView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializers

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 9
class ProductPagination(ListAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = productSerializers
    pagination_class = LargeResultsSetPagination
    filter_backends = (DjangoFilterBackend,SearchFilter)
    search_fields = ['category__name','category__id','brand__name','productclass__name']


class CategoryListView(ListAPIView):
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer

class ClassListApiView(ListAPIView):
    queryset = Productclass.objects.all().order_by('id')
    serializer_class = ClassSerializers

class BrandListapiview(ListAPIView):
    queryset = Brand.objects.all().order_by('id')
    serializer_class = BrandSerializers

class TopproductAPiView(ListAPIView):
    queryset = Topproduct.objects.all().order_by('-id')
    serializer_class = TopproductSerializers

class SingleCategoryListView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer

class OnlyProListView(ListAPIView):
    queryset = OnlyOneProduct.objects.all()
    serializer_class = OnlyOneProSerializers

class PopularCategoryView(ListAPIView):
    queryset = PopularCategory.objects.all()

# class LanguageMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         if request.LANGUAGE_CODE == "uz":
#             print("Foydalanuvchi rus tilidan foydalanmoqda.")
#         else:
#             print(f"Foydalanuvchi boshqa til ishlatmoqda: {request.LANGUAGE_CODE}")


