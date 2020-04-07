from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Post


@receiver(post_delete,sender=Post)
def delete_post(sender,instance,**kwargs):
    print(f"{instance.title} by {instance.author} is deleted")
