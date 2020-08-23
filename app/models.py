from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.models import User
import sys

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to="category/",blank=True)

    def __str__(self):
        return self.name
    

UNITS_CHOICE = (
    ('kg','kg'),
    ('gm','gm'),
    ('l','l'),
    ('ml','ml'),
    ('unit','unit'),
)

class Product(models.Model):
    name = models.CharField(max_length=80)
    mrp = models.FloatField()
    list_price = models.FloatField()
    discount = models.FloatField()
    qty = models.IntegerField()
    moq = models.IntegerField(default=1,blank=True)
    units = models.CharField(max_length=20,choices=UNITS_CHOICE)
    inactive = models.BooleanField(default=True,blank=True)
    instock = models.BooleanField(default=False,blank=True)
    sort_desc = models.TextField(null=True,blank=True)
    long_desc = models.TextField(null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class ProductImages(models.Model):
    large_image = models.ImageField(upload_to='product/large',null=True,blank=True)
    normal_image = models.ImageField(upload_to='product/normal',null=True,blank=True)
    thumbnail_image = models.ImageField(upload_to='product/thumbnail',null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return self.product.name

    def save(self,force_insert=False,force_update=False, using=None):
        im = Image.open(self.large_image)
        output = BytesIO()
        if im.size[0]<=700:
            basewidth = im.size[0]
        else:
            basewidth = 600

        wpercent = (basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent)))
        im = im.resize((basewidth,hsize), Image.ANTIALIAS)
        im = im.convert("RGB")
        self.height = im.height
        self.width = im.width
        im.save(output, format='JPEG', quality=70)
        self.normal_image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.large_image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        if im.size[0]<=100:
            basewidth = im.size[0]
        else:
            basewidth = 100
        wpercent = (basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent)))
        imc = im.resize((basewidth,hsize), Image.ANTIALIAS)
        imc = imc.convert("RGB")
        output = BytesIO()
        imc.save(output, format='JPEG', quality=70)
        output.seek(0)
        self.thumbnail_image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.large_image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super(ProductImages,self).save()
    
