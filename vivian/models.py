from django.db import models

class Writingprompt(models.Model):
    title=models.CharField(max_length=500)
    comment=models.CharField(max_length=10000)
    score=models.IntegerField()
<<<<<<< HEAD
    pub_date = models.DateTimeField('date published')
=======
>>>>>>> b6a1f70d0fb60e7eeee3ed739e3ac89a12228be2
    def __str__(self):
        return self.title
