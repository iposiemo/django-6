from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the publisher")
    website = models.URLField(blank=True, help_text="The website of the publisher")
    email = models.EmailField(blank=True, help_text="The publisher's email address")
