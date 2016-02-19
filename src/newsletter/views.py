from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import ContactForm, SignUpForm, OrgForm
from .models import SignUp
from .models import Org
from django.contrib.auth.models import User

# Create your views here.
def home(request):
	title = 'Sign Up Now'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		#form.save()
		#print request.POST['email'] #not recommended
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		# if not instance.full_name:
		# 	instance.full_name = "Justin"
		instance.save()
		context = {
			"title": "Thank you"
		}

	if request.user.is_authenticated() and request.user.is_staff:
		#print(SignUp.objects.all())
		# i = 1
		# for instance in SignUp.objects.all():
		# 	print(i)
		# 	print(instance.full_name)
		# 	i += 1

		queryset = SignUp.objects.all().order_by('-timestamp') #.filter(full_name__iexact="Justin")
		#print(SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="Justin").count())
		context = {
			"queryset": queryset
		}

	return render(request, "home.html", context)



def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		# 	#print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email, message, full_name
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'youotheremail@email.com']
		contact_message = "%s: %s via %s"%( 
				form_full_name, 
				form_message, 
				form_email)
		some_html_message = """
		<h1>hello</h1>
		"""
		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				html_message=some_html_message,
				fail_silently=True)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}
	return render(request, "forms.html", context)



def userDash(request):
	if request.user.is_authenticated():

		org_qs = Org.objects.filter(members=request.user.id).order_by('name')

		context = {

			"user_info": str(request.user),
			"user_id": str(request.user.id),
			"orgs": org_qs,
		}
	
		return render(request, "user_dash.html", context)
	else:
		return redirect(settings.LOGIN_REDIRECT_URL)



# information and managment for org members and admis, as well as exec
def orgView(request, id):
	if request.user.is_authenticated():
	
		org_qs = Org.objects.filter(members=request.user.id).filter(id=id).order_by('name')

		if org_qs:
			
			description = org_qs[0].description

			admin = org_qs.filter(org_admins=request.user.id).filter(id=id)

		 	is_exec = org_qs.filter(org_exec=request.user.id).filter(id=id)

		 	members = User.objects.filter(orgs=id)

		 	
			context = {

		
			"id": id,
			"orgs": org_qs,
			"org_description": description,
			"is_admin": admin,
			"is_exec": is_exec,
			"members": members,

			}

			#org_qs = Org.objects.filter(members=request.user.id)
			return render(request, "org_view.html", context)
		else:
			return redirect(settings.LOGIN_REDIRECT_URL)
	else:
		return redirect(settings.LOGIN_REDIRECT_URL)


def orgEdit(request, id=None):
	if request.user.is_authenticated():

		# this is the case of modifying an existing org
		if id:

			org_qs = Org.objects.filter(org_exec=request.user.id).filter(id=id).order_by('name')
			if org_qs:
				title = 'Edit Org'
				title_align_center = True

				org = Org.objects.get(pk=id)
				#form = OrgForm(instance=org)
				if request.method == 'POST':
					form = OrgForm(request.POST, instance=org)
					form.save()

				else:
					form = OrgForm(instance=org)
				
				context = {
					"form": form,
					"title": title,
					"title_align_center": title_align_center,
					}
				return render(request, "forms.html", context)
			else:
				# user is not exec of said org.
				return render(request, "403.html")
		else:
			# no org id specified.  ------------------------> creating New org.
			
			title = 'Edit Org'
			title_align_center = True
			if request.method == 'POST':
					form = OrgForm(request.POST)
					form.save()
			else:
				form = OrgForm(None)

			context = {
					"form": form,
					"title": title,
					"title_align_center": title_align_center,
					}
			return render(request, "forms.html", context)
			




def orgs(request):
	if request.user.is_authenticated():
		return redirect('newsletter.views.userDash')
	else:
		return redirect(settings.LOGIN_REDIRECT_URL)




