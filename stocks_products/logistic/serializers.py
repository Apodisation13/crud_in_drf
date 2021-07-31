from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import *


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

    # def create(self, validated_data):
    #     """если сделать так, что нельзя будет создать объект продукт"""
    #     raise ValidationError('ХРЕН ТЕБЕ')


class ProductPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockProduct
        fields = ['id', 'product', 'quantity', 'price']


class StockSerializer(WritableNestedModelSerializer):
    """красота... огромное спасибо beda-software, явно русские)))))"""
    positions = ProductPositionSerializer(
        many=True,
        # read_only=True  # вот это чтобы можно было создать как бы пустой склад, не заполняя его
    )

    class Meta:
        model = Stock
        fields = "__all__"

#     def create(self, validated_data):
#         """нужен полюбак для m2m если не указано read_only=True"""
#         positions = validated_data.pop('positions')
#
#         stock = super().create(validated_data)
#
#         for position in positions:
#             StockProduct.objects.create(stock=stock, **position)
#
#         return stock
#
#     def update(self, instance, validated_data):
#         """как же всё-таки это надо было написать??"""

#         # достаем связанные данные для других таблиц
#         positions = validated_data.pop('positions')
#         print(positions)
#
#         # обновляем склад по его параметрам
#         stock = super().update(instance, validated_data)
#         print(stock)
#
#         # здесь вам надо обновить связанные таблицы
#         # в нашем случае: таблицу StockProduct
#         # с помощью списка positions
#
#         for position in positions:
#             StockProduct.objects.filter(
#                             product_id=position.get('product_id'),
#                             stock_id=position.get('stock_id')
#                         ).update_or_create(
#                             defaults={
#                                 'price': position.get('price'),
#                                 'quantity': position.get('quantity'),
#                                 'product_id': position.get('product_id'),
#                                 'stock_id': position.get('stock_id'),
#                             }
#                         )
#         return stock
