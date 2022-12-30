from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse
from  .models import Room, Topic
from .forms import RoomForm
# Create your views here.

def loginPage(request):
  page = 'login'
  
  # to avoid user login again if already did
  if request.user.is_authenticated :
    return redirect('home')
  
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    try:
      user = User.objects.get(username=username) # check if the user exist
    except:
      messages.error(request, 'User does not exist')
    
    # if this user exist, check if is authenticate
    user = authenticate(request, username=username, password=password) 
    # if authenticate, will return a user object
    if user is not None:
      login(request, user) # 'login' will add the session in the database, and inside the browser, the user will officially login 
      return redirect('home')
    else:
      messages.error(request, 'Username OR Password does not exist')
    
  context = {'page': page}
  return render(request, 'base/login_register.html', context)

def logoutUser(request):
  logout(request)
  return redirect('home')
  
def registerPage(request):
  form = UserCreationForm()
  
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      # commit=False: save this user, but freeze the time, which is we want to be able to access to this user right away
      user.username = user.username.lower()
      user.save()
      login(request, user)
      return redirect('home')
    else:
      messages.error(request, 'An error occured during registration.')
      
  context = {'form': form}
  return render(request, 'base/login_register.html', context)
  
def home(request):
  # rooms = Room.objects.all()
  q = request.GET.get('q') if request.GET.get('q') != None else ''
  rooms = Room.objects.filter(
    Q(topic__name__icontains=q) |
    Q(name__icontains=q) | 
    Q(description__icontains=q)
    ) 
  # '__name': the double underscore is to the attribute of the parent
  # '__icontains': this makes if there isn't any room related with this topic, rooms will be all instance
    # 'i' is to make case insensitve, other options like start with, end with, etc
  # 'Q' makes it possible to search by different values
  
  topics = Topic.objects.all()
  room_count = rooms.count()
  
  context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
  return render(request, 'base/home.html', context)

def room(request, pk):
  room = Room.objects.get(id=pk)
  context = {'room': room}
  return render(request, 'base/room.html', context)

@login_required(login_url='login')
def createRoom(request):
  form = RoomForm()
  if request.method == 'POST':
    # print(request.POST)
    form = RoomForm(request.POST)
    if form.is_valid():
      form.save() # if valid, save the model into database
      return redirect('home')
    
  context = {'form': form}
  return render(request, "base/room_form.html", context)

@login_required(login_url='login')
def updateRoom(request, pk):
  room = Room.objects.get(id=pk)
  form = RoomForm(instance=room) # pass in the instance value
  
  if request.user != room.host:
    return HttpResponse('You are not allow to update this room.')
  
  if request.method == 'POST':
    form = RoomForm(request.POST, instance=room)
    if form.is_valid():
      form.save() # if valid, save the model into database
      return redirect('home')
    
  context = {'form': form}
  return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
  room = Room.objects.get(id=pk)
  
  if request.user != room.host:
    return HttpResponse('You are not allow to update this room.')
  
  if request.method == 'POST':
    room.delete() # remove the item from the database and delete it
    return redirect('home')
  
  return render(request, 'base/delete.html', {'obj': room})