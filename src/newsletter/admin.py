from django.contrib import admin

# Register your models here.

from .forms import SignUpForm
from .models import SignUp
#from .models import Organization
from .models import Org
from .models import Student


class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = SignUpForm
	# class Meta:
	# 	model = SignUp

"""
class OrganizationAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
"""

class MembershipInline(admin.TabularInline):
    model = Org.members.through
    verbose_name = "member"
    verbose_name_plural = "members"



class OrgadminInline(admin.TabularInline):
    model = Org.org_admins.through
    verbose_name = "admin"
    verbose_name_plural = "admins"
    #verbose_name = "admin"
    #verbose_name_plural = "admins"

"""
class PersonAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
"""

class OrgAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
        OrgadminInline,
    ]
    exclude = ('members','org_admins',)

class StudentAdmin(admin.ModelAdmin):
    """docstring for StudentAdmin"""
    list_display = ["__unicode__"]
    exclude = ('users',)

        


admin.site.register(SignUp, SignUpAdmin)
#admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Org, OrgAdmin)
admin.site.register(Student, StudentAdmin)