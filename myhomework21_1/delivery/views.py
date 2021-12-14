from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from delivery.forms import ShopForm
from delivery.models import Shop, Category


def shop_list(request: HttpRequest) -> HttpResponse:
    category_qs = Category.objects.all()
    qs = Shop.objects.all()

    category_id = request.GET.get()

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains="query")
    return render(request, "delivery/shop_list.html", {
        "shop_list": qs,
    })


def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, "delivery/shop_detail.html", {
        "shop": shop,
    })


def shop_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            saved_shop = form.save()
            return redirect("delivery:shop_detail", saved_shop.pk)
    else:
        form = ShopForm
    return render(request, "delivery/shop_form.html", {
        "form": form,
    })


def shop_edit(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            saved_shop = form.save
            return redirect("delivery:shop_detail", saved_shop.pk)
    else:
        form = ShopForm(instance=shop)
    return render(request, "delivery/shop_form.html", {
        "form": form,
    })
