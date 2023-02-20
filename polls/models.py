from django.db import models

class Izdelie(models.Model):
    name = models.CharField(max_length=50)

    objects = models.Manager

    def __str__(self):
        return self.name

class Detal(models.Model):
    name = models.CharField(max_length=50)
    izdelie = models.ForeignKey('Izdelie', on_delete=models.PROTECT)
    opisanie = models.TextField(max_length=100)
    kolichestvo = models.IntegerField(max_length=50)
    tcena = models.IntegerField(max_length=50)
    proizvoditel = models.TextField(max_length=50)

    objects = models.Manager

    def __str__(self):
        return self.name





from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=50)
    group = models.ForeignKey('Group', on_delete=models.PROTECT)

    objects = models.Manager

class Group(models.Model):
    group = models.CharField(max_length=50)

    objects = models.Manager