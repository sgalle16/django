from django.shortcuts import render
from django.views.generic import View
from .models import News

# Create your views here.


class NewsView(View):
    def get(self, request, *args, **kwargs):
        newss = News.objects.all().order_by('-date')
        context = {
            'newss': newss
        }
        return render(request, 'news.html', context)
