from django.db import models
from datetime import datetime

class CalvinTbl(models.Model):
    title = models.CharField(max_length=100)
    cnhImg = models.ImageField(upload_to='images/')
    cnhImgUrl = models.URLField()
    published_date = models.DateField(default=datetime.today().strftime("%Y-%m-%d"))

    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = 'published_date'
