from django.contrib import admin

from .models import *


class StoreCategoryAdmin(admin.ModelAdmin):
    list_display = ("name","picture")

class ItemCategoryAdmin(admin.ModelAdmin):
        list_display = ("name","picture")

class CostumerAdmin(admin.ModelAdmin):
        list_display = ("user","picture")

class StoreOwnerAdmin(admin.ModelAdmin):
        list_display = ("user","picture")

class StoreAdmin(admin.ModelAdmin):
        list_display = ("name","category","picture")

class ItemAdmin(admin.ModelAdmin):
        list_display = ("name","picture","category","price","info","store")

class MyBagAdmin(admin.ModelAdmin):
    ordering = ['costumer']
    def get_items(self, obj):
        return ",".join([item.name for item in obj.items.all()])

    list_display = ('id', 'costumer', 'get_items', 'total_price')

class PurchaseAdmin(admin.ModelAdmin):
    def get_items(self, obj):
        return ",".join([item.name for item in obj.items.all()])

    list_display = ('id', 'get_items', 'total_price')


admin.site.register(StoreCategory,StoreCategoryAdmin)
admin.site.register(ItemCategory,ItemCategoryAdmin)
admin.site.register(Costumer,CostumerAdmin)
admin.site.register(StoreOwner,StoreOwnerAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(MyBag,MyBagAdmin)
admin.site.register(Purchase,PurchaseAdmin)
