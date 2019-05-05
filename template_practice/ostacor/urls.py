from django.urls import path
from . import views
from django.conf import settings
from  django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('create_story/', views.create_story, name="create_story"),
    path('submit_story/', views.submit_story, name="submit_story"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT +'/story_media/')
