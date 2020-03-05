from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *

# Create your views here.
def rooms(request):
	rooms = Room.objects.all()

	form = RoomForm()

	if request.method =='POST':
		form = RoomForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/counts/room/')


	context = {'rooms':rooms, 'form':form}
	return render(request, 'countmanager/rooms.html', context)

def sess(request):
	sess = Session.objects.all()

	form = SessForm()

	if request.method =='POST':
		form = SessForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/counts/sess/')


	context = {'sessions':sess, 'form':form}
	return render(request, 'countmanager/sessions.html', context)

def speakers(request):
	speakers = Speaker.objects.all()

	form = SpeakerForm()

	if request.method =='POST':
		form = SpeakerForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/counts/speaker/')


	context = {'speakers':speakers, 'form':form}
	return render(request, 'countmanager/speakers.html', context)


def homePage(request):
	sessions = Session.objects.all()
	form = SessionFilter(request.GET, queryset=sessions)

	


	context = {'speakers':speakers, 'filter':form}
	return render(request, 'countmanager/SelectSess.html', context)


