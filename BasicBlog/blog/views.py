from django.shortcuts import render , get_object_or_404
from .models import index_page_category_data , index_page_repeat_data

def index_view(request , **kwargs):
    stories = index_page_category_data.objects.order_by('story_publish_date').all()
    recent_stories = index_page_category_data.objects.order_by('story_publish_date').reverse()[:3]
    
    context ={
        'recent_stories' : recent_stories,
        'stories'  : stories 
    }
    return render(request, 'blog/index.html',context)


def storypage_view(request, **kwargs):
    return render(request, 'blog/storypage.html', {})