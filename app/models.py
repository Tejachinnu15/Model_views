from django.db import models

# Create your models here.
class Top(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name
class Webpages(models.Model):
    topic_name=models.ForeignKey(Top,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    def __str__(self):
         return self.name
  
class AcessRecords(models.Model):
    name=models.ForeignKey(Webpages,on_delete=models.CASCADE)
    date=models.DateField()
    authors=models.CharField(max_length=100)
    def __str__(self):
         return self.authors
    def __str__(self):
        return self.date
