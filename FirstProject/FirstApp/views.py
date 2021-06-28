from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register
# Create your views here.
def home(request):
	return HttpResponse("Hi Good Evening to All...")

def htmltag(req):
	return HttpResponse("<h2>Hi Welcome to APSSDC Programs</h2>")

def usernameprint(request,uname):
	return HttpResponse("<h2>Hi Welcome <span style='color:green'>{}</span></h2>".format(uname))

def usernameage(request,un,ag):
	return HttpResponse("<h3 style='text-align:center;background-color:green;padding:23px'>Hi User <span style='color:yellow'>{}</span> and your age is: <span style='color:red'>{}</span></h3>".format(un,ag))

def empdetails(request,eid,ename,eage):
	return HttpResponse("<script>alert('Hi Welcome {}')</script><h3>Hi Welcome {} and your age is: {} and your id is: {}</h3>".format(ename,ename,eage,eid))

def htm(request):
	return render(request,'html/sample.html')

def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})

def empname(request,id,ename):
	k = {'i':id,'n':ename}
	return render(request,'html/ehtml.html',k)

def studentdetails(request):
	return render(request,'html/std.html')

def internalJS(request):
	return render(request,'html/internalJs.html')

def myform(req):
	if req.method=="POST":
		uname = req.POST['uname']
		rollno = req.POST['rollno']
		email = req.POST.get('email')
		data = {'username':uname,'rno':rollno,'emailID':email}
		return render(req,'html/display.html',data)
	return render(req,'html/myform.html')

def signup(req):
	if req.method=="POST":
		fname = req.POST['fname']
		lname = req.POST['lname']
		phno = req.POST['phno']
		email = req.POST.get('email')
		gender = req.POST.get('gender')
		add = req.POST.get('add')
		luk = req.POST.getlist('luk')
		data = {'fname':fname,'lname':lname,'phno':phno,'email':email,'gender':gender,'add':add,'luk':luk}
		return render(req,'html/see.html',data)
	return render(req,'html/signup.html')

def bootstrapfun(request):
	return render(request,'html/sampleboot.html')

def btregi(request):
	return render(request,'html/btregst.html')


def register1(request):
	reg = Register(name = "pinky",email="pinky@gmailcom")
	reg.save()
	return HttpResponse("row inserted successfully...")

def register2(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		reg = Register(name = name, email = email)
		reg.save()
		return HttpResponse("Record inserted successfully....")
	return render(request,"html/register2.html")

def display(request):
	data = Register.objects.all()
	return render(request,'html/display1.html',{'data':data})

def sview(request,y):
	w = Register.objects.get(id=y)
	return render(request,'html/sview.html',{'y':w})
	# return HttpResponse("Your Name is: {} and your email id is: {}".format(w.name,w.email))

def supt(request,q):
	t = Register.objects.get(id=q)
	if request.method == "POST":
		na = request.POST['n']
		em = request.POST['e']
		t.name = na
		t.email = em
		t.save()
		return redirect('/display')
	return render(request,'html/supdate.html',{'p':t})

def sudl(request,p):
	b = Register.objects.get(id=p)
	if request.method == "POST":
		b.delete()
		return redirect('/display')
	return render(request,'html/sndlt.html',{'z':b})


