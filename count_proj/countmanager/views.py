from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *

# Create your views here.



def homePage(request):
	sessions = Session.objects.all()
	form = SessionFilter(request.GET, queryset=sessions)

	print(form)


	context = { 'filter':form}
	return render(request, 'countmanager/SelectSess.html', context)


def bme(request,pk):

	selected_session=Session.objects.get(id=pk)
	
	context= {"sess" : selected_session}

	return render(request, 'countmanager/BME.html', context)

def recordCount(request,pk,bme):

	print(bme)

	selected_session=Session.objects.get(id=pk)
	
	form= CountsForm()
	label=""

	if bme == "b":
		form=form["beginning"]
		label="Beginning"
	elif bme == "m":
		form=form["middle"]
		label="Middle"
	elif bme == "e":
		form=form["end"]
		label="End"

	print(selected_session.counts)

	#print (form["beginning"])

	context= {"sess" : selected_session, "form" : form, "label":label}


	

	return render(request, 'countmanager/RecordCount.html',context)


