from django.db import models

# Create your models here.

class Hobby(models.Model):
    def __str__(self):
        return self.hobby_name + ": " + self.hobby_desc + "\n"

    hobby_name = models.CharField(max_length=200)
    hobby_desc = models.CharField(max_length=2000)
    hobby_image = models.CharField(max_length=500, default="https://thumbs.dreamstime.com/b/hobbies-activity-amusement-freetime-interest-concept-74926992.jpg")

class Portfolio(models.Model):
    def __str__(self):
        return self.project_name + ": " + self.project_desc + "\n"

    project_name = models.CharField(max_length=200)
    project_desc = models.CharField(max_length=2000)
    project_image = models.CharField(max_length=500, default="https://cdn-icons-png.freepik.com/512/12238/12238054.png")
    project_url = models.URLField(max_length=400, null=True, blank=True)

class Contact(models.Model):
    def __str__(self):
        return self.contact_name + ": " + self.contact_message + "\n"

    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    contact_message = models.CharField(max_length=2000)

    