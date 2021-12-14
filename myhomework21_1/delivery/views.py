from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from delivery.models import Shop


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    return render(request, "delivery/shop_list.html", {
        "shop_list": qs,
    })


def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = Shop.objects.get(pk=pk)
    return render(request, "delivery/shop_detail.html", {
        "shop": shop,
    })
