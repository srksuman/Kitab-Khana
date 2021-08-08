from django.db import models

# Create your models here.
Lable_CHOICES = (

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
   Book_Name = models.CharField(max_length=200)
   Author_Name = models.CharField(max_length=100)
   Description = models.TextField()
   ReleaseDates = models.DateTimeField()
   Selling_price = models.FloatField()
   Discount_price = models.FloatField(null=True)
   Lable = models.CharField(choices=Lable_CHOICES, max_length=2)
   Publication = models.CharField(max_length=200)
   Types_of_Book = models.CharField(choices=TYPES_OF_BOOK_CHOICES, max_length=100)
   Quantity = models.PositiveBigIntegerField(default=1)
   Image = models.ImageField(upload_to='book_images/')

def __str__(self):
        return str(self.id)

STATE_CHOICES = (
    ('State No. 1', 'State No. 1'),
      ('State No. 2', 'State No. 2'),
        ('State No. 3', 'State No. 3'),
          ('State No. 4', 'State No. 4'),
           ('State No. 5', 'State No. 5'),
              ('State No. 6', 'State No. 6'),
                ('State No. 7', 'State No. 7')
)


class personal_information(models.Model):
    Name = models.CharField(max_length=100)
    Phone_number = models.CharField(max_length=10)
    Email = models.EmailField(max_length=100)
    State = models.CharField(choices=STATE_CHOICES, max_length=200)
    District = models.CharField(max_length=100)
    municipality = models.CharField(max_length=200)
    VDC = models.CharField(max_length=100)
    Ward_No = models.FloatField(null=True)

    def __str__(self):
        return str(self.id)
