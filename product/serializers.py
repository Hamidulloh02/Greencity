from rest_framework import serializers

from product.models import Product,Description,Category,Productclass,Brand,Topproduct,OnlyOneProduct

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')
class ClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = Productclass
        fields = ('id','name')
class BrandSerializers(serializers.ModelSerializer):
    class Meta :
        model = Brand
        fields = ('id','name')

class descriptionSerializers(serializers.ModelSerializer):
    class Meta :
        model = Description
        fields = ('id','post','dec_title','dec_info')
class TopproductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Topproduct
        fields = ('id','img','created_at','updated_at')

class productSerializers(serializers.ModelSerializer):
    category = CategorySerializer()
    productclass = ClassSerializers()
    description = descriptionSerializers(many=True)
    brand = BrandSerializers()
    class Meta:
        model = Product
        fields = ('id','title','img','info','category','productclass','descript_text','description','brand')
class OnlyOneProSerializers(serializers.ModelSerializer):
    productclass = ClassSerializers()
    class Meta:
        model = OnlyOneProduct
        fields = ('img','productclass')