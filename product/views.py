from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from .serializers import (CategorySerializer,ProductSerializer, 
ReviewSerializer,CategoryDetailSerializer, 
ReviewDetailSerializer, ProductDetailSeralizer)


@api_view(['GET'])
def categories_list_api_view(request):
    categories = Category.objects.all()
    data = CategorySerializer(categories, many=True).data
    return Response(
        data=data,
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
def categories_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(
            data={"error": "Category not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    data = CategoryDetailSerializer(category, many=False).data
    return Response(data=data)

@api_view(['GET'])
def products_list_api_view(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data
    return Response(
        data=data,
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
def products_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(
            data={"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    data = ProductDetailSeralizer(product, many=False).data
    return Response(data=data)

@api_view(['GET'])
def reviews_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(
        data=data,
        status=status.HTTP_200_OK
    )
@api_view(['GET'])
def reviews_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(
            data={'error': 'Review not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    data = ReviewDetailSerializer(review, many=False).data
    return Response(data=data)
