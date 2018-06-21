from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render
from datetime import datetime
from django.conf import settings
from . import forms
from . import models
from . import views
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
# Create your views here.
def main_page(request):
	cont = models.ContactsModel.objects.all()
	return render(request, 'resturant/index.html', dict(cont=cont))

def about_page(request):
	return render(request, 'resturant/about.html', dict())

def menu_page(request):
	return render(request, 'resturant/menu.html', dict())\

def news_page(request):
	return render(request, 'resturant/news.html', dict())

def contacts_page(request):
	form = forms.ResturantForm()
	if request.method=='POST':
		form = forms.ResturantForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('main')
		else:
			form = forms.ResturantForm()
	return render(request, 'resturant/contacts.html',dict(form=form))

	

def single_page(request):
	return render(request, 'resturant/contacts.html', dict())

class ContactCreateView(CreateView):
	form_class = forms.ResturantForm
	model = models.ContactsModel