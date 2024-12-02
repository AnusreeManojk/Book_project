from django.contrib.auth.models import User
from django.db import models

from book_PP.models import Book


#
# class Author(models.Model):
#     name = models.CharField(max_length=200, null=True)
#
#     def __str__(self):
#         return '{}'.format(self.name)
#
#
# class Book(models.Model):
#     title = models.CharField(max_length=200, null=True)
#     price = models.IntegerField(null=True)
#     image=models.ImageField(upload_to='book_media')
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return '{}'.format(self.title)

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(Book)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)