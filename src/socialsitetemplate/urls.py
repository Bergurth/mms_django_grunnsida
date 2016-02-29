from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'organizations.views.home', name='home'),
    url(r'^contact/$', 'organizations.views.contact', name='contact'),
    url(r'^about/$', 'socialsitetemplate.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^user-dash', 'organizations.views.userDash', name='user-dash'),
    #url(r'^org/(?P<orgid>[-w]+)/$', 'organizations.views.orgView', name='org-view'),

    url(r'^org/$', 'organizations.views.orgs', name='orgs-view'),
    url(r'^org/(?P<id>[\w{}.-]{1,40})/$', 'organizations.views.orgView', name='org-view'),
    #/(?P<id>[\w{}.-]{1,40})/$
    #url(r'^org/', 'organizations.views.orgView', name='org-view'),

    # org edit
    url(r'^org-edit/(?P<id>[\w{}.-]{1,40})/$', 'organizations.views.orgEdit', name='org-edit'),
    # for creating new orgs.
    url(r'^org-edit/$','organizations.views.orgEdit', name='org-edit'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)