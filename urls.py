from django.views.static import *
from django.views.generic.simple import redirect_to
from django.conf import settings
from views import *
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
     (r'^$',home),
     (r'^home/$',home),
     (r'^profile/$',profile),
     (r'^edit_profile/$', edit_profile),
     (r'^edit_profile/saved/$', redirect_to, {'url': ''}),
     (r'^casual_leave/$',casual_leave),
     (r'^logout/$',logout),
     (r'^time/plus/(\d{1,2})/$', hours_ahead),
     (r'^media/(?P<path>.*)$', 'django.views.static.serve',       
                  {'document_root': settings.MEDIA_ROOT}),
     url(r'^display/$',display_meta),
     url(r'^admin/', include(admin.site.urls)),
     (r'^([A-Za-z])/$',home),
     (r'^csleave/$', submit_csleave),
     (r'^leave_extension/$', leave_extend),
     (r'^extend_leave/$', submit_extension_leave),
     #(r'^search-form/$',views.search_form),
     #(r'^search/$',views.search),
     # Examples:
     # url(r'^$', 'mysite.views.home', name='home'),
     # url(r'^mysite/', include('mysite.foo.urls')),

     # Uncomment the admin/doc line below to enable admin documentation:
     #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     #url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )

