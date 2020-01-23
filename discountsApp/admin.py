from django.contrib import admin
from .models import Product

# Register your models here.
#admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #all the info show to user
    list_display =('Product_ID','ProductName','PubTime','Tag','click','isExpired')

    ordering = ('PubTime',)

    list_editable = ['ProductName','Tag']

    date_hierarchy = 'PubTime'

    search_fields = ['Tag','EndTime','isExpired']