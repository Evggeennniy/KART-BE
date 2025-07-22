from django.contrib import admin
from orders.models import OrderList, OrderedObject


class OrderedObjectInline(admin.TabularInline):
    model = OrderedObject
    extra = 1
    fields = ('product', 'quantity', 'sale_price', 'discounted_price')
    autocomplete_fields = ['product']


class OrderListAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_method', 'delivery_price', 'notes')
    search_fields = ('notes',)
    list_filter = ('payment_method',)
    inlines = [OrderedObjectInline]


admin.site.register(OrderList, OrderListAdmin)
