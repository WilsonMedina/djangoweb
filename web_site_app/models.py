from django.db import models
from ckeditor.fields import RichTextField 

#-------------------------------------About-----------------------------------------------#
class About(models.Model):
    first_name = models.CharField('First name', max_length=50, null=False, blank=False)
    last_name = models.CharField('Last name', max_length=50, null=False, blank=False)
    profession = models.CharField('Profession', max_length=150, null=False, blank=False)
    content = RichTextField('Content', null=False, blank=False)
    state = models.BooleanField('State', default=True)
    created = models.DateTimeField('Created',auto_now_add=True) 
    updated = models.DateTimeField('Updated',auto_now=True) 

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
        db_table = 'About'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
  
#-------------------------------------RRSS-----------------------------------------------#   
class RrSs(models.Model):
    name = models.CharField('Name RRSS', max_length=50, null=False, blank=False)
    url = models.URLField('URL RRSS', max_length=150, null=False, blank=False)
    icon = models.CharField('Icon RRSS', max_length=100, null=False, blank=False)
    state = models.BooleanField('State', default=True)
    created = models.DateTimeField('Created',auto_now_add=True) 
    updated = models.DateTimeField('Updated',auto_now=True) 

    class Meta:
        verbose_name = 'RRSS'
        verbose_name_plural = 'RRSS'
        db_table = 'RRSS'

    def __str__(self):
        return f'{self.name}'

#-------------------------------------Experience-----------------------------------------------#   
class Experience(models.Model):
    position = models.CharField('Position', max_length=50, null=False, blank=False)
    company = models.CharField('Company', max_length=50, null=False, blank=False)
    period = models.CharField('Period', max_length=50, null=False, blank=False)
    description = RichTextField('Description', null=True, blank=True)
    state = models.BooleanField('State', default=True)
    created = models.DateTimeField('Created',auto_now_add=True) 
    updated = models.DateTimeField('Updated',auto_now=True) 

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experience'
        db_table = 'Experience'
        ordering = ['-id']

    def __str__(self):
        return f'{self.position}'
