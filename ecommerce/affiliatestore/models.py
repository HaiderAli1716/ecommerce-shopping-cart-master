from django.db import models

# Create your models here.
class Carousel(models.Model):
    image=models.ImageField(upload_to="core/images", default="")
    link        = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.image)
    
class stores(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,)
    category=models.ForeignKey("categories", on_delete=models.CASCADE,null=True)
    desc = models.CharField(max_length=500, default="")
    about=models.TextField(null=True)
    image=models.ImageField(upload_to="core/images", default="")
    
    def __str__(self):
        return str(self.name)

class categories(models.Model):
    name=models.CharField(max_length=500,null=True)  
    def __str__(self):
        return str(self.name)  

class Offer(models.Model):
    id=models.AutoField(primary_key=True)
    desc=models.CharField(max_length=50,default="")
    code=models.CharField(max_length=50,null=True,blank=True)
    link=models.URLField( max_length=200, default="" )
    image=models.ImageField(upload_to="core/images", default="")
    storename=models.ForeignKey("stores", on_delete=models.CASCADE)
    displayfields=['id','desc','code','link','storename']
    searcfield=['id','desc']
    

    def __str__(self):
        
        
        return str (f'{self.id} {self.storename}')

