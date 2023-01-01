from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    description2 = models.TextField()
    cateogry = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="thumbnails/")
    slug = models.SlugField(max_length=240, unique=True) 
    exprity_date = models.DateTimeField()
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

    

    