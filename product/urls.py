from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories_list_api_view),
    path('<int:id>/', views.categories_detail_api_view),
    path('', views.products_list_api_view),
    path('<int:id>/', views.products_detail_api_view),
    path('', views.reviews_list_api_view),
    path('<int:id>', views.reviews_detail_api_view),
    path('api/v1/products/reviews/', views.products_reviews_api_view),
]