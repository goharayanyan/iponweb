from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import ItemCategory,Item,Store,StoreCategory,MyBag,Costumer
from django.http import Http404


def index(request):
    items = Item.objects.order_by('name')[:20]
    context = {
        'items': items,
    }
    return render(request, 'shopapp/index.html', context)
    

def item(request,itemid):
    the_item = get_object_or_404(Item,pk = itemid)
    return render(request, 'shopapp/item.html',{'item':the_item})

def stores(request):
    stores = Store.objects.order_by("name")
    context = {
        'stores': stores,
    }
    return render(request, 'shopapp/stores.html', context)

def store(request,storeid):
    items = Item.objects.filter(store__id = storeid).order_by('name')
    context = {
        'items': items,
    }
    return render(request, 'shopapp/store.html', context)

def storecategories(request):
    categories = StoreCategory.objects.all()
    return render(request, 'shopapp/storecatgories.html', {'categories': categories })

def storecategory(request,storecategid):
    stores = Store.objects.filter(category__id = storecategid).order_by('name')
    return render(request, 'shopapp/storecategory.html', {'stores': stores })

def itemcategories(request):
    categories = ItemCategory.objects.all()
    return render(request, 'shopapp/itemcategories.html', {'categories': categories })

def itemcategory(request,itemcategid):
    items = Item.objects.filter(category__id = itemcategid).order_by('name')
    return render(request, 'shopapp/itemcategory.html', {'items': items })

def bag(request,costumerid):
    mybag = get_object_or_404(MyBag, costumer__id = costumerid)
    return render(request, 'shopapp/bag.html',{'items':mybag.items.all()})
