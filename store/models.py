from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField

class University(models.Model):
	name = models.Charfield(max_length = 900)
	slug = models.SlugField(max_length = 900, default="slug-field", unique= True)

class Category(models.Model):
	name = models.Charfield(max_length = 900)
	slug = models.SlugField(max_length = 900, default="slug-field", unique= True)

class BookName(models.Model):
	user = models.ForeignKey()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	university = models.ForeignKey(University, on_delete = models.CASCADE)
	name = models.Charfield(max_length=900)
	author = models.Charfield(max_length=255)
	description = RichTextUploadingField()
	cover = ProcessedImageField(upload_to = '/cover/',format='JPEG',options={'quality': 60}, null = True, blank=False)
	file = models.FileField(upload_to = '/file/', null = True, blank=False)
	created_on = models.DateTimeField(auto_now_add = True)