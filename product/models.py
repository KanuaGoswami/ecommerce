from django.db import models
import uuid 
from autoslug import AutoSlugField
# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    class Meta:
        abstract =True


class Category(BaseModel):
    # slug = models.SlugField(unique=True,blank=True,null=True,default='')
    Cname = models.CharField(max_length=100,unique=True,)

    slug = AutoSlugField(populate_from='Cname',unique=True,)
    cimage = models.ImageField(upload_to='upload')

class ProductColor(BaseModel):
    # product = models.ForeignKey(Product,on_delete=models.CASCADE)
    color = models.CharField(max_length=100,unique=True)

class ProductSize(BaseModel):
    # product = models.ForeignKey(Product,on_delete=models.CASCADE)
    size = models.CharField(max_length=100,unique=True)

class Product(BaseModel):
    # slug = models.SlugField(unique=True,blank=True,null=True)
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    
    Pname = models.CharField(max_length=100,unique=True)
    slug = AutoSlugField(populate_from='Pname',unique=True)    
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity =models.IntegerField()
    color_variant = models.ManyToManyField(ProductColor)
    size_variant = models.ManyToManyField(ProductSize) 

 
class ProductImage(BaseModel):
    # id = models.UUIDField(primary_key=True,editable=False,default=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload')





    
