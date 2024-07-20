from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListCreateApiView.as_view(), name="product_list_create"),
    path('<int:pk>/', views.ProductDetailApiView.as_view(), name="product_deatil"),
    path('<int:pk>/update/', views.ProductUpdateApiView.as_view(), name="product_update"),
    path('<int:pk>/delete/', views.ProductDeletlApiView.as_view(), name="product_delete"),
]