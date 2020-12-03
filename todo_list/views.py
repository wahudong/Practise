from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm, CreateUserForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

# Create your views here.

def home(request):

  if request.method == 'POST':
    form = ListForm(request.POST or None)

    if form.is_valid():
      form.save()
      all_items = List.objects.all
      messages.success(request, ('Item Has Been Added To List!'))
      return render(request,'home.html', {'all_items':all_items})
  else:
    all_items = List.objects.all
    return render(request, 'home.html', {'all_items':all_items})

def about(request):
  context = {'first_name':'BenBen', 'last_name': 'Wang'}
  return render(request, 'about.html', context )

def delete(request,list_id):
  item =  List.objects.get(pk=list_id)
  item.delete()
  messages.success(request, ('Item Has Been Deleted'))
  return redirect('home')

def cross_off(request, list_id):
  item = List.objects.get(pk=list_id)
  item.completed = True
  item.save()
  return redirect('home')

def uncross(request, list_id):
  item = List.objects.get(pk=list_id)
  item.completed = False
  item.save()
  return redirect('home')

def edit(request, list_id):
  if request.method == 'POST':
      item = List.objects.get(pk=list_id)

      form = ListForm(request.POST or None, instance=item)

      if form.is_valid():
        form.save()
        all_items = List.objects.all
        messages.success(request, ('Item Has Been Edited!'))
        return redirect('home')
  else:
    item = List.objects.get(pk=list_id)
    return render(request, 'edit.html', {'item':item})

def register(request):
  form = CreateUserForm()

  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      user = form.cleaned_data.get('username')
      messages.success(request, 'Account was created for ' + user)
      return redirect('login')

  context={'form':form}
  return render(request, 'register.html', context)


def login(request):
  context={}
  return render(request, 'login.html', context)