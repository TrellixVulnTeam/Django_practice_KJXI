from django.shortcuts import render
from .models import CreateStoryHeader

# Create your views here.

def create_story_header_view(request):
	if request.method == 'POST':
		title = request.POST.get('Story_Tilte')
		One_liner = request.POST.get('Story_One_liner')
		CreateStoryHeader.objects.create(title = title , one_liner= One_liner)
	context={}
	
	return render(request, 'BlogAdminApp/CreateStoryHeader.html', context)
