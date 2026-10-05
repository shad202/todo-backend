from django.db import models

# Create your models here.
class Task(models.Model): # define a new dataset table called task 
    text = models.CharField(max_length=255)
    category = models.CharField(max_length=100, default='Uncategorized')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
