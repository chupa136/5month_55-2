from rest_framework import serializers
from .models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'product_count']

    def get_product_count(self, category):
        return category.products.count()

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category']

class ProductDetailSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ReviewDetailSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = "__all__" 

    def get_product(self, review):
        return review.product.title

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__" 


class ProductReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'rating', 'reviews']

    def get_rating(self, product):
        reviews = product.reviews.all()
        if reviews:
            return sum(review.stars for review in reviews) / reviews.count()
        return 0