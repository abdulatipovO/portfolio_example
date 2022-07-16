from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog', BlogView.as_view(), name='blog'),
    path('subcribe_index', SubribeView.as_view(), name='subcribe_index')
]