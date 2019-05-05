from django.db import models

# Create your models here.
class nav_header(models.Model):
    head_menu_name = models.CharField(max_length=50, blank=True, null=True)
    page_name = models.CharField(max_length=50)
    sep = models.CharField(max_length = 4, blank=True, null=True)


    def __str__(self):
        return self.head_menu_name


class homepage_latest_story(models.Model):
    one_title = models.CharField(max_length=75)
    cover_img_src = models.CharField(max_length=100)
    one_liner_desc = models.CharField(max_length= 300)
    

    def __str__(self):
        return self.one_title
      
class homepage_food_locus_story(models.Model):
    one_title = models.CharField(max_length=75)
    cover_img_src= models.CharField(max_length=100)
    one_liner = models.CharField(max_length= 300)

    def __str__(self):
        return self.one_title

class CreateStory(models.Model):
    story_number = models.AutoField(primary_key = True)
    story_title = models.CharField(max_length = 100)
    story_one_liner = models.CharField(max_length = 250)

    def __str__(self):
        return  self.story_title

class CreateStory_media(models.Model):
    BLANK = 'BLANK'
    IMAGE = 'IMAGE'
    TEXT = 'TEXT'
    VIDEO = 'VIDEO'
    var_media_type = (
        (BLANK,'BLANK'),(IMAGE,'IMAGE'), (TEXT,'TEXT'), (VIDEO,'VIDEO')
        )
    story_no = models.ForeignKey(CreateStory, on_delete=models.CASCADE)
    # media_type = models.CharField(max_length=10, choices=var_media_type, default=BLANK)
    video_file = models.FileField(blank=True, null=True)
    video_heading = models.CharField(max_length = 200)
    image_file = models.ImageField(upload_to = 'story_media' , null=True )
    image_heading = models.CharField(max_length = 200)
    text_desc = models.CharField(max_length=5000, null=True)
    text_desc_heading = models.CharField(max_length=200)
    media_position= models.IntegerField()
    
    def __str__(self):
        return  str(self.story_no)