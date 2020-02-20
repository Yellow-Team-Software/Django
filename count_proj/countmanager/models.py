from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Speaker(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Session(models.Model):
    name = models.CharField(max_length=30)
    speaker =models.ForeignKey(Speaker,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)


    count_start=models.IntegerField(default=0)
    count_mid=models.IntegerField(default=0)
    count_end=models.IntegerField(default=0)
    def __str__(self):
        return self.name + "\n by: " + self.speaker.name + "\n in room: "+ self.room.name

class TimeSlot(models.Model):
    start_time=models.IntegerField(default=0)
    duration=models.IntegerField(default=0)
   