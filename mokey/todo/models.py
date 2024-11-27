from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=500)
    completed=models.BooleanField(default=False)
    def __str__(self):

        #it will return the title
        return self.title
    
# Create your models here.
class user_data(models.Model):
    user_id=models.CharField(max_length=150)
    email=models.CharField(max_length=500)
    name=models.CharField(max_length=150)
    lname=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    
    def __str__(self):

        #it will return the title
        return self.user_id

class product_data(models.Model):
    product_id=models.CharField(max_length=150)
    product_name=models.CharField(max_length=500)
    product_description=models.CharField(max_length=150)
    quantity=models.CharField(max_length=150)
    price=models.FloatField(max_length=150)
    
    def __str__(self):

        #it will return the title
        return self.product_id
    
class user_cart(models.Model):
    user_id= models.CharField(max_length=150)
    product_id=models.CharField(max_length=150)
    quantity=models.CharField(max_length=150)

    
    def __str__(self):

        #it will return the title
        return self.quantity #dont know what to write