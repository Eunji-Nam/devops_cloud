# Class Based View(CBV)
#   - 뷰 함수를 만들어주는 클래스
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import PostForm
from blog.models import Post, Subscriber

# post_list
post_list = ListView.as_view(
    model=Post,
)

# post_detail
post_detail = DetailView.as_view(
    model=Post,
)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # success_url = reverse_lazy("blog:post_list")

    # def get_success_url(self):
    #     # self.object  # 저장된 모델 인스턴스
    #     post_pk = self.object.pk
    #     return reverse("blog:post_detail", args=[post_pk])  # 문자열
        # return resolve_url("blog:post_detail", post_pk)  # 문자열
        # return redirect   ("blog:post_detail", post_pk)  # HttpResponse
        #            {% url "blog:post_detail" post_pk %}  #문자열


# post_new
post_new = PostCreateView.as_view()


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    # def get_success_url(self):
    #     post_pk = self.object.pk
    #     return reverse("blog:post_detail", args=[post_pk])


# post_edit
post_edit = UpdateView.as_view(
    model=Post,
    form_class=PostForm,
    # TODO:가변적으로 URL을 지정할 수 없다.
    # TODO: URL Reverse가 미적용
    # success_url='blog:post_list',  # URL Reverse 미지원
    # success_url=reverse("blog:post_list"),  # 프로젝트가 초기화가 되어야 할 수 있음
    success_url=reverse_lazy("blog:post_list"),
)


# post_delete
post_delete = DeleteView.as_view(
    model=Post,
    success_url=reverse_lazy("blog:post_list"),
)

