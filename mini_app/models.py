from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField()  # Percentage level of the skill (0-100)

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='services/')  # Ensure you have a media directory for images

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')  # Ensure you have a media directory for images
    link = models.URLField(blank=True)  # URL for the project link

    def __str__(self):
        return self.title

class Counter(models.Model):
    title = models.CharField(max_length=255)
    value = models.IntegerField()

    def __str__(self):
        return self.title

class PortfolioItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.title
