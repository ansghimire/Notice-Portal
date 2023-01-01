from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Notice
from django.template.defaultfilters import slugify
import random 
import string


def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size)) 



@receiver(pre_save, sender = Notice)
def create_news(sender, instance, **kwargs):
       slug_exists =  Notice.objects.filter(slug = slugify(instance.title)).exists()
       
       if slug_exists:
        instance.slug = instance.title + '-' +random_string_generator(size=10)

       else:
        instance.slug = slugify(instance.title) 
    