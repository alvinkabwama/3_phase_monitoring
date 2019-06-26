from django.db import models

# Create your models here.


class Client(models.Model):    
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    device_serial = models.CharField(max_length = 255)
    occupation = models.CharField(max_length = 255)
    def __str__(self):
        return self.device_serial
    
  

class Data(models.Model):
    client = models.ForeignKey(Client, blank= True, on_delete=models.CASCADE)
    
    p1vb_meter = models.CharField(max_length = 255)
    p2vb_meter = models.CharField(max_length = 255)
    p3vb_meter = models.CharField(max_length = 255)
    
    p1cb_meter = models.CharField(max_length = 255)
    p2cb_meter = models.CharField(max_length = 255)
    p3cb_meter = models.CharField(max_length = 255)
    
    p1va_meter = models.CharField(max_length = 255)
    p2va_meter = models.CharField(max_length = 255)
    p3va_meter = models.CharField(max_length = 255)
    
    p1ca_meter = models.CharField(max_length = 255)
    p2ca_meter = models.CharField(max_length = 255)
    p3ca_meter = models.CharField(max_length = 255)
    
    received_at = models.DateTimeField(auto_now_add =True)  



