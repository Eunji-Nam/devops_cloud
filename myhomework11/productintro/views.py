from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from productintro.models import Introduce


def index(request):
    return render(request, "productintro/index.html")


def introduce_list(request: HttpRequest) -> HttpResponse:

    qs = Introduce.objects.all()
    qs = qs.order_by("-pk")

    q = request.GET.get("q", "")
    if q:
        qs = qs.filter(product_name__icontains=q)

    return render(request, "productintro/introduce_list.html", {
        "introduce_list": qs,
    })


def introduce_detail(request: HttpRequest, pk: int) -> HttpResponse:
    introduce = Introduce.objects.get(pk=pk)
    return render(request, "productintro/introduce_detail.html", {
        "introduce": introduce,
    })

