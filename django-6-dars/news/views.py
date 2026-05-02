from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import News
from .forms import CommentForm


def news_list(request):
    news_list = News.objects.order_by('-pk')
    return render(request, 'news/news_list.html', {'news_list': news_list})


def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    comments = news.news_comments.all()

    if request.method == 'POST':
        if 'like' in request.POST:
            news.likes += 1
            news.save()
            messages.success(request, 'Like qo\'shildi!')
            return redirect('news:news_detail', pk=pk)
        elif 'comment' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.news = news
                comment.save()
                news.comments += 1
                news.save()
                messages.success(request, 'Izoh qo\'shildi!')
                return redirect('news:news_detail', pk=pk)
        else:
            form = CommentForm()
    else:
        form = CommentForm()

    return render(request, 'news/news_detail.html', {
        'news': news,
        'comments': comments,
        'form': form
    })
