from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from mall.models import Cloth


def cloth_list(request: HttpRequest) -> HttpResponse:
    qs = Cloth.objects.all()
    qs = qs.order_by("-pk")
    return render(request, "mall/cloth_list.html", {})
