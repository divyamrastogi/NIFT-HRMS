from django.views.static import *
from django.views.generic.simple import redirect_to
from django.conf import settings
from views import profile, home, casual_leave, logout, edit_profile, submit_csleave, leave_extend, submit_extension_leave, mark_attendance, check_attendance, department_attendance,leave_approval
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('views',
#harsha's urls....
     (r'^$',home),
     (r'^edit_profile/$', edit_profile),
     (r'^edit_profile/saved/$', redirect_to, {'url': ''}),
     (r'^casual_leave/$',casual_leave),
     (r'^logout/$',logout),
     url(r'^admin/', include(admin.site.urls)),
     (r'^([A-Za-z])/$',home),
#harsha's changes ..............
     (r'^mark_attendance/$',mark_attendance),
     (r'^check_attendance/$',check_attendance),
     (r'^leave_approval/$', leave_approval),
     (r'^department_attendance/$',department_attendance),
#divyam's url....
     (r'^csleave/$', submit_csleave),
     (r'^leave_extension/$', leave_extend),
     (r'^extend_leave/$', submit_extension_leave),
#divyam's changes .....................

     

)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )

