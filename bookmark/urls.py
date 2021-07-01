from django.urls import path
from .views import *



urlpatterns = [
    path('', bookmarkListView.as_view(), name = 'list'),
    path('add/', bookmarkCreateView.as_view(), name = 'add'),
    path('detail/<int:pk>', bookmarkDetailView.as_view(), name ="detail"),
    
]