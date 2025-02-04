from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Productclass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    

class Product(models.Model):
    title = models.CharField(max_length=1000)
    img = models.ImageField(upload_to="./images")
    info = RichTextField()
    descript_text = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    productclass = models.ForeignKey(Productclass, on_delete=models.SET_NULL,null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Topproduct(models.Model):
    img = models.ImageField(upload_to="./images")
    # title = models.CharField(max_length=1000)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class OnlyOneProduct(models.Model):
    img = models.ImageField(upload_to="./images")
    productclass = models.ForeignKey(Productclass, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.productclass.name


class Description(models.Model):
    post = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='description')
    dec_title = models.CharField(max_length=1000)
    dec_info = models.CharField(max_length=1000)

    def __self__(self):
        return self.dec_title

class PopularCategory(models.Model):
    title = models.CharField(max_length=1000)
    img = models.ImageField(upload_to="./images")
    info = RichTextField()
    descript_text = RichTextField()

    def __str__(self):
        return self.title
