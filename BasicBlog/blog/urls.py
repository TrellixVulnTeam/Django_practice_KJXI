from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index_recent_story_view, name='index_recent_story_view'),
    path('<int:entertainment_category[0].id>/', views.storypage_view, name="storypage"),
]
