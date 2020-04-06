from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *

# Create your views here.



def homePage(request):
	
	print(request)

	sessions = Session.objects.all()
	form = SessionFilter(request.GET, queryset=sessions)

	print(form)

	success_msg=" "
	context = { 'filter':form, "msg":success_msg}
	
	return render(request, 'countmanager/SelectSess.html', context)

#beggining middle end
def bme(request,pk):

	selected_session=Session.objects.get(id=pk)
	
	context= {"sess" : selected_session}

	return render(request, 'countmanager/BME.html', context)

def recordCount(request,pk,bme):


	if request.method == 'POST':

		selected_session=Session.objects.get(id=pk)


		if bme == "Beginning":
			selected_session.beginning_count=request.POST[bme.lower()]
		elif bme == "Middle":
			selected_session.middle_count=request.POST[bme.lower()]
		elif bme == "End":
			selected_session.end_count=request.POST[bme.lower()]
		
		success_msg="Successfully Recorded Count"

		selected_session.save()

		print(request.POST[bme.lower()])
		

		return redirect('/counts/')


	print(bme)

	selected_session=Session.objects.get(id=pk)
	
	

	
	form= CountsForm()
	
	
	label=""

	if bme == "b":
		form=form["beginning"]
		label="Beginning"
		form.initial=selected_session.beginning_count
	elif bme == "m":
		form=form["middle"]
		label="Middle"
		form.initial=selected_session.middle_count
	elif bme == "e":
		form=form["end"]
		label="End"
		form.initial=selected_session.end_count

	#print(selected_session.counts)

	print (form.value)

	context= {"sess" : selected_session, "form" : form, "label":label}


	

	return render(request, 'countmanager/RecordCount.html',context)


