from django import forms
from django.forms.extras.widgets import SelectDateWidget
from models import Crop, Problem_type, Problem_specifics

# This file defines forms, which collect inputs from user to add entry to database

# The Crop form, only one field is needed (the crop name)
class CropForm(forms.Form):
    crop_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-lg-7'}), label='Crop name*', max_length=200)

# The Farm form, 8 fields are needed
class FarmForm(forms.Form):
	farm_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-lg-7'}), label='Farm name*', max_length=200, error_messages={'required': 'Please enter your name'})
	city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-lg-7'}), label='City*', max_length=200)
	state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-lg-7'}), label='State*', max_length=200)
	address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-lg-7'}), label='Address*', max_length=200)
	office_num = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-lg-7'}), label='Office Number', max_length=200, required=False)
	fax = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-lg-7'}), label='Fax', max_length=200, required=False)
	web = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-lg-7'}), label='Web', max_length=200, required=False)
	notes = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control col-lg-7'}), label='Notes', required=False)

# The Client form, 8 fields are needed
class ClientForm(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-lg-7'}), label='First Name*', max_length=200)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-lg-7'}), label='Last Name*', max_length=200)
	phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-lg-7'}), label='Phone*', max_length=200, required=False)
	spouse = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-lg-7'}), label='Spouse', max_length=200, required=False)
	children = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-lg-7'}), label='Children', max_length=200, required=False)
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control col-lg-7'}), label='Email', max_length=200, required=False)
	pet = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-lg-7'}), label='Pet', max_length=200, required=False)
	notes = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control col-lg-7'}), label='Notes' , required=False)
		
# The Visit form, 1 field is needed
class VisitForm(forms.Form):
	visit_date = forms.DateField(widget=SelectDateWidget(attrs={'class':'form-control col-lg-7'}), label='Visit Date*', required=True)

# The Problem from
class ProblemForm(forms.Form):
	#farm_id will come from the view
	crop_name = forms.ModelChoiceField(queryset=Crop.objects.all().order_by('crop_name'))
	notes = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control col-lg-7'}), label='Notes' , required=False)

# Problem specific form
class ProblemSpecificForm(forms.Form):
	type_name = forms.ModelChoiceField(queryset=Problem_type.objects.all().order_by('type_name'))
	specific_name = forms.ModelChoiceField(queryset=Problem_specifics.objects.all().order_by('name'))
	# TODO: REMEMBER TO USE AJAX TO GET THE SPECIFICS OF THIS CERTAIN TYPE!!!!



