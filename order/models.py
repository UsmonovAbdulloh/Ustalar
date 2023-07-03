from django.db import models

# Create your models here.
class UstaModel(models.Model):
    name = models.CharField(max_length=65, default='')
    fname = models.CharField(max_length=65, default='')
    phone_number = models.CharField(max_length=15,default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'usta'


class ClientModel(models.Model):
    client_name = models.CharField(max_length=50, default='')
    client_phonenumber = models.CharField(max_length=15, default='')
    client_location = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'client'

class OrderModel(models.Model):
    order = models.ForeignKey(ClientModel,on_delete=models.SET_NULL,null=True)
    client_problem = models.TextField(default='')
    price = models.TextField(default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'order'
