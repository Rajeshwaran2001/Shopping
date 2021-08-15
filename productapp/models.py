from django.db import models

# Create your models here.
class Category(models.Model):
 cname=models.CharField("Category Name",max_length=20)

 def __str__(self):
     return self.cname

class Product(models.Model):
 pname = models.CharField('Product Name', max_length=30)
 category = models.ForeignKey(Category, blank=True, null=True, on_delete = models.CASCADE)
 price = models.FloatField()
 qty = models.IntegerField()

 def __str__(self):
     return self.pname
