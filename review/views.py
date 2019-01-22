from django.shortcuts import render,redirect,HttpResponse
from .forms import login_form_org,login_form,add_service
from .forms import admin_login_form,auth_form
from .models import Org,Services,Admin
import random
from django.http import Http404
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def create(request):

	if request.method == 'GET':
		
		form = login_form_org()

		return render(request,'login_org.html',{'form':form})

	if request.method == 'POST':
		form = login_form_org(request.POST)
		if form.is_valid():
			password = form.cleaned_data['password']
			confirm_password = form.cleaned_data['confirm_password']
			if(password==confirm_password):
				form.save()
				form = login_form_org()
				success = "Registered success"
				context = {
				'not':success,
				'form':form
				}
			else:
				form = login_form_org()
				error = "password and confirm password doesnot not match"
				context={
				'not':error,
				'form':form
				}
		
		return render(request,'login_org.html',context)
	
def login(request):

	form = login_form()

	if request.method =='GET':
		if request.session.has_key('company'):
			username = request.session['company']
			context = {
				'username':username,
				}
			return redirect("/homepage")
		else:
			error = "Please login"
			context = {
			'form':form
			}
			return render(request,'login.html',context)
	else:
		form = login_form(request.POST)
		if form.is_valid():
			company = form.cleaned_data['company']
			password = form.cleaned_data['password']
			Check = Org.objects.filter(company=company,password=password).count()
			if(Check>=1):
				request.session['company'] = company
				context = {
				'username':company
				}
				return redirect('/homepage')
			else:
				error = "Please login"
				context = {
				'error':error
				}
				return redirect('/homepage')

def logout(request):
	form =login_form()
	del request.session['company']
	context={
	'form':form
	}
	return redirect('/login')

def homepage(request):
	if request.session.has_key('company'):
		form = add_service()
		username = request.session['company']
		query_set = Services.objects.filter(company=username)
		context = {
		'objects': query_set,
		'username':username,
		'form':form
		}
		return render(request,'test.html',context)
	else:
		return redirect('/login')

def add_service_form(request):
	form = add_service(request.POST)
	username = request.session['company']
	if form.is_valid():
		company = form.cleaned_data['company']
		service = form.cleaned_data['service']
		category = form.cleaned_data['category']
		description = form.cleaned_data['description']
		if(company==username):
			form.save()
		else:
			return HttpResponse(form)
		return redirect('/homepage')
	
def myservice(request,id):
	if request.session.has_key('company'):
		username = request.session['company']
		query_set = Services.objects.get(id=id)
		return render(request,'myservice.html',{'object':query_set,'username':username})

def admin_login(request):
	if request.method == 'GET':
		form = admin_login_form()
		return render(request,'login_admin.html',{'form':form})
	else:
		form = admin_login_form(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			Check = Admin.objects.filter(username=username,password=password,email=email).count()
			if(Check>=1):
				request.session['username'] = username
				otp = random.randint(50000,70000)
				request.session['otp'] = otp
				subject='Hey Admin'
				message='This is your OTP to login '+str(otp)
				from_email=settings.EMAIL_HOST_USER
				to_email = [email]
				send_mail(subject=subject,from_email=from_email,recipient_list=to_email,message=message,fail_silently=False)
				return redirect('/auth')
			else:
				error = "Username or password invalid!!!!"
				context = {
				'error':error,
				'form':form
				}
				return render(request,'login_admin.html',context)

def auth(request):
	if request.method == 'GET':
		if request.session.has_key('otp'):
			if(request.session.has_key('admin_verify') and request.session['admin_verify'] == "1"):
				return redirect('/admin_home')
			else:
				form = auth_form()
				otp = request.session['otp']
				return render(request,'auth.html',{'form':form,'otp':otp})
		else:
			return HttpResponse("Page does not exist")
	else:
		form = auth_form(request.POST)
		if form.is_valid():
			otp = request.session['otp']
			otp1 = form.cleaned_data['otp_test']
			otp1 = int(otp1)
			if(otp1==otp):
				request.session['admin_verify'] = "1"
				return redirect('/auth')
			else:
				del request.session['otp']
				del request.session['username']
				return redirect('/admin_login')

def admin_home(request):
	query_set = Org.objects.all()
	context = {
		'all_company': query_set 
	}
	return render(request,'auth_admin.html', context)