from django.template.defaultfilters import register
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, models
from nift.models import User, Profile, Leave_Info, Attendance, Leave_Details
from datetime import date
import datetime
import unicodedata

# divyam's methods..............

def casual_leave(request):
    try:
        u = models.User.objects.get(username = request.session.get('user'))
        t = User.objects.get(user_id = u.id)
        p = Profile.objects.get(user_id = u.id)
        return render_to_response('leave_application_form.html', locals())
    except Exception:
        return render_to_response('error.html',)

def submit_extension_leave(request):
    try:
        u = models.User.objects.get(username = request.session.get('user'))
        t = User.objects.get(user_id = u.id)
        p = Profile.objects.get(user_id = u.id)
        return render_to_response('casual_leave.html', locals())
    except Exception:
        return render_to_response('error.html',)



def leave_extend(request):
    try:
        u = models.User.objects.get(username = request.session.get('user'))
        t = User.objects.get(user_id = u.id)
        p = Profile.objects.get(user_id = u.id)
        return render_to_response('leave_extension_form.html', locals())
    except Exception:
        return render_to_response('error.html',)


def submit_csleave(request):
    if (request.POST):
        u = models.User.objects.get(username = request.session.get('user'))
        LeaveType = request.POST.get('leave_type')
        Reason = request.POST.get('reason')
        Permission = request.POST.get('permission')
        #Address = request.POST.get('address')
	StartDate = request.POST.get('start_date')
	EndDate = request.POST.get('end_date')
	Today = datetime.datetime.now().strftime('%Y-%m-%d') 
	Start = datetime.datetime.strptime(StartDate,'%Y-%m-%d')
	End = datetime.datetime.strptime(EndDate, '%Y-%m-%d')
	Diff = End - Start
	No_of_days = Diff.days+1
	if(No_of_days < 0):
	    return HttpResponse("<html> You have entered an invalid end date.<br> Please try again by clicking the back button</html>")
	elif(No_of_days > 7):
	    Extra = No_of_days % 7
	    No_of_days = No_of_days - Extra
	#elif(No_of_days > 2):
	    #if(End.Weekday() = 0):
	        #No_of_days = No_of_days - 2
        	#print 'The number of days is: ', No_of_days
	    
	#Days_Left=	
	l=Leave_Info(leave_type=1, start_date=StartDate, reason=Reason, status = '9', no_of_days=No_of_days, user_id_id=u.id, applied_date=Today)
        l.save()
	return HttpResponseRedirect('/')
    else:
        return render_to_response('error.html')


#divyam's changes ......................




#harsha's methods ...............................
def profile(request):
    try:
        u = models.User.objects.get(username = request.session.get('user'))
        t = User.objects.get(user_id = u.id)
        p = Profile.objects.get(user_id = u.id)
        return render_to_response('profile.html', locals())
    except Exception:
        return render_to_response('error.html',)


def edit_profile(request):
    u = models.User.objects.get(username = request.session.get('user'))
    t = User.objects.get(user_id = u.id)
    p = Profile.objects.get(user_id = u.id)
    error = False
    if (request.POST):
            u = models.User.objects.get(username = request.session.get('user'))
            t = User.objects.get(user_id = u.id)
            p = Profile.objects.get(user_id = u.id)
            p.designation = request.POST.get('designation')
            p.department = request.POST.get('department')
            try:
                p.image = request.FILES['image']
            except Exception:
                p.image
            t.email = request.POST.get('email')
            t.sex = request.POST.get('sex')
            t.dob = request.POST.get('dob')
            t.phone_no = request.POST.get('phone_no')
            t.marital_status = request.POST.get('marital_status')
            t.city = request.POST.get('city') 
            t.street = request.POST.get('street') 
            t.state = request.POST.get('state')
            t.zip_code = request.POST.get('zip_code')
            t.save()
            p.save()
            return HttpResponseRedirect('/')
    else:
        return render_to_response('profile_form.html',locals() )

def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return HttpResponseRedirect("/")

# harsha's changes. ................................

