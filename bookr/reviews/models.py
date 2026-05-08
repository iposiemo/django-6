from django.db import models
from django.contrib import auth

class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the publisher")
    website = models.URLField(blank=True, help_text="The website of the publisher")
    email = models.EmailField(blank=True, help_text="The publisher's email address")


class Book(models.Model):
    title = models.CharField(max_length=80, help_text="The title of the book")
    publication_date = models.DateField(verbose_name="Date the book was published")
    isbn = models.CharField(max_length=50, verbose_name="ISBN number of the book")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributor = models.ManyToManyField('Contributor', through="BookContributor")


class Contributor(models.Model):
    first_name = models.CharField(max_length=50, help_text="Controbutor's first name")
    last_name = models.CharField(max_length=50, help_text="Controbutor's last name")
    email = models.EmailField(blank=True, help_text="The contact email for the contributor")


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in the book", choices=ContributionRole.choices, max_length=20)


class Review(models.Model):
    content = models.TextField(help_text="The Review Text")
    rating = models.IntegerField(help_text="The rating the reviewer has given")
    date_created = models.DateTimeField(auto_now_add=True, help_text="The date and time the review was added")
    date_edited = models.DateTimeField(null=True, help_text="The time and date the review was edited")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="The that this review is for")