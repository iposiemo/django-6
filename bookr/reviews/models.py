from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the publisher")
    website = models.URLField(blank=True, help_text="The website of the publisher")
    email = models.EmailField(blank=True, help_text="The publisher's email address")


class Book(models.Model):
    title = models.CharField(max_length=80, help_text="The title of the book")
    publication_date = models.DateField(verbose_name="Date the book was published")
    isbn = models.CharField(max_length=50, verbose_name="ISBN number of the book")


class Contributor:
    first_name = models.CharField(max_length=50, help_text="Controbutor's first name")
    last_name = models.CharField(max_length=50, help_text="Controbutor's last name")
    email = models.EmailField(blank=True, help_text="The contact email for the contributor")