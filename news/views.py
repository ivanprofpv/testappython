from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

class NewDetailsView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewUpdateView(UpdateView):
    model = Articles
    template_name = 'news/update.html'

    form_class = ArticlesForm

class NewDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/delete.html'

def news_home(request):
    news = Articles.objects.order_by('-date')[:5]
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'В форме допущены ошибки'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
