from django.shortcuts import render
# from django.shortcuts import redirect
# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from django.views.generic import View
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin
from .forms import TagForm, PostForm
# Create your views here.

def posts_list(request):
    # return HttpResponse('ekekek')
    # n = ['Kek', 'Lol', 'Cheburek']
    # return render(request, 'blog/index.html', context={'names': n})

    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_detail.html', context={'post': post})

class PostDetail(ObjectDetailMixin, View):  # на замену def post_detail(по принципу DRY)
        model = Post
        template = 'blog/post_detail.html'

    # def get(self, request, slug):
        # # post = Post.objects.get(slug__iexact=slug)
        #
        # post = get_object_or_404(Post, slug__iexact=slug)
        # return render(request, 'blog/post_detail.html', context={'post': post})

# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html', context={'tag': tag})

class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create_form.html'

    # def get(self, request):
    #     form = PostForm()
    #     return render(request, 'blog/post_create_form.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = PostForm(request.POST)
    #
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request, 'blog/post_create_form.html', context={'form': bound_form})

class TagDetail(ObjectDetailMixin, View):  # на замену def tag_detail(по принципу DRY)
        model = Tag
        template = 'blog/tag_detail.html'

    # def get(self, request, slug):
        # # tag = Tag.objects.get(slug__iexact=slug)
        #
        # tag = get_object_or_404(Tag, slug__iexact=slug)
        # return render(request, 'blog/tag_detail.html', context={'tag': tag})

class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'

    # def get(self, request):
    #     form = TagForm()
    #     return render(request, 'blog/tag_create.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = TagForm(request.POST)
    #
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         # return redirect('tag_detail_url', slug=new_tag.slug)
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_create.html', context={'form': bound_form})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


