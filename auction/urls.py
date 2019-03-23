from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuctionListView.as_view(), name='auction-home'),
    path('user/<str:username>', views.UserAuctionListView.as_view(), name='user-auctions'),
    path('auctions/<int:pk>/', views.AuctionDetailView.as_view(), name='auction-detail'),
    path('auctions/new/', views.AuctionCreateView.as_view(), name='auction-create'),
    path('auctions/<int:pk>/update/', views.AuctionUpdateView.as_view(), name='auction-update'),
    path('auctions/<int:pk>/delete/', views.AuctionDeleteView.as_view(), name='auction-delete'),
    path('about/', views.about, name='auction-about'),
]
