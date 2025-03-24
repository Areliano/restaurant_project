from django.contrib import admin
from django.utils.html import format_html
from .models import (Customer, Homepage, Restaurant, Aboutpage, Stories, Chefs,
                     Ourmenu, Happy, Testimony, Aboutend, Contact, Footer, Table, Order)

# Register models
admin.site.register(Customer)
admin.site.register(Homepage)
admin.site.register(Restaurant)
admin.site.register(Aboutpage)
admin.site.register(Stories)
admin.site.register(Chefs)
admin.site.register(Happy)
admin.site.register(Testimony)
admin.site.register(Aboutend)
admin.site.register(Contact)
admin.site.register(Footer)
admin.site.register(Table)
admin.site.register(Order)

# Admin customization for Ourmenu
class MenuAdmin(admin.ModelAdmin):
    list_display = ("foodname", "category", "price", "stock_status")

    def stock_status(self, obj):
        if obj.stock <= 5:  # Low stock threshold
            return format_html('<span style="color: red; font-weight: bold;">⚠️ {} Left</span>', obj.stock)
        return obj.stock

    stock_status.short_description = "Stock"

admin.site.register(Ourmenu, MenuAdmin)  # ✅ Corrected registration

