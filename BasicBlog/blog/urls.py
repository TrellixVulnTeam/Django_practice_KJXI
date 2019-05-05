from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('storypage/', views.storypage_view, name="storypage"),
]
