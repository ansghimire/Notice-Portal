from rest_framework import serializers
from .models import Category,Notice, Advertisement


class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields = '__all__'
        read_only_fields = ['id']



class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice

        fields = ['id', 'title', 'description', 'description2', 'cateogry', 'thumbnail', 'slug', 'exprity_date', 'file', 'created_at']
        read_only_fields = ['id', 'slug']
    

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method == "GET":
            fields['cateogry'] = CategorySerializer()
        return fields



class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['ads_image', 'ads_type', 'id']
        read_only_fields = ['id']