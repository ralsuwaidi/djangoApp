from django.db import models

class Writingprompt(models.Model):
    title=models.CharField(max_length=500)
    comment=models.CharField(max_length=10000)
    score=models.IntegerField()
    pub_date = models.DateTimeField('date published')
    url=models.CharField(max_length=100)
    def __str__(self):
        return self.title
