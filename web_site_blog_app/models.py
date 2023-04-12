from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

#-------------------------------------Profile-----------------------------------------------#
class ProfileAuthor(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField('Image', upload_to='img_author', default='default_author.jpg')
    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)

    class Meta:
        verbose_name = 'ProfileAuthor'
        verbose_name_plural = 'ProfileAuthors'
        db_table = 'ProfileAuthors'

    def __str__(self):
        return f'Author {self.author.username}'

#-----------------------------------Category-----------------------------------------------#    
class Category(models.Model):
    name = models.CharField('Name', max_length=50, null=False, blank=False, unique=True)
    state = models.BooleanField('State', default=True)
    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'Categories'

    def __str__(self):
        return f'Category {self.name}'

#--------------------------------------Posts-----------------------------------------------#  
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    title = models.CharField('Title', max_length=20, null=False, blank=False) 
    excerpt = models.CharField('Excerpt', max_length=100, null=False, blank=False)
    image = models.ImageField('Image', upload_to='img_post', default='default_post.png', null=False, blank=False)
    content = RichTextField('Content',null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.BooleanField('State', default=False)
    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'Posts'
        ordering = ['-timestamp']

    def __str__(self):
        return F'{self.title}'

