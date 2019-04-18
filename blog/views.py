from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'HericB',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 21,2018'
    },

    {
        'author': 'BaconHamfish',
        'title': 'Blog Post 2',
        'content': 'Fishy Content',
        'date_posted': 'August 29,2018'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
