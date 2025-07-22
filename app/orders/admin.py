from django.contrib import admin
from orders.models import OrderedObject, OrderList


class OrderedObjectAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'sale_price', 'discounted_price')
    list_filter = ('product',)
    search_fields = ('product__name',)
    autocomplete_fields = ('product',)


class OrderedObjectInline(admin.TabularInline):
    model = OrderList.included.through
    extra = 1
    verbose_name = "Ordered Object"
    verbose_name_plural = "Ordered Objects"
    autocomplete_fields = ['orderedobject']


class OrderListAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_method', 'delivery_price', 'notes')
    list_filter = ('payment_method',)
    search_fields = ('notes',)
    inlines = [OrderedObjectInline]
    exclude = ('included',)


admin.site.register(OrderedObject, OrderedObjectAdmin)
admin.site.register(OrderList, OrderListAdmin)
