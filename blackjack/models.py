from django.db import models

# Create your models here.

class BJ_history(models.Model):
    game_name = models.CharField(max_length=100)
    time = models.DateTimeField('date')
    Choices=[
    ('hit','Hit'),
    ('stand','Stand'),
    ('double','Double'),
    ('insurrance','Insurrance'),
    ('split','Split')

    ]
    choice=models.CharField(choices=Choices,max_length=10)
