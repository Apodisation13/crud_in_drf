from django.contrib import admin

from .models import *


class StockProcuctInline(admin.TabularInline):
    model = StockProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    inlines = [StockProcuctInline, ]
