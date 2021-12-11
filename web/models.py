from django.db import models
from django.db.models.base import ModelState
from django.utils import timezone

# Create your models here.

class WilkommensText(models.Model):
    HeadLine = models.TextField(max_length=100)
    SmallHeadLine = models.TextField(max_length=50)
    Text = models.TextField(max_length=2000)
    Bild = models.ImageField(upload_to="pictures/")
    BildBeschreibung = models.TextField(max_length=50)
    Anzeigen = models.BooleanField(default=True)

class Fotos(models.Model):
    HeadLine = models.TextField(max_length=100)
    Beschreibung = models.TextField(max_length=2000)
    Bild = models.ImageField(upload_to="pictures/")

class Blog(models.Model):
    HeadLine = models.TextField(max_length=100)
    smallHeadLine = models.TextField(max_length=100)
    Text = models.TextField(max_length=2000)
    Bild1 = models.ImageField(upload_to="pictures/", blank=True)
    Bild2 = models.ImageField(upload_to="pictures/", blank=True)
    pub_date = models.DateField()
    TimeToRead = models.IntegerField()

class Sponsoren(models.Model):
    Name = models.CharField(max_length=50)
    Summe = models.IntegerField()
    Statement = models.TextField(max_length=2000)

class Roadmap(models.Model):
    Beschreibung = models.TextField(max_length=2000)
    Headline = models.CharField(max_length=50)
    Jahr = models.IntegerField()

class Kontakt(models.Model):
    Paypal = models.URLField()
    Instagram = models.URLField()
    Facebook = models.URLField()
    Youtube = models.URLField()
    Email = models.EmailField(null=True)
    Aktuell = models.BooleanField(default=True)