from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, resolve_url
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from shop.forms import ReviewForm
from shop.mixins import ReviewUserCheckMixin
from shop.models import Shop, Category, Review


class ShopListView(ListView):
    model = Shop
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["category_list"] = Category.objects.all()
        return context_data


shop_list = ShopListView.as_view()


shop_detail = DetailView.as_view(
    model=Shop
)


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    # form_vaild에서 직접 URL이동하기에
    # 아래에 success_url 설정은 불필요
    # success_url = reverse_lazy("shop:shop_list")

    # 유효성 검사에 통과한다면...
    def form_valid(self, form) -> HttpResponse:
        # self.kwargs : URL Captured 값들이 사전으로 저장
        shop_pk = self.kwargs["shop_pk"]
        shop = get_object_or_404(Shop, pk=shop_pk)

        review = form.save(commit=False)
        review.shop = shop
        review.user = self.request.user
        review.save()
        # return redirect("shop:shop_detail", shop.pk)
        return redirect(shop)      # HttpResponse는 redirect 함수로 호출


review_new = ReviewCreateView.as_view()


class ReviewUpdateView(LoginRequiredMixin, ReviewUserCheckMixin, UpdateView):    # 다중상속 둘 모두 부모
    model = Review
    form_class = ReviewForm
    # success_url = reverse_lazy("shop:shop_list")

    def get_success_url(self) -> str:
        review = self.object
        return resolve_url(review.shop)   # 문자열일 경우 resolve_url 함수로 호출


review_edit = ReviewUpdateView.as_view()

