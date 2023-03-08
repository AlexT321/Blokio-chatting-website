from django.db import models

# Create your models here.
class Messages(models.Model):
  message = models.CharField(max_length=120)

  def __str_(self):
    return f"Messages for {self.message}"