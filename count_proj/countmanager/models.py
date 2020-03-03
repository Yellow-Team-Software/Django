from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=30)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Speaker(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=30)


    def __str__(self):
        return self.first_name + self.last_name



class TimeSlot(models.Model):
    start_time=models.IntegerField(default=0)
    end_time=models.IntegerField(default=0)
    duration=models.IntegerField(default=0)

class Session(models.Model):
    name = models.CharField(max_length=30)
    speaker =models.ForeignKey(Speaker,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "\n by: " + self.speaker.__str__() + "\n in room: "+ self.room.__str__()
   