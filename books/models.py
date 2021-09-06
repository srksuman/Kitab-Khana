from django.db import models


# Create your models here.


Label_CHOICES = (

    ('o', 'Old'),
    ('N', 'New'),   
)


TYPES_OF_BOOK_CHOICES = (

    ('Action and Adventure', 'Action and Adventure'),
    ('Classics', 'Classics'),
    ('Comic Book or Graphic Novel', 'Comic Book or Graphic Novel.'),
    ('Detective and Mystery', 'Detective and Mystery'),
    ('Fantasy', 'Fantasy'),
    (' Historical Fiction', ' Historical Fiction'),
    ('Horror', ' Horror'),
    ('Literary Fiction', 'Literary Fiction'),
    ('School', 'School'),
    ('+2', '+2'),
    ('+2', '+2'),
    ('Bachelor', 'Bachelor'),
    ('Bachelor', 'Bachelor'),
    ('Master  and degree', 'Master  and degree'),
    ('Other', 'Others'),
  
)
class UploadsBook(models.Model):
   isbn = models.CharField(max_length=30)
   Book_Name = models.CharField(max_length=200)
   Author_Name = models.CharField(max_length=100)
   Description = models.TextField()
   ReleaseDate = models.DateTimeField()
   Selling_price = models.FloatField()
   Label = models.CharField(choices=Label_CHOICES, max_length=2)
   Publication = models.CharField(max_length=200)
   Types_of_Book = models.CharField(choices=TYPES_OF_BOOK_CHOICES, max_length=100)
   Quantity = models.PositiveBigIntegerField(default=1)
   Image = models.ImageField(upload_to='book_images/')
   Seller_phoneno = models.PositiveBigIntegerField(null=True,blank=True)
   Seller_address = models.CharField(max_length=200,null=True,blank=True)



class Contact(models.Model):
    Name = models.CharField(max_length=122)
    Email = models.CharField(max_length=122)
    Telephone = models.CharField(max_length=12)
    Subject = models.TextField()
    Message = models.TextField()
    date = models.DateField() 
