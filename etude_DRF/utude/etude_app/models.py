import uuid
from django.db import models
from django.utils import timezone


class Publisher(models.Model):
    """出版社モデル"""

    class Meta:
        db_table = "publisher"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="出版社", max_length=20)
    create_at = models.DateTimeField(default=timezone.now)


class Author(models.Model):
    """著者モデル"""

    class Meta:
        db_table = "author"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="著者名", max_length=20)
    created_at = models.DateTimeField(default=timezone.now)


class Book(models.Model):
    """本モデル"""

    class Meta:
        db_table = "book"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name="タイトル", max_length=20, unique=True)
    price = models.IntegerField(verbose_name="価格", null=True)
    publisher = models.ForeignKey(
        Publisher, verbose_name="出版社", on_delete=models.SET_NULL, null=True
    )
    authors = models.ManyToManyField(Author, verbose_name="著者", blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class bookStock(models.Model):
    """本のモデル"""

    class Meta:
        db_table = "book_stock"

    book = models.OneToOneField(Book, verbose_name="本", on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="在庫量", default=0)
