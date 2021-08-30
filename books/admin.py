from django.contrib import admin


# Register your models here.
from .models import(
    Contact, UploadsBook, personal_information, 
)


@admin.register(UploadsBook)
class UploadsBookModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'Book_Name', 'Author_Name', 'Description', 'ReleaseDates', 'Selling_price', 'Discount_price', 'Lable', 'Publication', 'Types_of_Book', 'Quantity', 'Image']



@admin.register(personal_information)
class personal_informationModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Phone_number', 'Email', 'State', 'District', 'municipality', 'VDC', 'Ward_No']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Email','Telephone','Subject','Message','date']

