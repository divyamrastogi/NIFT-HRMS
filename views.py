from django.template.defaultfilters import register
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.db.models import Avg, Sum
from django.contrib.auth import authenticate, models
from nift.models import User, Profile, Teaching, Leave_Info, Feedback, Attendance, Leave_Details, Leave_Extension_Info, Cen_Dep_Info, Offered, Course
#from nift.models import *
from datetime import date
import datetime
import math
import unicodedata


# divyam's methods..............

def edirectory_info(request):
    try:
        u = models.User.objects.get(username = request.session.get('user'))
        t = User.objects.get(user_id = u.id)
        p = Profile.objects.get(user_id = u.id)
	if(request.POST):
	    id = request.POST.get('user_id')
	    return HttpResponse("<html><header>This page is under construction</header></html>") 
	else:
	    render_to_response('error.html')
    except:
	return render_to_response('error.html')

def edirectory_courses(request):
    try:
	u = models.User.objects.get(username = request.session.get('user'))
	t = User.objects.get(user_id = u.id)
	p = Profile.objects.get(user_id = u.id)
	return render_to_response('edirectory_course.html', {'Error': False})
    except:
	return render_to_response('error.html')

def course_info(request):
    if(request.POST):
      try:
	courseid = request.POST.get('course_id')
	c = Offered.objects.filter(course_id=courseid)
	course = Course.objects.get(course_id=courseid)
	print c, course.course_name
        return render_to_response('course_info.html', locals())	
      except:
	return render_to_response('edirectory_course.html', {'Error': True})

def edirectory_faculty(request):
    try:
        u = models.User.objects.get(username = request.session.get('user'))
        t = User.objects.get(user_id = u.id)
        p = Profile.objects.get(user_id = u.id)
        return render_to_response('edirectory_faculty.html')
    except:
        return render_to_response('error.html')

def faculty_info(request):
        if(request.POST):
            try:	  
                fid = request.POST.get('user_id')
                u = models.User.objects.get(id = fid)
            except:
                return render_to_response('edirectory_faculty.html', {'Error' : True})
            try:    
		if 'Courses' in request.POST:
			c = Offered.objects.filter(user_id = fid)
			print 'c'
		elif 'Expertise' in request.POST:
			e = Profile.objects.filter(user_id = fid)
			print 'e'
		elif 'Teaching' in request.POST:
		    t = Teaching.objects.filter(user_id = fid)
		    print 't'
		return render_to_response('faculty_info.html', locals())
	    except:
	        return render_to_response('faculty_info.html', {'Error' : True})
	return HttpResponseRedirect('/')

def leave_application(request):
    try:
        u = models.User.objects.get(username = request.session.get('user'))
        t = User.objects.get(user_id = u.id)
        p = Profile.objects.get(user_id = u.id)
        return render_to_response('leave_application_form.html', locals())
    except Exception:
        return render_to_response('error.html',)

def weekly_feedback(request):
    return render_to_response('weekly_feedback.html',{'Error': False})
    
def teaching_hours(request):
    return render_to_response('teaching_hours.html',)
#except Exception:
 #       return render_to_response('error.html',)

