from django.db import models

# Create your models here.

class Hobby(models.Model):
    def __str__(self):
        return self.hobby_name + ": " + self.hobby_desc + "\n"

    hobby_name = models.CharField(max_length=200)
    hobby_desc = models.CharField(max_length=2000)

class Portfolio(models.Model):
    def __str__(self):
        return self.project_name + ": " + self.project_desc + "\n"

    project_name = models.CharField(max_length=200)
    project_desc = models.CharField(max_length=2000)
    