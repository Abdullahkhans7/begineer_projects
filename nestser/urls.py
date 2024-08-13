from django.urls import path
from.views import *
urlpatterns = [
     path('book/',Booklistview.as_view(),name='book-list'),
 ]
 