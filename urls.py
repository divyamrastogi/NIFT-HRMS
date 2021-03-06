from django.views.static import *
from django.views.generic.simple import redirect_to
from django.conf import settings

from views import profile, home,workload_details, leave_application, logout, edit_profile, teaching_hours, submit_teaching_hours, feedback_details, submit_leave, leave_extend, submit_extension_leave, mark_attendance, check_attendance, department_attendance, leave_approval,  leave_details,weeklyfeedbacklink, weekly_feedback, submit_feedback, edirectory_courses, edirectory_faculty, edirectory_info, course_info, faculty_info

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('views',
#harsha's urls....
     (r'^$',home),
     (r'^edit_profile/$', edit_profile),
     (r'^edit_profile/saved/$', redirect_to, {'url': ''}),
     (r'^leave_application/$',leave_application),
     (r'^logout/$',logout),
     url(r'^admin/', include(admin.site.urls)),
     (r'^([A-Za-z])/$',home),
#harsha's changes ..............
     (r'^mark_attendance/$',mark_attendance),
     (r'^leave_approval/$',leave_approval),
     (r'^leave_details/$',leave_details),
     (r'^weekly_feedback/$',weekly_feedback),
     (r'^weeklyfeedbacklink/$',weeklyfeedbacklink),
     (r'^teaching_hours/$',teaching_hours),
     (r'^submit_teaching_hours/$',submit_teaching_hours),
     (r'^feedback_details/$',feedback_details),
     (r'^workload_details/$',workload_details),
     (r'^submit_feedback/$',submit_feedback),
     (r'^check_attendance/$',check_attendance),
     (r'^department_attendance/$',department_attendance),
#divyam's url....
     (r'^submit_leave/$', submit_leave),
     (r'^leave_extension/$', leave_extend),
     (r'^leave_extend/$', submit_extension_leave),
     (r'^course/$', edirectory_courses),
     (r'^faculty/$', edirectory_faculty),
     (r'^edirectory_info/$', edirectory_info),
     (r'^course_info/$', course_info),
     (r'^faculty_info/$', faculty_info),
#divyam's changes .....................

     

)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )

