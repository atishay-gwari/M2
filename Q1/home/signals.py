from django.db.models.signals import post_save,post_delete
from .models import *
from django.dispatch import receiver

@receiver(post_save,sender=Profile)
def autoGenrateData(sender,instance,created,**kwargs):
    if created:
        projectdata=instance
        # print(projectdata.name)
        # print(projectdata.techStack)
        # print(projectdata.description)
        # print(projectdata.link)
        Data.objects.create(
            name=projectdata.name
        )
        print("created")

@receiver(post_delete,sender=Profile)
def autoGenrateDataGone(sender,instance,**kwargs):
    projectdata=instance
    fetchdata=Data.objects.get(name=projectdata.name)
    fetchdata.delete()
