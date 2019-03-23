from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Auction
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

def home(request):
    context = {
        'auctions': Auction.objects.all()
    }
    return render(request, 'auction/home.html', context)


class AuctionListView(ListView):
    model = Auction
    # Default Template path
    # <app> / <model>_<viewtype>.html
    template_name = 'auction/home.html'
    context_object_name = 'auctions'
    ordering = ['-date_posted']


class UserAuctionListView(ListView):
    model = Auction
    # Default Template path
    # <app> / <model>_<viewtype>.html
    template_name = 'auction/user_auctions.html'
    context_object_name = 'auctions'
    ordering = ['-date_posted']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Auction.objects.filter(vendor=user).order_by()


class AuctionDetailView(DetailView):
    model = Auction
    # Default Template path
    # <app> / <model>_<viewtype>.html
    ordering = ['-date_posted']


class AuctionCreateView(LoginRequiredMixin, CreateView):
    model = Auction
    fields = ['name', 'description', 'image', 'bid_min_value', 'bid_start_date', 'bid_end_date']

    def form_valid(self, form):
        form.instance.vendor = self.request.user
        return super().form_valid(form)


class AuctionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Auction
    fields = ['name', 'description', 'image', 'bid_min_value', 'bid_start_date', 'bid_end_date']

    def form_valid(self, form):
        form.instance.vendor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        auction = self.get_object()
        if self.request.user == auction.vendor:
            return True
        else:
            return False


class AuctionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Auction
    success_url = '/'

    def test_func(self):
        auction = self.get_object()
        if self.request.user == auction.vendor:
            return True
        else:
            return False


def about(request):
    return render(request, 'auction/about.html')
