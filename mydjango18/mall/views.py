from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def cloth_list(request: HttpRequest) -> HttpResponse:
    return render(request, "mall/cloth_list.html", {})

