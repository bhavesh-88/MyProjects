from django.shortcuts import render,redirect
from .models import Contact,User
from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.
def index(request):
	return render(request,'index.html')
def contact(request):
	if request.method=='POST':
		#print(request.POST['name'])
		Contact.objects.create(
			name=request.POST['name'],
			email=request.POST['email'],
			mobile=request.POST['mobile'],
			remarks=request.POST['remarks'],
			)
		msg="contact saved successfully"
		contacts=Contact.objects.all().order_by('-id')
		return render(request,'contact.html',{'msg':msg,'contacts':contacts})
	else:
		contacts=Contact.objects.all().order_by('-id')	
		return render(request,'contact.html',{'contacts':contacts})

def signup(request):
	if request.method=='POST':
		#print(request.POST['fname'])
		try:
			user=User.objects.get(email=request.POST['email'])      # give singel object
			msg="Email Already Registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:	
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					address=request.POST['address'],
					gender=request.POST['gender'],	
					password=request.POST['password'],
					profile_pic=request.FILES['profile_pic']
					)
				msg="User signup successfully`"
				return render(request,'signup.html',{'msg':msg})
			else:
				msg="Password & Confrim Password Does not Match"
				return render(request,'signup.html',{'msg':msg})	
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])      # give singel object
			if user.password==request.POST['password']:
				request.session['email']=user.email
				request.session['fname']=user.fname
				request.session['profile_pic']=user.profile_pic.url
				return render(request,'index.html')
			else:
				msg="Incorrect password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email not Registered"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		del request.session['profile_pic']
		return render(request,"login.html")
	except:
		return render(request,"login.html")

def change_password(request):
	if request.method=='POST':
		user=User.objects.get(email=request.session['email'])

		if user.password==request.POST['opassword']:
			if request.POST['npassword']==request.POST['cpassword']:
				user.password=request.POST['npassword']
				user.save()
				msg="Password Changed Successfully"
				#return render(request,"change-password.html",{'msg':msg})
				return redirect('logout')  #function call
			else:
				msg="New Password & Confrim New Password Does not Matched"
				return render(request,"change-password.html",{'msg':msg})
		else:
			msg="Old Password Does not Matched"
			return render(request,"change-password.html",{'msg':msg})							
	else:
		return render(request,"change-password.html")			
	

def forgot_password(request):
	if request.method=='POST':
		try:
			user=User.objects.get(email=request.POST['email'])
			otp=random.randint(1000,9999)
			subject = 'OTP for Forgot Password'
			message='HELLO user,Your otp was Forgot Password is : '+str(otp)
			#message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email,]
			send_mail( subject, message, email_from, recipient_list )

			return render(request,'otp.html',{'email':user.email,'otp':otp}) 
		except:
			msg="Email Does Not Registered"
			return render(request,'forgot-password.html',{'msg':msg})
	else:	
		return render(request,'forgot-password.html') 


def verify_otp(request):
	email=request.POST['email']
	otp=request.POST['otp']
	uotp=request.POST['uotp']
	if otp==uotp:
		return render(request,'new-password.html',{'email':email})
	else:
		msg="Invalid Otp"	
		return render(request,'otp.html',{'email':email,'otp':otp,'msg':msg})


def new_password(request):
	email=request.POST['email']
	np=request.POST['new_password']
	cnp=request.POST['cnew_password']

	if np==cnp:
		user=User.objects.get(email=email)
		user.password=np
		user.save()
		msg="Password Update Successfully"
		return render(request,'login.html',{'msg':msg})
	else:
		msg='New password & Confrim New password Does Not Matched'
		return render(request,'new-password.html',{'email':email,'msg':msg})

def profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=='POST':
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		user.gender=request.POST['gender']
		try:
			user.profile_pic=request.FILES['profile_pic']
		except:
			pass
		user.save()
		request.session['profile_pic']=user.profile_pic.url
		msg="Profile Update Successfully"
		return render(request,'profile.html',{'user':user,'msg':msg})
	else:
		return render(request,'profile.html',{'user':user})




