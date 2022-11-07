from django.db import models
from django.urls import reverse
import uuid  # better than slug become slug is random string
from django.contrib.auth import get_user_model


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/',blank=True)

    id = models.UUIDField(
        primary_key=True,
        db_index=True, #db performance indexing
        default=uuid.uuid4,
        editable=False
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk':str(self.id)})

    # Setting Custom permission
    class Meta:
        indexes =[
            models.Index(fields=['id'],name='id_index'),
        ]
        permissions=[
            ('special_status','Can read all books'),
        ]


class Review(models.Model):
    book = models.ForeignKey(
        Book,  # model
        on_delete=models.CASCADE,
        related_name='reviews'
    )  # one-to-many fields

    review = models.CharField(max_length=255)

    author = models.ForeignKey(
        get_user_model(),  # this is for custom user model
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review
