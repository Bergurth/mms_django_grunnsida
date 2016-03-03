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

	#parent_org = models.ForeignKey(Org, on_delete=models.CASCADE, blank=True)
	org_exec = models.ForeignKey(User, blank=True, related_name='org_exec', null=True)
	#org_type = models.ForeignKey(OrgType, blank=True, null=True)


	def __unicode__(self):
		return self.name

'''
class OrgType(models.Model):
	name = models.CharField(max_length=128)
	description = models.CharField(max_length=520, blank=True, null=True)
	# ParentType somthing that can be null refrencing a parent type.

'''



class Student(models.Model):
	ss_number = models.IntegerField()
	name = models.CharField(max_length=228)
	date_of_birth = models.DateTimeField(blank=True, null=True)
	sex = models.IntegerField(blank=True, null=True)
	user = models.ForeignKey(User, blank=True, related_name='student_user', null=True, unique=True)

	def __unicode__(self):
		return self.name


class Class(models.Model):
	name = models.CharField(max_length=228)
	students = models.ManyToManyField(Student, related_name='students')
	parent_org = models.ForeignKey(Org, related_name='parent_org')
	associated_teacher = models.ForeignKey(User, blank=True, related_name='associated_teacher', null=True)
	year = models.DateField(auto_now = False, auto_now_add = False)


	def __unicode__(self):
		return self.name


