from django.urls import path
from. import views
urlpatterns = [
    path('order', views.Order_list, name='Order_list'),
    path('orders/<int:pk>/', views.Order_detail, name='Order_detail'),
    path('line-items/', views.line_item_list, name='Line_items_list'),
    path('line-items/<int:pk>/', views.line_item_detail, name='Line_items_detail'),
]