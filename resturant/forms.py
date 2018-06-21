from django import forms
from . import models

class ResturantForm(forms.ModelForm):
	class Meta:
		model= models.ContactsModel
		fields = '__all__'
		

