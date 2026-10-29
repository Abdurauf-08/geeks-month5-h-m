from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.Model.Serializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryDetailSerializer(serializers.Model.Serializer):
    class Meta:
        model = Category
        fields = '__all__'