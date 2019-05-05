from django.contrib import admin
from .models import nav_header,homepage_latest_story,homepage_food_locus_story,CreateStory,CreateStory_media

# Register your models here.

admin.site.register(nav_header)
admin.site.register(homepage_latest_story)
admin.site.register(homepage_food_locus_story)
admin.site.register(CreateStory)
admin.site.register(CreateStory_media)