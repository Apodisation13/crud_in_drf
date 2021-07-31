from rest_framework.viewsets import ModelViewSet
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer

# from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # фильтрация по параметру в гет-запросе, не нужно если указать в настройках
    # filter_backends = [filters.SearchFilter]

    search_fields = ['title', 'description']  # для фильтрации по ?search=
    ordering_fields = ['title', ]  # для сортировки ?ordering=title

    # def list(self, request, *args, **kwargs):
    # """если здесь переопределить такую функцию, то гет запрос не пройдёт (сообщение фигушки)"""
    #     raise ValidationError('фигушки')


class StockViewSet(ModelViewSet):

    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    filterset_fields = ['products']
    search_fields = ['products__title']
