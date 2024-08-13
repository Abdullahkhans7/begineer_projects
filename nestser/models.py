from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(default=60)

    def __str__(self) :
        return self.name


class Book(models.Model):
    title=models.CharField(max_length=100)
    Author=models.ForeignKey(Author,on_delete=models.CASCADE)
    publish_date=models.DateField()


    def __str__(self):
        return self.title