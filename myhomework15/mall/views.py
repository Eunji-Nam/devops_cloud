from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from mall.models import Shop


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    qs = qs.order_by("-pk")
    q = request.GET.get("q", "")
    if q:
        qs = qs.filter(name__icontains=q)
    return render(request, "mall/shop_list.html", {
        "shop_list": qs,
    })

def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = Shop.objects.get(pk=pk)
    return render(request, "mall/shop_detail.html", {
        "shop": shop,
    })
