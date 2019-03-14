from django.shortcuts import render
from .models import Auction

# Create your views here.

# Dummy Data
posts = [
    {
        'author': 'PyCharm',
        'title': 'Django',
        'content': 'Django is the award-winning leader of Python web frameworks and PyCharm has long supported it. '
                   'Running, debugging, navigating, working productively... PyCharm has you covered for Django.',
        'date_posted': 'January 4, 2019'
    },
    {
        'author': 'PyCharm',
        'title': 'Flask',
        'content': 'The fast-growing Flask microframework has strong and growing PyCharm support: templates, '
                   'navigation, completion, and more.',
        'date_posted': 'January 5, 2019'
    }
]


def home(request):
    context = {
        'auctions': Auction.objects.all()
    }
    return render(request, 'auction/home.html', context)


def about(request):
    return render(request, 'auction/about.html')
