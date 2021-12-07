from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from mall.models import Cloth


def cloth_list(request: HttpRequest) -> HttpResponse:
    qs = Cloth.objects.all()
    qs = qs.order_by("-pk")
    q = request.GET.get("q", "")
    if q:
        qs = qs.filter(name__icontains=q)
    return render(request, "mall/cloth_list.html", {
        "cloth_list":qs,
    })

def cloth_detail(request: HttpRequest, pk: int) -> HttpResponse:
    cloth = Cloth.objects.get(pk=pk)
    review_list = cloth.review_set.all()
    return render(request, "mall/cloth_detail.html", {
        "cloth": cloth,
        "review_list": review_list,
    })
