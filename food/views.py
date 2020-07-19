from django.shortcuts import render
from .models import Item, Package
# Create your views here.


def food(request):
    items = [item for item in Item.objects.all()]
    data = {
        'title': 'Foods',
        'items': items[:3],
    }
    return render(request, 'food/index.html', context=data)


def package(request):
    packages = [pack for pack in Package.objects.all()]

    data = {
        'title': 'Packages',
        'packages1': {
            'name': packages[0].name,
            'price': packages[0].price,
            'item_list': packages[0].item_list
        },
        'packages2': {
            'name': packages[1].name,
            'price': packages[1].price,
            'item_list': packages[1].item_list
        },
        'packages3': {
            'name': packages[2].name,
            'price': packages[2].price,
            'item_list': packages[2].item_list
        }
    }
    return render(request, 'package/index.html', context=data)


def contact(request):
    return render(request, 'contact/index.html')