def submit_teaching_hours(request):
    if (request.POST):
      t = models.User.objects.get(username = request.session.get('user'))
      u = User.objects.get(user_id = t.id)
      for i in ['1','2','3','4','5','6']:
	try:
		D_course_id = request.POST.get('d_course_id['+ i + ']')
		D_sem_id = request.POST.get('d_sem_id['+ i + ']')
		every_id = Offered.objects.get(user_id = u.user_id , course_id = D_course_id, sem_id = D_sem_id)
		D_1 = request.POST.get('D_1['+ i + ']')
		D_2 = request.POST.get('D_2['+ i + ']')
		D_3 = request.POST.get('D_3['+ i + ']')
		I_3 = request.POST.get('I_3['+ i + ']')
		a = Teaching(study_type = 'D', detail_type = 1, hours = D_1, every_id = every_id, user_id = u)
		b = Teaching(study_type = 'D', detail_type = 2, hours = D_2, every_id = every_id, user_id = u)
		c = Teaching(study_type = 'D', detail_type = 3, hours = D_3, every_id = every_id, user_id = u)
		d = Teaching(study_type = 'I', detail_type = 3, hours = I_3, every_id = every_id, user_id = u)
		I_course_id = request.POST.get('i_course_id['+ i + ']')
		I_sem = request.POST.get('i_sem_id['+ i + ']')
		every_id = Offered.objects.get(user_id = u.user_id , course_id = I_course_id, sem_id = I_sem )
		I_4 = request.POST.get('I_4['+ i + ']')
		I_5 = request.POST.get('I_5['+ i + ']')
		I_6 = request.POST.get('I_6['+ i + ']')
		I_7 = request.POST.get('I_7['+ i + ']')
		A = request.POST.get('A['+ i + ']')
		e = Teaching(study_type = 'I', detail_type = 4, hours = I_4, every_id = every_id, user_id = u)       
		f = Teaching(study_type = 'I', detail_type = 5, hours = I_5, every_id = every_id, user_id = u)       
		g = Teaching(study_type = 'I', detail_type = 6, hours = I_4, every_id = every_id, user_id = u)       
		h = Teaching(study_type = 'I', detail_type = 7, hours = I_4, every_id = every_id, user_id = u)       
		i = Teaching(study_type = 'A', hours = A, every_id = every_id, user_id = u)       
		a.save()
		b.save()
		c.save()
		d.save()
		e.save()
		f.save()
		g.save()
		h.save()
		i.save()
        except Exception:
	        return render_to_response('teaching_hours.html', {'Error': True})   
    return HttpResponseRedirect('/')
 
 
def submit_feedback(request):
    if (request.POST):
        print "enter try      "
        try:  
            for i in [1,2,3,4,5]:
	        print "entered for"
                date = request.POST.get('date_'+str(i))
                faculty_id = request.POST.get('faculty['+str(i)+']')
                course_id  = request.POST.get('course_id['+str(i)+']')
                sem_id  = request.POST.get('sem_id['+str(i)+']')
                every_id = Offered.objects.filter(user_id = faculty_id ).filter(course_id = course_id).filter(sem_id = sem_id)
                content_rate = request.POST.get('content_rate['+str(i)+']')
                present_rate = request.POST.get('content_rate['+str(i)+']')
                print date, faculty_id, course_id, every_id, content_rate, present_rate, "_________"
                f = Feedback(date = date, content_rate = content_rate, present_rate = present_rate, every_id = every_id[0])
                f.save()
            return HttpResponseRedirect('/')
        except:
	    print 'RRRRRRRRRRR'
	    return render_to_response('weekly_feedback.html', {'Error': True})
    

def feedback_details(request):
    if (request.POST):
      try:
        t = models.User.objects.get(username = request.session.get('user'))
        u = User.objects.get(user_id = t.id)
        course_id  = request.POST.get('course_id')
        sem_id  = request.POST.get('sem_id')
        date  = request.POST.get('date')
        print u.user_id, course_id
        e  = Offered.objects.get(sem_id = sem_id, course_id = course_id)
      	print e.every_id
        t  = Feedback.objects.filter(every_id = e).filter(date = date).count()
        c1 = Feedback.objects.filter(every_id = e).filter(date = date).filter(content_rate = 1).count()
        c2 = Feedback.objects.filter(every_id = e).filter(date = date).filter(content_rate = 2).count()
        c3 = Feedback.objects.filter(every_id = e).filter(date = date).filter(content_rate = 3).count()
        c4 = Feedback.objects.filter(every_id = e).filter(date = date).filter(content_rate = 4).count()
        c5 = Feedback.objects.filter(every_id = e).filter(date = date).filter(content_rate = 5).count()
        p1 = Feedback.objects.filter(every_id = e).filter(date = date).filter(present_rate = 1).count()
        p2 = Feedback.objects.filter(every_id = e).filter(date = date).filter(present_rate = 2).count()
        p3 = Feedback.objects.filter(every_id = e).filter(date = date).filter(present_rate = 3).count()
        p4 = Feedback.objects.filter(every_id = e).filter(date = date).filter(present_rate = 4).count()
        p5 = Feedback.objects.filter(every_id = e).filter(date = date).filter(present_rate = 5).count()
        print t
        return render_to_response('feedback_details.html',locals())
      except:
	return render_to_response('feedback_details.html', {'Error': True})
    return HttpResponseRedirect('/')
     

