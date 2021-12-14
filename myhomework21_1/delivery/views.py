from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from delivery.models import Shop


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    return render(request, "delivery/shop_list.html", {
        "shop_list": qs,
    })
