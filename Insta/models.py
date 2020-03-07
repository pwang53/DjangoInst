from django.db import models
from imagekit.models import ProcessedImageField  # 第三方库：django-image
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 有不会的就谷歌Django官方文档: google Django Model Fields
# https://docs.djangoproject.com/en/3.0/ref/models/fields/

# 定义一个model

class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        # 当有人上传一个图片时，存到服务器哪个路径
        upload_to='static/images/posts',
        # 希望图片格式是
        format='JPEG',
        # 图片质量为100
        options={'quality': 100},
        # 允许图片是空白的
        blank=True,
        # 允许null图片存在
        null=True
    )

    # 这个方法是重定位到一个网页
    def get_absolute_url(self):

        return reverse('post_detail', args=[self.id])

class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )
