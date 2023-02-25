from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length = 250, null = True, blank = True) 

    def __str__(self):
        return self.category_name
    
    def save(self, *args, **kwargs):
        original_slug = slugify(self.category_name)
        queryset = Category.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while queryset:
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = Category.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

    
        return super().save(*args, **kwargs)


class Notice(models.Model):
    title = models.CharField(max_length=200)
    nepali_title = models.CharField(max_length=200)
    description = models.TextField()
    description2 = models.TextField(null=True, blank=True)
    cateogry = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="thumbnails/")
    slug = models.SlugField(max_length=240, unique=True) 
    exprity_date = models.DateTimeField(null=True, blank=True)
    file = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class AdvertisementTypes(models.TextChoices):
    VERTICAL = 'vertical',
    HORIZONTAL = 'horizontal',
    SQUARE = 'square',


class Advertisement(models.Model):
    ads_image = models.ImageField(upload_to="ads-image/")
    ads_type = models.CharField(max_length = 20, choices=AdvertisementTypes.choices, default=AdvertisementTypes.VERTICAL)

    

    