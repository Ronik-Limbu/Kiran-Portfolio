from django.db import models

# Create your models here.
class Video(models.Model):
    embed_url = models.URLField(max_length=200)
    link = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.description

class Article(models.Model):
    title = models.CharField(max_length=200,null=True)
    description = models.TextField()  # Add this line
    Heading = models.CharField(max_length=200,default='Heading',null=True)
    newspaper_name = models.CharField(max_length=200,null=True)
    newspaper_email = models.CharField(max_length=200,null=True)
    first_para = models.TextField(null=True)
    second_para = models.TextField(null=True)
    third_para = models.TextField(null=True)
    fourth_para = models.TextField(null=True)
    image = models.ImageField(upload_to='articles/images/',null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name