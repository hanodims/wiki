from django.shortcuts import render
from pages.models import Page

# Create your views here.


def Page_list(request):
    context = {
        "pages":Page.objects.all(),
    }
    return render(request, 'list.html', context)


def Page_detail(request, page_id):
    context = {
        "Page":Page.objects.get(id=page_id),
    }
    return render(request, 'detail.html', context)