from django import forms

from .models import SignUp
from .models import Org

from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User


class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']
		### exclude = ['full_name']
	
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		# if not domain == 'USC':
		# 	raise forms.ValidationError("Please make sure you use your USC email.")
		if not extension == "edu":
			raise forms.ValidationError("Please use a valid .EDU email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		#write validation code.
		return full_name


class OrgForm(forms.ModelForm):
	class Meta:
		model = Org
		fields = ['name','description','members','org_admins','org_exec']
		widgets = {
            'members': forms.CheckboxSelectMultiple(),
            'org_admins': forms.CheckboxSelectMultiple()
        }
		
		
