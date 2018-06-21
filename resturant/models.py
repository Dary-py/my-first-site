from django.db import models



class ContactsModel(models.Model):
	name = models.CharField(max_length=20, unique = True)
	email = models.EmailField(max_length=20, unique = True)
	text =  models.CharField(max_length=200, unique = True)
	
def __str__(self):
 	return f'id = {self.id} , cname=  {self.name}, text = {self.text}'
# Create your models here.
