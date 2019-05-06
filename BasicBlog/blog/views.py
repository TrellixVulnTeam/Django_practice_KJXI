from django.shortcuts import render , get_object_or_404
from .models import index_page_recent_stories_data,index_page_category_data , index_page_repeat_data, story_page_view,story_page_view_blog

def index_recent_story_view(request , **kwargs):
    entertainment_category= index_page_category_data.objects.all().filter(category_name='Entertainment')


    stories = index_page_recent_stories_data.objects.order_by('story_publish_date').all()
    if len(stories) != 0:
        recent_stories = index_page_recent_stories_data.objects.order_by('story_publish_date').reverse()[:3]
    else:
        recent_stories=None

    context ={
        'recent_stories' : recent_stories,
        'stories' : stories,
        'entertainment_category':entertainment_category
    }

    return render(request, 'blog/index.html',context)



def storypage_view(request, **kwargs):
    data  = story_page_view_blog.objects.all()
    print(data)
    context = {
    'data':data
    }
    return render(request, 'blog/storypage.html', context)
