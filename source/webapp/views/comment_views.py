
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView

from webapp.forms import CommentForm
from webapp.models import Comment


class CommentIndexView(TemplateView):
    template_name = 'comment/comment_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all().order_by('created_at').reverse()
        return context

class CommentCreateView(View):
    def get(self, request, *args, **kwargs):
        form = CommentForm()
        return render(request, 'comment/comment_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = CommentForm(data=request.POST)
        if form.is_valid():
            Comment.objects.create(
                article=form.cleaned_data['article'],
                text=form.cleaned_data['text'],
                author=form.cleaned_data['author']
            )
            return redirect('comment_view')
        else:
            return render(request, 'comment/comment_create.html', context={'form': form})



class CommentUpdateView(View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        form = CommentForm(data={
            'author': comment.author,
            'text': comment.text,
            # 'article': comment.article
        })
        return render(request, 'comment/comment_update.html', context={'form': form, 'comment': comment})

    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment.author = form.cleaned_data['author']
            comment.text = form.cleaned_data['text']
            comment.article = form.cleaned_data['article']
            comment.save()
            return redirect('comment_view')
        else:
            return render(request, 'comment/comment_update.html', context={'form': form, 'comment': comment})


class CommentDeleteView(View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        return render(request, 'comment/comment_delete.html', context={'comment': comment})

    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        comment.delete()
        return redirect('comment_view')




