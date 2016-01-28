from django.contrib import admin

# Register your models here.

from .forms import SignUpForm
from .models import SignUp
#from .models import Organization
from .models import Org

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

class OrgadminInline(admin.TabularInline):
	model = Org.org_admins.through

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




admin.site.register(SignUp, SignUpAdmin)
#admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Org, OrgAdmin)