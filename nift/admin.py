from django.contrib import admin, auth
from nift.models import Course,  User, Profile, Attendance, Sem_Info, Course, Cen_Dep_Info, Offered, Teaching, Feedback, Leave_Info, Leave_Extension_Info


admin.site.register(User)
admin.site.register(Course)
admin.site.register(Profile)
admin.site.register(Attendance)
admin.site.register(Sem_Info)
admin.site.register(Cen_Dep_Info)
admin.site.register(Offered)
admin.site.register(Teaching)
admin.site.register(Feedback)
admin.site.register(Leave_Info)
admin.site.register(Leave_Extension_Info)

