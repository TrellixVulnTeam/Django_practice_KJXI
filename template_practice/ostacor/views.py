from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404, render, redirect
from .models import nav_header, homepage_latest_story, homepage_food_locus_story,CreateStory, CreateStory_media
# Create your views here.

def index(request):
    page = nav_header.objects.all()
    one_title = homepage_latest_story.objects.all()
    food_locus_one_title = homepage_food_locus_story.objects.all()
    context = {'page' : page,
                'one_title' : one_title,
                'food_locus_one_title': food_locus_one_title}
    return render(request, 'ostacor/index.html/' , context)


def create_story(request):
    return render(request, 'ostacor/create_story.html')


def submit_story(request):
    Story_Tilte = request.POST['Story_Tilte']
    Story_One_liner = request.POST['Story_One_liner']
    createStory_data = CreateStory(story_title=Story_Tilte , story_one_liner = Story_One_liner)
     
    video_file = request.POST.get('video_file', False)
    video_heading = request.POST.get('video_heading', False)
    image_file = request.POST.get('image_file', False)
    image_heading = request.POST.get('image_heading', False)
    text_desc = request.POST.get('text_desc', False)
    text_desc_heading = request.POST.get('text_desc_heading', False)
    media_position = request.POST.get('media_position', False)

    createStory_data.save()
    create_story_media = CreateStory_media(story_no= createStory_data, video_file=video_file, video_heading=video_heading, image_file=image_file, image_heading=image_heading, text_desc=text_desc, text_desc_heading=text_desc_heading, media_position=media_position)
    create_story_media.save()

    print('data loaded')
    return render(request, 'ostacor/create_story.html')