def home(request):
    todays_attendance = True
    if (request.POST):
        user = authenticate(username = request.POST.get('username'), password = request.POST.get('password') )
        if user is not None:
            request.session['user'] = request.POST.get('username')
            request.session.set_expiry(0)
            try:
                u = models.User.objects.get(username = request.session.get('user'))
                t = User.objects.get(user_id = u.id)
                p = Profile.objects.get(user_id = u.id)
                myLeaveApplications = Leave_Info.objects.filter(user_id = u.id).filter(start_date__gte = datetime.datetime.now().date)
                ids = Profile.objects.filter(department = p.department)
                leaves = Leave_Info.objects.filter(status = p.designation)                
                leave_data = Leave_Details.objects.filter(user_id = u.id)
                try:                
                    leaves = Leave_Info.objects.filter(status = p.designation)                
                    print leaves
                    attendance = Attendance.objects.get(user_id = u.id , date=datetime.datetime.now().date())                    
                    if attendance is not None:
                        todays_attendance = False
                except Exception:                     
                    todays_attendance = True
                print "__!!!!!!!!!__", todays_attendance
                return render_to_response('home.html', locals() )
            except Exception:
                return render_to_response('error.html',)
        else:
            return render_to_response('login.html', {'error': True})
    elif (request.session.get('user') is not None):
#       try:
       u = models.User.objects.get(username = request.session.get('user'))
       t = User.objects.get(user_id = u.id)
       p = Profile.objects.get(user_id = u.id)
       myLeaveApplications = Leave_Info.objects.filter(user_id = u.id).filter(start_date__gte = datetime.datetime.now().date)
       ids = Profile.objects.filter(department = p.department)
       leaves = Leave_Info.objects.filter(status = p.designation)                
       leave_data = Leave_Details.objects.filter(user_id = u.id)
    
       try:                
           leaves = Leave_Info.objects.filter(status = p.designation)                
           attendance = Attendance.objects.get(user_id = u.id , date=datetime.datetime.now().date())
           print attendance
           if attendance is not None:
               todays_attendance = False
       except Exception:                     
           todays_attendance = True
       print "_______", todays_attendance
       return render_to_response('home.html', locals() )
#       except Exception:
        #   return render_to_response('error.html',)
    return render_to_response('login.html',)

def mark_attendance(request):
    u = models.User.objects.get(username = request.session.get('user'))
    t = User.objects.get(user_id = u.id)
    p = Profile.objects.get(user_id = u.id)
    if (request.POST):
        present = []
        present = request.POST.getlist('Present')    
        ids = Profile.objects.filter(department = p.department)
        for i in ids:
            if i.user_id.user_id.username in present:
                a = Attendance(date=datetime.datetime.now().date(), present = True,user_id_id = i.user_id.user_id.id)        
            else:
                a = Attendance(date=datetime.datetime.now().date(), present = False,user_id_id = i.user_id.user_id.id)                      
            a.save()
    return HttpResponseRedirect("/")

def leave_approval(request):
    u = models.User.objects.get(username = request.session.get('user'))
    t = User.objects.get(user_id = u.id)
    p = Profile.objects.get(user_id = u.id)
    if (request.POST):
        approved = []
        approved = request.POST.getlist('Approved')    
        print approved
        ids = Leave_Info.objects.filter(status = p.designation)
        for i in ids:
            print i
            if i.user_id.user_id.username in approved:
                if p.designation == '7':
                    i.status = 2
                else: 
                    i.status = '7'
            else:
                i.status = '1'
            i.save()
    return HttpResponseRedirect("/")

def check_attendance(request):
    u = models.User.objects.get(username = request.session.get('user'))
    t = User.objects.get(user_id = u.id)
    p = Profile.objects.get(user_id = u.id)
    if (request.POST):
        start_date = request.POST.get('start_date')    
        end_date = request.POST.get('end_date')    
        dates = Attendance.objects.filter( date__gte= start_date).filter( date__lte= end_date).filter(user_id = u.id)
        check_attendance = True
    return render_to_response('attendance.html', locals() )

def department_attendance(request):
    if (request.POST):
        dept = request.POST.get('department')
        start_date = request.POST.get('start_date')    
        end_date = request.POST.get('end_date')    
        ids = Profile.objects.filter(department = dept)
        dates = []
        for i in ids:     
             dates.append( Attendance.objects.filter( date__lte = end_date).filter( date__gte= start_date).filter(user_id = i.user_id))
    return render_to_response('department_attendance.html', locals() )
'''
        for i in ids:
            u = models.User.objects.get(id = i.user_id_id)
            t = User.objects.get(user_id = u.id)
            if u.username in present:
                a = Attendance(date=datetime.datetime.now().date(), present = True,user_id_id = u.id)        
            else:
                a = Attendance(date=datetime.datetime.now().date(), present = False,user_id_id = u.id)                      
            a.save()
'''

