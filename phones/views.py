from django.http import HttpResponse
from django.shortcuts import render
from pprint import pprint

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get("sort", 'id')
    phone_list = []
    phones = Phone.objects.all().order_by(sorting)
    for phone_item in phones:
        phone_dict = {}
        phone_dict['id'] = phone_item.id
        phone_dict['name'] = phone_item.name
        phone_dict['image'] = phone_item.image
        phone_dict['price'] = phone_item.price
        phone_dict['release_date'] = phone_item.release_date
        phone_dict['slug'] = phone_item.slug
        phone_list.append(phone_dict)
    context = {'phones': phone_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_list = []
    phone = Phone.objects.get(slug=slug)
    print(phone.name)
    phone_d = {}
    phone_d['id'] = phone.id
    phone_d['name'] = phone.name
    phone_d['image'] = phone.image
    phone_d['price'] = phone.price
    phone_d['release_date'] = phone.release_date
    phone_d['slug'] = phone.slug
    phone_list.append(phone_d)
    context = phone_d
    return render(request, template, context)
    # return HttpResponse(phone_item.name, slug)
