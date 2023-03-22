from django.db import models

# Create your models here.
class Messages(models.Model):
  message = models.CharField(max_length=120)
  
# messages = Messages.objects.raw('SELECT * FROM Messages')
# print(messages)


