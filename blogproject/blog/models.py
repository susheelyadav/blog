from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.caption}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    Excerpt = models.TextField()
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="",unique=True,db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,related_name="post",null=True)
    tag = models.ManyToManyField(Tag,related_name="post")

    def save(self,*args, **kwargs):
        self.slug =slugify(self.title)
        super(Post,self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}-{self.author}{self.date}"
    
    class Meta:
        verbose_name_plural = "POSTS"
        
    
    
    

