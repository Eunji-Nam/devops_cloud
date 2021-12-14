from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from mall.models import Cloth
from mall.form import ClothForm


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


def cloth_new(request: HttpRequest) -> HttpResponse:
    # raise NotImplementedError("곧 구현할 예정")
    if request.method == "POST":
         form = ClothForm(request.POST, request.FILES)
         if form.is_valid():
             saved_post = form.save()

             # shop_detail 뷰를 구현했다면,
             return redirect("mall:cloth_detail", saved_post.pk)
    else:
        form = ClothForm()
    return render(request, "mall/cloth_form.html", {
        "form": form,
    })



def tag_detail(request: HttpRequest, tag_category: str) -> HttpResponse:
    qs = Cloth.objects.all()
    qs = qs.filter(tag_set__category=tag_category)
    return render(request, "mall/tag_detail.html", {
        "tag_category": tag_category,
        "cloth_list": qs,
    })