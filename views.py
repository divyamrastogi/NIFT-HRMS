from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, models
from nift.models import User, Profile, Leave_Info
from datetime import date
import datetime
import unicodedata

def profile(request):
    try:
        u = models.User.objects.get(username = request.session.get('user'))
        t = User.objects.get(user_id = u.id)
        p = Profile.objects.get(user_id = u.id)
        return render_to_response('profile.html', locals())
    except Exception:
        return render_to_response('error.html',)

def casual_leave(request):
    try:
        u = models.User.objects.get(username = request.session.get('user'))
        t = User.objects.get(user_id = u.id)
        p = Profile.objects.get(user_id = u.id)
        return render_to_response('casual_leave.html', locals())
    except Exception:
        return render_to_response('error.html',)

def submit_extension_leave(request):
    if (request.POST):
        u = models.User.objects.get(username = request.session.get('user'))
	Name = request.POST.get('Name')
	Designation = request.POST.get('Designation')
	Department = request.POST.get('Department')
	Phone = request.POST.get('Phone')
	BasicPay = request.POST.get('BasicPay')
	Allowance = request.POST.get('Allowance')
        LeaveType = request.POST.get('LeaveType')
	Reason = request.POST.get('Reason')	
	StartDate = request.POST.get('StartDate')
	EndDate = request.POST.get('EndDate')
        PrefixSuffix = request.POST.get('PrefixSuffix')
	LeaveGround = request.POST.get('LeaveGround')
	LStart = request.POST.get('LStart')
	LEnd = request.POST.get('LEnd')
	LeaveNature = request.POST.get('LeaveNature')
	LTCBlock = request.POST.get('LTCBlock')
	CommitmentsDescription = request.POST.get('CommitmentsDescription')
        ApplicationDate = request.POST.get('ApplicationDate')
        Iagree = request.POST.get('Iagree')
        Address = request.POST.get('Address')
	End = datetime.datetime.strptime(EndDate,'%Y-%m-%d') 
	Start = datetime.datetime.strptime(StartDate,'%Y-%m-%d')
	Diff = End - Start
	No_of_days = Diff.days
	

	return HttpResponseRedirect('/')
    else:
        return render_to_response('error.html')


def leave_extend(request):
    try:
        u = models.User.objects.get(username = request.session.get('user'))
        t = User.objects.get(user_id = u.id)
        p = Profile.objects.get(user_id = u.id)
        return render_to_response('extension_of_leave.html', locals())
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



def home(request):
    if (request.POST):
        user = authenticate(username = request.POST.get('username'), password = request.POST.get('password') )
        if user is not None:
            request.session['user'] = request.POST.get('username')
            request.session.set_expiry(0)
            try:
                u = models.User.objects.get(username = request.session.get('user'))
                t = User.objects.get(user_id = u.id)
                p = Profile.objects.get(user_id = u.id)
                return render_to_response('home.html', locals() )
            except Exception:
                return render_to_response('error.html',)

        
        else:
            return render_to_response('login.html', {'error': True})
    elif (request.session.get('user') is not None):
        u = models.User.objects.get(username = request.session.get('user'))
        t = User.objects.get(user_id = u.id)
        p = Profile.objects.get(user_id = u.id)
        return render_to_response('home.html', locals() )
    return render_to_response('login.html',)
    
def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return HttpResponseRedirect("/")



def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def submit_csleave(request):
    if (request.POST):
        u = models.User.objects.get(username = request.session.get('user'))
        LeaveType = request.POST.get('leave')
        Reason = request.POST.get('Reason')
        Permission = request.POST.get('permission')
        Address = request.POST.get('Address')
	StartDate = request.POST.get('StartDate')
	EndDate = request.POST.get('EndDate')
	End = datetime.datetime.strptime(EndDate,'%Y-%m-%d') 
	Start = datetime.datetime.strptime(StartDate,'%Y-%m-%d')
	Diff = End - Start
	No_of_days = Diff.days
	#Days_Left=	
	l=Leave_Info(leave_type=1, start_date=StartDate, reason=Reason, no_of_days=No_of_days, days_left=2, approved='false', user_id_id=u.id, leave_id=1)
        l.save()
	return HttpResponseRedirect('/')
    else:
        return render_to_response('error.html')

