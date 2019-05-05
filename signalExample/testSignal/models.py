from django.db import models
from django.db.models.signals import post_save,pre_save

# Create your models here.


class Signal_test(models.Model):
    title = models.CharField(max_length=50)


    def __str__(self):
        return self.title


def test_Save(sender, instance, **kwargs):
    print("we have saved the data")

post_save.connect(test_Save, sender=Signal_test)
