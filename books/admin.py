from django.contrib import admin


# Register your models here.
from .models import(
    Contact, UploadsBook, 
)


@admin.register(UploadsBook)
class UploadsBookModelAdmin(admin.ModelAdmin):
    list_display =  ['isbn','Book_Name','Seller_phoneno','Seller_address','Author_Name','ReleaseDate','Selling_price','Description','Publication','Types_of_Book','Label','Quantity','Image']



# @admin.register(personal_information)
# class personal_informationModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'Name', 'Phone_number', 'Email', 'State', 'District', 'municipality', 'VDC', 'Ward_No']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Email','Telephone','Subject','Message','date']

