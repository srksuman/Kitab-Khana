from django.db.models import fields
from books.models import UploadsBook
from django import forms
from .models import Label_CHOICES, TYPES_OF_BOOK_CHOICES, UploadsBook
from django.forms.widgets import NumberInput
from django.core.exceptions import ValidationError
import re


class AddProductForm(forms.ModelForm):
     Seller_phoneno = forms.IntegerField(label="phoneno",widget=forms.TextInput(attrs={"placeholder":"phoneno", 'class':'form-control','style':'margin-bottom:10px; width:450px'}),error_messages={'required':'phoneno is required'})
     class Meta:
        model = UploadsBook
       
        fields =  ['isbn','Book_Name','Seller_phoneno','Seller_address','Author_Name','ReleaseDate','Selling_price','Description','Publication','Types_of_Book','Label','Quantity','Image']
   
        widgets={
            
            'isbn':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px; width:450px','placeholder':'isbn'}),
            'Book_Name':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px; width:450px','placeholder':'book name',}),
            'Author_Name':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px; width:450px','placeholder':'author name',}),
            'Seller_address':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px;    width:450px','placeholder':'address',}),
            'ReleaseDate':forms.NumberInput(attrs={'type':'date','class':'form-control','style':'margin-bottom:10px; width:450px','placeholder':'released date',}),
            'Selling_price':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px; width:450px','placeholder':'selling price',}),
            'Description':forms.Textarea(attrs={'class':'form-control','style':'margin-bottom:10px; width:450px','placeholder':'description ',}),
            'Publication':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px; width:450px','placeholder':'publication',}),
            'Label':forms.Select(choices=Label_CHOICES, attrs={'class':'form-control','style':'margin-bottom:10px; width:300px',}),
            'Types_of_Book':forms.Select(choices=TYPES_OF_BOOK_CHOICES,attrs={'class':'form-control','style':'margin-bottom:10px; width:300px',}),
            'Quantity':forms.NumberInput(attrs={'class':'form-control','style':'margin-bottom:10px; width:300px',}),
            # 'Image':forms.I(attrs={'class':'form-control  ','style':'form-control','style':'margin-bottom:10px; width:300px','placeholder':'choose image',})
        }



# class AddSellerForm(forms.ModelForm):
    
#     class Meta:
#         model = personal_information
#         fields = [ 'Name', 'Phone_number', 'Email', 'State', 'District', 'municipality', 'VDC', 'Ward_No']
   
#         widgets={
            
#             'isbn':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px; width:450px','placeholder':'isbn'}),
#             'Book_Name':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px; width:450px','placeholder':'book name',}),
#             'Author_Name':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px; width:450px','placeholder':'author name',}),
#             'ReleaseDate':forms.NumberInput(attrs={'type':'date','class':'form-control','style':'margin-bottom:10px; width:450px','placeholder':'released date',}),
#             'Selling_price':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px; width:450px','placeholder':'selling price',}),
#             'Description':forms.Textarea(attrs={'class':'form-control','style':'margin-bottom:10px; width:450px','placeholder':'description ',}),
#             'Publication':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px; width:450px','placeholder':'publication',}),
#             'Label':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px; width:300px',}),
#             'Types_of_Book':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px; width:300px',}),
#             'Quantity':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px; width:300px',}),
#             'Image':forms.TextInput(attrs={'class':'form-control  ','style':'form-control','style':'margin-bottom:10px; width:300px','placeholder':'choose image',})}


   
    # isbn = forms.IntegerField(label="isbn", widget=forms.TextInput(attrs={"placeholder":"isbn"}),error_message={"required":"Please enter isbn"},)
    # bookname = forms.CharField(label="bookname",widget=forms.TextInput(attrs={"placeholder":"book name"}),error_message={"required":"please enter book name"},)
    # author = forms.CharField(label="author",widget=forms.TextInput(attrs={"placeholder":"authorname"}),error_message={"required":"please enter author name"},)
    # released_year = forms.CharField(label="released_year",widget=forms.TextInput(attrs={"placeholder":"released year"}),error_message={"required":"please enter released year"},)
    # seller_name = forms.CharField(label="seller_name",widget=forms.TextInput(attrs={"placeholder":"Seller Name","required":True}),error_messages={"required":"Seller name cannot be empty"})
    # seller_contact = forms.IntegerField(label="seller contact number",widget=forms.TextInput(attrs={"placeholder":"Seller Contact number","required":True}),error_messages={"required":"Seller contact number cannot be empty"})
    # book_description = forms.CharField(label="book description",widget=forms.TextInput(attrs={"placeholder":"description","required":True}),error_messages={"required":"description cannot be empty"})
    # book_category = forms.CharField(label="book description",widget=forms.TextInput(attrs={"placeholder":"description","required":True}),error_messages={"required":"description cannot be empty"})





