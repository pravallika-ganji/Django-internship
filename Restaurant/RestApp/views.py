from django.shortcuts import render,redirect
from django.http import HttpResponse
from RestApp.forms import ReForm
from RestApp.models import Restaurant


# Create your views here.
def home(request):
	return render(request,'app/home.html')

def about(request):
	return render(request,'app/about.html')

def contact(request):
	return render(request,'app/contact.html')

def restlist(request):
	y = Restaurant.objects.all()
	if(request.method=="POST"):
		t = ReForm(request.POST)
		if t.is_valid():
			t.save()
			return redirect("/rlist")
	t = ReForm()
	return render(request,'app/restaurantlist.html',{'q':t,'a':y})

def rstup(request,m):
	k = Restaurant.objects.get(id=m)
	if request.method == "POST":
		e = ReForm(request.POST,instance=k)
		if e.is_valid():
			e.save()
			return redirect('/rlist')
	e = ReForm(instance=k)
	return render(request,'app/restupdate.html',{'x':e})








