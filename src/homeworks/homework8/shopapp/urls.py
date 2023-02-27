from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stores/',views.stores, name = "stores"),
    path('store/<int:storeid>/', views.store, name='store'),
    path('item/<int:itemid>/',views.item,name = 'item'),
    path('storecategories/', views.storecategories,name="storecategories"),
    path('storecategory/<int:storecategid>/',views.storecategory,name = "storecategroy"),
    path('itemcategories/', views.itemcategories, name = "itemcategories"),
    path('itemcategory/<int:itemcategid>/',views.itemcategory,name = "itemcategroy"),
    path('bag/<int:costumerid>/', views.bag, name='bag'),
    ]