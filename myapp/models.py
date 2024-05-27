from django.db import models

# Create your models here.

class Contact(models.Model):
    name_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    about = models.TextField()
    added_date = models.DateField()

    def __str__(self):                                                                                                                            
        return self.name
    







