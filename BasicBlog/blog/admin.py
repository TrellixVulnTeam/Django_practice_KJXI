from django.contrib import admin
from .models import index_page_category_data, index_page_repeat_data, story_page_view_blog, story_page_view


# Register your models here.

admin.site.register(index_page_category_data)
admin.site.register(index_page_repeat_data)
admin.site.register(story_page_view)
admin.site.register(story_page_view_blog)