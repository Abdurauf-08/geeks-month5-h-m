from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from .models import Product, Category
from .serializer import ProductSerializer, ProductDetailSerializer, CategorySerializer, CategoryDetailSerializer


@api_view(['GET'])
def product_list_api_view(request):
    product = Product.objects.all()
    list_ = ProductSerializer(product, many=True).data
    return Response(data=list_)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
            product = Product.objects.get(id=id)
    except Product.DoesNotExist:
            return Response(data={'error': 'product not found'},
                            status=status.HTTP_404_NOT_FOUND)
    
    data = ProductDetailSerializer(product, many=False).data
    return Response(data=data)


@api_view(['GET'])
def category_list_api_view(request):
    category = Category.objects.all()
    list_ = CategorySerializer(category, many=True).data
    return Response(data=list_)


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': 'category not found'},
                                status=status.HTTP_404_NOT_FOUND)
        
    data = CategoryDetailSerializer(category, many=False).data
    return Response(data=data)