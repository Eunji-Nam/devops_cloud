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
    tag_list = cloth.tag_set.all()
    return render(request, "mall/cloth_detail.html", {
        "cloth": cloth,
        "review_list": review_list,
        "tag_list": tag_list,
    })

def tag_detail(request: HttpRequest, tag_category: str) -> HttpResponse:
    qs = Cloth.objects.all()
    qs = qs.filter(tag_set__category=tag_category)
    return render(request, "mall/tag_detail.html", {
        "tag_category": tag_category,
        "cloth_list":qs,
    })