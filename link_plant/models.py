from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(
      max_length=100, 
      choices=(
          ("blue", "Blue"), 
          ("green", "Green"),
          ("red", "Red")))

    def __str__(self):
        return self.name

class Link(models.Model):
    text = models.CharField(max_length=100)
    url = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="links")

    def __str__(self):
        return self.text