def workload_details(request):
    if (request.POST):
        try:
	  t = models.User.objects.get(username = request.session.get('user'))
	  u = User.objects.get(user_id = t.id)
	  course_id  = request.POST.get('course_id')
	  sem_id  = request.POST.get('sem_id')
	  print u.user_id, course_id
	  e  = Offered.objects.filter(user_id = u.user_id, course_id = course_id, sem_id = sem_id)
	  print e[0].every_id
	  direct = Teaching.objects.filter(every_id = e[0]).filter(study_type = 'D').aggregate(Sum('hours'))
	  indirect = Teaching.objects.filter(every_id = e[0]).filter(study_type = 'I').aggregate(Sum('hours'))
	  audit = Teaching.objects.filter(every_id = e[0]).filter(study_type = 'A').aggregate(Sum('hours'))
	  print direct , indirect, audit
          return render_to_response('workload_details.html',locals())
        except:
	  return render_to_response('workload_details.html', {'Error': True})
    return HttpResponseRedirect('/')
          
       

def submit_extension_leave(request):
    if (request.POST):
	u = models.User.objects.get(username = request.session.get('user'))
        LeaveType = request.POST.get('leave_type')
        Reason = request.POST.get('reason')
        StartDate = request.POST.get('start_date')
        EndDate = request.POST.get('end_date')
	last_leave_type = request.POST.get('last_leave_type')
	lid = Leave_Info.objects.filter(user_id=u.id, start_date=StartDate)
        Today=datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')
        Start = datetime.datetime.strptime(StartDate,'%Y-%m-%d')
        End = datetime.datetime.strptime(EndDate, '%Y-%m-%d')
	if not lid:
            return render_to_response('leave_extension_form.html', {'Error': True})
            #return HttpResponse("<html>Sorry. A leave with a start date that you have entered does not already exist. <br>Enter the date from which your leave starts to extend your leave.</html>")
        Diff = End - Start
        No_of_days = Diff.days+1
        Buffer= Start - Today
        Buffer_days = Buffer.days
        No_of_days = Diff.days + 1
        Extend_by = No_of_days - lid[0].no_of_days
	To_end = End - Today
	Days_to_end = To_end.days
	if Days_to_end < 0:
	    return render_to_response('leave_extension_form.html', {'Error1': True})
	    #return HttpResponse("<html>Your End Date has already passed. You cannot extend any such leave.</html>")
	if Extend_by < 1:
            return render_to_response('leave_extension_form.html', {'Error2': True})
	    #return HttpResponse("<html>You have to enter a date which is after your previously sanctioned leave end date.</html>")
	if Buffer_days < 0:
            return render_to_response('leave_extension_form.html', {'Error3': True})
	    #return HttpResponse("<html>Your start date should be at least today's date.</html>")
	if(No_of_days < 1):
            return render_to_response('leave_extension_form.html', {'Error4': True})
	    #return HttpResponse("<html>You have entered invalid end date. <br>The end date cannot be before the start date.<br> You can go back by clicking the back button on your browser. </html>")
	elif No_of_days > 6:
	    Extra = math.floor(No_of_days/7)
	    No_of_days -= 2*Extra
	print 'Extending the leave by ', No_of_days, 'days.'
        #l=Leave_Extension_Info(leave_type=LeaveType, start_date=StartDate, last_leave_id=lid[0], reason=Reason, no_of_days=Extend_by, status='7', applied_date=Today)

        l=Leave_Extension_Info(leave_type=LeaveType, user_id_id=u.id, start_date=StartDate, end_date=EndDate, last_leave_id=lid[0], reason=Reason, no_of_days=Extend_by, status=7, applied_date=Today)
        l.save()
	#m=Leave_Info.objects.get(leave_id=lid[0].leave_id)
	#m.no_of_days=No_of_days
	#m.status='9'
	#m.save()
	return HttpResponseRedirect('/')
    else:
        return render_to_response('error.html',)

