from django.db import models
import uuid

# Create your models here.

class Store(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    productName = models.CharField(max_length=100 , null=False)
    price = models.IntegerField(null=False)
    description = models.CharField(max_length=100 ,null= True)
    clubName = models.CharField(max_length=100 ,null=False)
    payment = models.CharField(max_length=100 ,null=False)

    def __str__(self):
        return self.productName
        
class ProductImage(models.Model):
    product = models.ForeignKey(Store, on_delete=models.CASCADE)
    imageUrl1 = models.URLField("image Url1", null=True,max_length=255, blank=False)
    imageUrl2 = models.URLField("image Url2", null=True,max_length=255, blank=False)

    def __str__(self):
        return f'{self.product}\'s image'