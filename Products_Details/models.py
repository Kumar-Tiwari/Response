from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MaxValueValidator,MinValueValidator

class Add_Feature(models.Model):
    title=models.CharField(max_length=20)
    price=models.IntegerField()

    def __str__(self):
        return self.title

class Add_category(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(null=True, blank=True,unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Add_category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('categories', kwargs={'slug': self.slug})
    
class Destination(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image1=models.ImageField(upload_to='product_image',default='default.jpg')
    image2=models.ImageField(upload_to='product_image',default='default.jpg')
    image3 = models.ImageField(upload_to='product_image',default='default.jpg')
    feature_image=models.ImageField(upload_to='product_image',null=True,blank=True)
    other_details=models.TextField(null=True,blank=True)
    number_of_people=models.IntegerField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    guide=models.BooleanField(default=True)
    categories=models.ManyToManyField(Add_category, null=True, blank=True)
    additional_feature=models.ManyToManyField(Add_Feature,null=True,blank=True)
    slug=models.SlugField(null=True,blank=True,unique=True)
    ratings=models.IntegerField(null=True,default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)]
        )

    def save(self, *args,**kwargs):
        self.slug=slugify(self.title)
        super(Destination,self).save(*args,**kwargs)
    

    def get_absolute_url(self):
        return reverse('detail_view', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title

