from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'socialsitetemplate.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^user-dash', 'newsletter.views.userDash', name='user-dash'),
    #url(r'^org/(?P<orgid>[-w]+)/$', 'newsletter.views.orgView', name='org-view'),
    url(r'^org/(?P<id>[\w{}.-]{1,40})/$', 'newsletter.views.orgView', name='org-view'),
    #/(?P<id>[\w{}.-]{1,40})/$
    #url(r'^org/', 'newsletter.views.orgView', name='org-view'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)