def leave_details(request):
    u = models.User.objects.get(username = request.session.get('user'))
    t = User.objects.get(user_id = u.id)
    p = Profile.objects.get(user_id = u.id)
    if (request.POST):
        try:
            leave_type = request.POST.get('leave')    
            start_date = request.POST.get('date')    
            print start_date, leave_type
            details = Leave_Info.objects.filter(user_id = u.id).filter( leave_type= leave_type).filter( start_date__gte= start_date)
            return render_to_response('leave_details.html', locals() )
        except Exception:
            return HttpResponse("<html>no such leave has been approved</html>")
    return HttpResponseRedirect('/')


def leave_extend(request):
    try:
        u = models.User.objects.get(username = request.session.get('user'))
        t = User.objects.get(user_id = u.id)
        p = Profile.objects.get(user_id = u.id)
        return render_to_response('leave_extension_form.html', locals())
    except Exception:
        return render_to_response('error.html',)


def submit_leave(request):
    if (request.POST):
        u = models.User.objects.get(username = request.session.get('user'))
        LeaveType = request.POST.get('leave_type')
        Reason = request.POST.get('reason')
        Permission = request.POST.get('permission')
        #Address = request.POST.get('address')
	StartDate = request.POST.get('start_date')
	EndDate = request.POST.get('end_date')
	Today=datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d') 
	Start = datetime.datetime.strptime(StartDate,'%Y-%m-%d')
	End = datetime.datetime.strptime(EndDate, '%Y-%m-%d')
	Diff = End - Start
	No_of_days = Diff.days+1
	leave = Leave_Info.objects.filter(user_id=u.id, start_date=StartDate)
	Buffer= Start - Today
	Buffer_days = Buffer.days
	print "No. of days: ", Buffer_days
	if Buffer_days < 15 and LeaveType=='1':
	    return render_to_response('leave_application_form.html', {'Error1': True})
	if Buffer_days < 0:
            return render_to_response('leave_application_form.html', {'Error2': True})
	if leave:
            return render_to_response('leave_application_form.html', {'Error3': True})
	if(No_of_days < 1):
            return render_to_response('leave_application_form.html', {'Error4': True})
	elif(No_of_days > 7):
	    Extra = math.floor(No_of_days/7)
	    No_of_days = No_of_days - 2*Extra
	#elif(No_of_days > 2):
	    #if(End.Weekday() = 0):
	        #No_of_days = No_of_days - 2
        	#print 'The number of days is: ', No_of_days
	    
	#Days_Left=	
	l=Leave_Info(leave_type=1, start_date=StartDate, reason=Reason, status = 7, no_of_days=No_of_days, user_id_id=u.id, applied_date=Today)
        l.save()
	#ld=Leave_Details.objects.get(user_id=u.id, leave_type=LeaveType)
	#ld.days_left = ld.days_left - No_of_days
	#ld.save()
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
		extendedLeaveApps = Leave_Extension_Info.objects.filter(user_id = u.id)#.filter(end_date__lte = datetime.datetime.now().date)
                ids = Profile.objects.filter(department = p.department)
                leave_data = Leave_Details.objects.filter(user_id = u.id)
                try:                
                    leaves = Leave_Info.objects.filter(status = p.designation)               
                    extended_leaves = Leave_Extension_Info.objects.filter(status = p.designation)
 
                except Exception:                     
                    print leaves, extended_leaves
                try:                
                    attendance = Attendance.objects.get(user_id = u.id , date=datetime.datetime.now().date())                    
                    print attendance
                    if attendance is not None:
                        todays_attendance = False
                except Exception:                     
                    todays_attendance = True
                print "__!!!!!!!!!__", todays_attendance
                return render_to_response('home.html', locals() )
            except Exception:
                return render_to_response('error.html',)
        else:
            return render_to_response('login.html' , {'error': True})
    elif (request.session.get('user') is not None):
