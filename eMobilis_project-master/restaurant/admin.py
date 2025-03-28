from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Reservation, Homepage, Restaurant, Aboutpage, Stories, Chefs,
    Ourmenu, Happy, Testimony, Aboutend, Contact, Footer, Table, Order
)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_id',
        'menu_item_display',
        'client_info',
        'quantity',
        'total_price',
        'order_date_formatted',
        'stock_impact'
    )
    list_filter = ('order_date', 'menu_item__category')
    search_fields = (
        'client_name',
        'client_email',
        'client_phone',
        'menu_item__foodname'
    )
    readonly_fields = ('order_date', 'total_price_display')
    fieldsets = (
        ('Order Information', {
            'fields': (
                'menu_item',
                'quantity',
                'total_price_display',
                'order_date'
            )
        }),
        ('Customer Information', {
            'fields': (
                'client_name',
                'client_email',
                'client_phone',
                'special_requests'
            )
        }),
    )

    def order_id(self, obj):
        return f"Order #{obj.id}"
    order_id.short_description = "Order ID"

    def menu_item_display(self, obj):
        return f"{obj.menu_item.foodname} ({obj.menu_item.category})"
    menu_item_display.short_description = "Menu Item"

    def client_info(self, obj):
        return format_html(
            "{}<br>{}<br>{}",
            obj.client_name,
            obj.client_email,
            obj.client_phone
        )
    client_info.short_description = "Customer Info"

    def total_price(self, obj):
        return f"KSh {obj.menu_item.price * obj.quantity}"
    total_price.short_description = "Total"

    def order_date_formatted(self, obj):
        return obj.order_date.strftime("%b %d, %Y %H:%M")
    order_date_formatted.short_description = "Order Date"
    order_date_formatted.admin_order_field = 'order_date'

    def stock_impact(self, obj):
        remaining = obj.menu_item.stock
        if remaining <= 5:
            return format_html(
                '<span style="color: red; font-weight: bold;">⬇ {} left</span>',
                remaining
            )
        return f"{remaining} left"
    stock_impact.short_description = "Stock After Order"

    def total_price_display(self, obj):
        return self.total_price(obj)
    total_price_display.short_description = "Total Price"

@admin.register(Ourmenu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'foodname',
        'category',
        'price_display',
        'stock_status',
        'menu_item_actions'
    )
    list_filter = ('category',)
    search_fields = ('foodname', 'description')
    actions = ['restock_items']

    def price_display(self, obj):
        return f"KSh {obj.price}"
    price_display.short_description = "Price"

    def stock_status(self, obj):
        if obj.stock <= 5:
            return format_html(
                '<span style="color: red; font-weight: bold;">⚠️ {} Left</span>',
                obj.stock
            )
        return format_html(
            '<span style="color: green;">✓ {}</span>',
            obj.stock
        )
    stock_status.short_description = "Stock"

    def menu_item_actions(self, obj):
        return format_html(
            '<a href="/admin/restaurant/ourmenu/{}/change/">Edit</a> | '
            '<a href="/admin/restaurant/ourmenu/{}/delete/">Delete</a>',
            obj.id, obj.id
        )
    menu_item_actions.short_description = "Actions"

    @admin.action(description="Restock selected items (+10)")
    def restock_items(self, request, queryset):
        for item in queryset:
            item.stock += 10
            item.save()
        self.message_user(
            request,
            f"Successfully restocked {queryset.count()} items."
        )

# Simplified registration for other models
models_to_register = [
    Reservation, Homepage, Restaurant, Aboutpage, Stories,
    Chefs, Happy, Testimony, Aboutend, Contact, Footer, Table
]

for model in models_to_register:
    admin.site.register(model)