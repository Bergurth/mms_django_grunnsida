from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #Python 3.3 is __str__
		return self.email

"""
class Organization(models.Model):
	#group_founder = models.ForeignKey(user, on_delete=models.CASCADE)
	group_founder = models.ForeignKey(User, related_name='profile', unique=True)
	name = models.CharField(max_length=120, blank=True, null=True)
	description = models.CharField(max_length=520, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	members = models.ManyToManyField(
        User,
        through='Membership',
        through_fields=('organization', 'user'),
    )
	def __unicode__(self):
		return self.name

class Membership(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
"""

class Org(models.Model):
	name = models.CharField(max_length=128)
	members = models.ManyToManyField(User, related_name='orgs')
	org_admins = models.ManyToManyField(User, related_name='orgs_adm')
	# more stuff
	description = models.CharField(max_length=520, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.name

