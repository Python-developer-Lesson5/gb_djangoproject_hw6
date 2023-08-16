from django.contrib import admin
from .models import Product, Client, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'date_registered']
    list_filter = ['date_registered']
    search_fields = ['phone']
    search_help_text = 'Поиск по полю телефон (phone)'


@admin.action(description="Сбросить количество в ноль")
def reset_count(modeladmin, request, queryset):
    queryset.update(count=0)


@admin.action(description="Сбросить цену в ноль")
def reset_price(modeladmin, request, queryset):
    queryset.update(price=0)


@admin.action(description="Сбросить суммарную стоимость заказа")
def reset_total_price(modeladmin, request, queryset):
    queryset.update(total_price=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    list_filter = ['date_added', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'

    actions = [reset_count, reset_price]

    """Отдельный продукт."""
    readonly_fields = ['date_added']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'count'],
            }
        ),
        (
            'Сведения',
            {
                'fields': ['date_added']
            }
        ), ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price']
    list_filter = ['date_ordered', 'total_price']
    actions = [reset_total_price]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)