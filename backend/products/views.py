from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

# we shouldn't do this if we need to have diff end points 
class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#not gonna use this method
# class ProductListApiView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
