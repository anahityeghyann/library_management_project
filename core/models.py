from django.contrib.auth.models import AbstractUser
from django.db import models


class Libraryuser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    member_type = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True)  # Taken from Member
    active_member = models.BooleanField(default=True)

    def str(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)

    def str(self):
        return self.name


class Book(models.Model):
    LANGUAGE_CHOICES = [
        ("English", "English"),
        ("French", "French"),
        ("Spanish", "Spanish"),
        ("German", "German"),
        ("Chinese", "Chinese"),
        ("Arabic", "Arabic"),
    ]

    GENRE_CHOICES = [
        ("Fiction", "Fiction"),
        ("Non-Fiction", "Non-Fiction"),
        ("Science", "Science"),
        ("Sci-Fi", "Sci-Fi"),
        ("Fantasy", "Fantasy"),
        ("Biography", "Biography"),
        ("History", "History"),
        ("Romance", "Romance"),
        ("Mystery", "Mystery"),
        ("Self-Help", "Self-Help"),
        ("Finance", "Finance"),
    ]

    title = models.CharField(max_length=255)

    author = models.CharField(max_length=255)

    publication_year = models.IntegerField(null=True, blank=True)

    language = models.CharField(
        max_length=50,
        choices=LANGUAGE_CHOICES,
        default="English"
    )

    genre = models.CharField(
        max_length=50,
        choices=GENRE_CHOICES
    )

    page_count = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    publisher = models.CharField(max_length=255)

    def str(self):
        return self.title


class BookCopy(models.Model):
    STATUS_CHOICES = [
        ("available", "Available"),
        ("borrowed", "Borrowed"),
        ("lost", "Lost"),
        ("damaged", "Damaged"),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="copies")
    barcode = models.CharField(max_length=50, unique=True)
    acquisition_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="available")
    location = models.CharField(max_length=100)

    def str(self):
        return f"{self.book.title} ({self.barcode})"


class Loan(models.Model):
    copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE, related_name="loans")
    member = models.ForeignKey(Libraryuser, on_delete=models.CASCADE, related_name="loans")
    loan_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def str(self):
        return f"{self.member} - {self.copy}"