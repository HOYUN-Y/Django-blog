from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import unicodedata
import uuid
import os


def upload_to_path(instance, filename):
    ext = filename.split('.')[-1]
    base = unicodedata.normalize('NFKD', instance.title).encode('ascii','ignore').decode('ascii')
    base = base.replace(' ','_') or 'file'
    new_filename = f"{base}_{uuid.uuid4().hex[:8]}.{ext}"
    return f"documents/{instance.doc_type}/{new_filename}"


# Create your models here.
class Posts(models.Model):
    POST_TYPES = (
        ('blog','BLOG'),
        ('portfolio','PORTFOLIO')
    )
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True, null=True)
    type = models.CharField(max_length=20, choices=POST_TYPES, default='blog')
    image = models.ImageField(upload_to='', blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    reference_url = models.URLField(blank=True, null= True)
    github_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Statements(models.Model):
    STATEMENT_TYPE =(
        ('public','PUBLIC'),
        ('corporation','CORPORATION')
    )
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    content = RichTextUploadingField(blank=True, null=True)
    type = models.CharField(max_length=20, choices=STATEMENT_TYPE, default='public')
    corp_name = models.CharField(max_length=100, default='public', blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class GuestbookEntry(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} : {self.created_at.strftime('%Y-%m-%d %H:%M')}"



#######

    
class Document(models.Model):
    DOCUMENT_TYPE_CHOICES = (
        ('resume','RESUME'),
        ('project', 'PROJECT'),
        ('certification','CERTIFICATION'),
        ('etc','ETC'),
    )

    title = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=100, choices=DOCUMENT_TYPE_CHOICES, default='etc')
    file = models.FileField(upload_to=upload_to_path)
    original_filename = models.CharField(max_length=255, blank=True)
    uploaded_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.file and not self.original_filename:
            self.original_filename = self.file.name
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


