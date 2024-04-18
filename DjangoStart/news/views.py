from django.shortcuts import render, redirect
from .models import News_table
from .forms import News_tableForm
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView


# Create your views here.
def news(request):
    news = News_table.objects.order_by('-date')
    return render(request, 'news/news.html', {'news': news})


class NewsDetailView(DetailView):
    model = News_table
    template_name = 'news/detalis_view.html'
    context_object_name = 'post'


class NewsUpdateView(UpdateView):
    model = News_table
    template_name = 'news/detalis_view.html'
    # form_class = News_tableForm
    fields = ['title', 'anons', 'full_text', 'date']

def create(request):
    error = ''
    if request.method == 'POST':
        form = News_tableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Форма была неверной'
    form = News_tableForm()


    data = {'form': form, 'error': error}
    return render(request, 'news/create.html', data)