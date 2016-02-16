from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import ContactForm, SignUpForm
from .models import SignUp
from .models import Org

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
		#print(SignUp.objects.all())
		# i = 1
		# for instance in SignUp.objects.all():
		# 	print(i)
		# 	print(instance.full_name)
		# 	i += 1


		#org_qs = Org.objects.filter(members=request.user.id)

		org_qs = Org.objects.filter(members=request.user.id).order_by('name')

		context = {

			"user_info": str(request.user),
			"user_id": str(request.user.id),
			"orgs": org_qs,
		}
		"""
			context = {
				"queryset": queryset
			}

		return render(request, "home.html", context)
		"""
		return render(request, "user_dash.html", context)



# information and managment for org members and admis, as well as exec
def orgView(request, id):
	if request.user.is_authenticated():
		#print(SignUp.objects.all())
		# i = 1
		# for instance in SignUp.objects.all():
		# 	print(i)
		# 	print(instance.full_name)
		# 	i += 1


		org_qs = Org.objects.filter(members=request.user.id).filter(id=id).order_by('name')


		context = {

		"orginfo" : "bla",
		"id": id,
		"orgs": org_qs,

		}

		#org_qs = Org.objects.filter(members=request.user.id)
		return render(request, "org_view.html", context)



def orgs(request):
	return redirect('newsletter.views.userDash')





