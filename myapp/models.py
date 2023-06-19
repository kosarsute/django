from django.db import models 

class Logger(models.Model): 
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text= "Enter the exact time!")

class Booking(models.Model): 
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)

class Employees(models.Model): 
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name



