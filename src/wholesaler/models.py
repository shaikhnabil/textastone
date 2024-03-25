from django.db import models
from django.utils import timezone 
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=25, unique=True)
    phone_no = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


class UserMerchent(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    merchent_id = models.ForeignKey(CustomUser,related_name = 'merchent',on_delete = models.CASCADE)
   
class Saree(models.Model):
    saree_name = models.CharField(max_length = 100)
    sample_image = models.ImageField(upload_to='saree_images/',blank=True)
    material = models.CharField(max_length = 100)
    design_no = models.IntegerField(default = 1)

class Saree_Date_Price(models.Model):
    saree = models.ForeignKey(Saree,on_delete=models.CASCADE)
    price = models.IntegerField()
    date = models.DateTimeField(default = timezone.now)


class Distributor_record(models.Model):
    saree = models.ForeignKey(Saree,on_delete=models.CASCADE)
    who_work =  models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    who_provide =  models.ForeignKey(CustomUser,related_name = 'provider',on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    comission = models.IntegerField(default=0,validators=[MaxValueValidator(500)])
    received_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(default=timezone.now)
    deadline_date =  models.DateTimeField(default=timezone.now)



# class WholesalerSaree(models.Model):

#     wholesaler_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
#     saree_id = models.ForeignKey(Saree,on_delete = models.CASCADE)
#     commission_per_saree = models.IntegerField()
#     sale_price = models.IntegerField()
#     quantity = models.IntegerField()
#     total_commission = models.IntegerField()
#     total_sale_price = models.IntegerField()
#     net_total = models.IntegerField()
#     received_date = models.DateTimeField(default=timezone.now)
#     return_date = models.DateTimeField(default=timezone.now)
#     deadline_date =  models.DateTimeField(default=timezone.now)
#     merchent_id = models.IntegerField(default=None)


# class RetailerSaree(models.Model):

#     retailer_id = models.ForeignKey(CustomUser,default = 0 ,on_delete=models.CASCADE)
#     wholesaler_id = models.ForeignKey(CustomUser,default = 0 ,on_delete=models.CASCADE)
#     saree_id = models.ForeignKey(Saree,on_delete = models.CASCADE)
#     price = models.IntegerField()
#     commission_per_saree = models.IntegerField()
#     sale_price = models.IntegerField()
#     quantity = models.IntegerField()
#     total_commission = models.IntegerField()
#     total_sale_price = models.IntegerField()
#     net_total = models.IntegerField()
#     received_date = models.DateTimeField(default=timezone.now)
#     return_date = models.DateTimeField(default=timezone.now)
#     deadline_date =  models.DateTimeField(default=timezone.now)
#     wholesaler_id = models.IntegerField(default = None)

# class CustomerRecords(models.Model):

#     saree_id = models.ForeignKey(Saree,on_delete = models.CASCADE)
#     retailer_id = models.IntegerField(default = 0)
#     wholesaler_id = models.IntegerField(default = None)
#     price = models.IntegerField()
#     quantity = models.IntegerField()
#     total = models.IntegerField()
#     received_date = models.DateTimeField(default=timezone.now)
#     return_date = models.DateTimeField(default=timezone.now)
#     deadline_date =  models.DateTimeField(default=timezone.now)


    