#       try:
        u = models.User.objects.get(username = request.session.get('user'))
        t = User.objects.get(user_id = u.id)
        p = Profile.objects.get(user_id = u.id)
        myLeaveApplications = Leave_Info.objects.filter(user_id = u.id).filter(start_date__gte = datetime.datetime.now().date)
        extendedLeaveApps = Leave_Extension_Info.objects.filter(user_id = u.id)#.filter(end_date__lte = datetime.datetime.now().date)
        ids = Profile.objects.filter(department = p.department)
        leaves = Leave_Info.objects.filter(status = p.designation)                
        extended_leaves = Leave_Extension_Info.objects.filter(status = p.designation)
        leave_data = Leave_Details.objects.filter(user_id = u.id)
        try: 
            leaves = Leave_Info.objects.filter(status = p.designation)              
	    extended_leaves = Leave_Extension_Info.objects.filter(status = p.designation)      
        except Exception:                     
            print "no leaves", leaves
        try:                
            attendance = Attendance.objects.get(user_id = u.id , date=datetime.datetime.now().date())
            print attendance
            if attendance is not None:
                todays_attendance = False
        except Exception:                     
           todays_attendance = True
        return render_to_response('home.html', locals() )
    return render_to_response('login.html',)

def mark_attendance(request):
    u = models.User.objects.get(username = request.session.get('user'))
    t = User.objects.get(user_id = u.id)
    p = Profile.objects.get(user_id = u.id)
    if (request.POST):
        present = []
        present = request.POST.getlist('Present')
        on_duty = request.POST.getlist('on_duty')    
        ids = Profile.objects.filter(department = p.department)
        for i in ids:
            if i.user_id.user_id.username in present:
                a = Attendance(date=datetime.datetime.now().date(), present = True,user_id_id = i.user_id.user_id.id, on_duty = False, status = 1)        
            else:
	        if i.user_id.user_id.username in on_duty:
                    a = Attendance(date=datetime.datetime.now().date(), present = False,user_id_id = i.user_id.user_id.id,on_duty = True, status = 1)
		else:
		    a = Attendance(date=datetime.datetime.now().date(), present = False,user_id_id = i.user_id.user_id.id,on_duty = False, status = 1)                      
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
            if p.designation == 7:
                i.cc_date = datetime.datetime.now().date() 
            elif p.designation == 6: 
                i.registrar_date = datetime.datetime.now().date() 
            elif p.designation == 9: 
                i.director_date = datetime.datetime.now().date() 
            if i.user_id.user_id.username in approved:
	        if p.designation == 7:
                    i.status = 6
                elif p.designation == 6: 
                    i.status = 9
                elif p.designation == 9: 
                    i.status = 2
            else:
                i.status = 1
                i.reject_reason = request.POST.get('reason')
            i.save()
	eids = Leave_Extension_Info.objects.filter(status = p.designation)
	for e in eids:
	    print e
	    if p.designation == 7:
                e.cc_date = datetime.datetime.now().date() 
            elif p.designation == 6: 
                e.registrar_date = datetime.datetime.now().date() 
            elif p.designation == 9: 
                e.director_date = datetime.datetime.now().date() 
	    if e.user_id.user_id.username in approved:
	        if p.designation == 7:
                    i.status = 6
                elif p.designation == 6: 
                    i.status = 9
                elif p.designation == 9: 
                    i.status = 2
            else:
                e.status = 1
                e.reject_reason = request.POST.get('reason')
            e.save()

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
'''        try:
            start = datetime.strptime( start_date,'%Y-%m-%d')
            end = datetime.strptime( end_date,'%Y-%m-%d')
        except:
	    return HttpResponseRedirect("/")    '''
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

