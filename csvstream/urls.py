from django.urls import path
from .views import OrderListCreateView,OrderDetailView,LineItemListCreateView,LineItemDetailView
urlpatterns = [
    path('order/', OrderListCreateView.as_view(), name='Order_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='Order_detail'),
    path('line-items/', LineItemListCreateView.as_view(), name='Line_items_list'),
    path('line-items/<int:pk>/', LineItemDetailView.as_view(), name='Line_items_detail'),
]