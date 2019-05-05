from django.db import models

class index_page_category_data(models.Model):
    category_name = models.CharField(max_length=200)
    story_base_image_name = models.CharField( max_length=50, null=True, blank=True)
    story_base_image = models.CharField(max_length=400)
    story_heading = models.TextField(max_length = 500, default = None)
    story_writter_name = models.CharField(max_length=100)
    story_publish_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    

    def __str__(self):
        return self.story_heading


class index_page_repeat_data(models.Model):
    story_base_image = models.CharField(max_length=400)
    story_base_image_name = models.CharField( max_length=50, null=True, blank=True    )
    story_heading = models.TextField(max_length = 500, default = None)
    story_writter_name = models.CharField(max_length=100)
    story_publish_date = models.DateTimeField(auto_now=False, auto_now_add=False)


    def __str__(self):
        return self.story_heading


class story_page_view(models.Model):
    story_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=200)
    story_base_image = models.CharField(max_length=400)
    story_base_image_name = models.CharField(max_length=50, null=True, blank=True)
    story_heading = models.TextField(max_length = 500, default = None)
    story_writter_name = models.CharField(max_length=100)
    story_publish_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.story_id)


class story_page_view_blog(models.Model):
    story_id = models.ForeignKey(story_page_view, on_delete=models.CASCADE)
    desc_story_img_seq = models.IntegerField(default=1 , unique=True)
    desc_story_img = models.CharField(max_length=200)
    desc_story_img_name = models.CharField(max_length=50)
    desc_story_img_title = models.CharField(max_length=100)
    desc_story_img_content = models.TextField(max_length=1500)

    def __str__(self):
        s = 'storyId_'+ str(self.story_id)+'_' + str(self.desc_story_img_title)+ '_' +'imgNo_' + str(self.desc_story_img_seq)
        return s
    

