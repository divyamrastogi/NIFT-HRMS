from django.db import models

'''
class User(models.Model):

	first_name 	= models.CharField(max_length=100)
	last_name  	= models.CharField(max_length=100)
	login_name 	= models.CharField(max_length=100, unique=True) 

	password   	= models.CharField(max_length=100)
	email_add  	= models.EmailField(max_length=100)

	phone_no   	= models.SmallIntegerField()

'''

class Profile(models.Model):
	DESIGNATION_CHOICES = (
		('1','Professor'),
		('2','Assistant Professor'),
		('3','Associate Professor'),
		('4','Senior Professor'),
		('5','Director'),
		('6','Assistant'),
		('7','Centre Coordinator'),
		('8','Director General'),
	)
	SEX_CHOICES = (
		('M','Male'),
		('F','Female'),
	)

	STATUS_CHOICES = (
		('M','Married'),
		('U','Unmarried'),
	)
	join_date 	= models.DateField()
	designation 	= models.CharField(max_length=1, choices=DESIGNATION_CHOICES)
	basic_pay 	= models.IntegerField()
#	department 	= models.CharField(max_length..........)
#	centre 		= models.CharField(max_length.........)
	dob 	   	= models.DateField()
	marital_status  = models.CharField(max_length=1, choices=STATUS_CHOICES)
	room_no 	= models.CharField(max_length=10)
	past_positions 	= models.CharField(max_length=150)
	experience 	= models.SmallIntegerField()
      	sex        	= models.CharField(max_length=1, choices=SEX_CHOICES)
	expertise 	= models.CharField(max_length=150)
#	user_id       	= models.ForeignKey(Auth_User.id)
#	image 		= models.ImageField(upload_to='images/%Y/%m/%d')

class Attendance(models.Model):
	date 		= models.DateField(auto_now=True)
	present 	= models.BooleanField()
	user_id 	= models.ForeignKey(Profile)
	user_id.primary_key = True

class Address(models.Model):
	user_id         = models.ForeignKey(Profile, primary_key=True)
	perm_street 	= models.CharField(max_length=200)
	perm_zip 	= models.SmallIntegerField()
	perm_state 	= models.CharField(max_length=50)
	temp_street     = models.CharField(max_length=200)                                  
	temp_zip        = models.SmallIntegerField()
        temp_state  	= models.CharField(max_length=50)

class Sem_Info(models.Model):
	TERM_CHOICES = (
		('1','Winter'),
		('2','Autumn'),
        )

	term 		= models.CharField(max_length=1, choices=TERM_CHOICES)
	year 		= models.CharField(max_length=4)
	sem_id 		= models.AutoField(primary_key=True)

class Course(models.Model):
	course_name 	= models.CharField(max_length=50)
	course_id 	= models.CharField(max_length=20, primary_key=True)

class Cen_Dep_Info(models.Model):
	centre_name 	= models.CharField(max_length=50)
	department_name = models.CharField(max_length=50)
	cen_dep_info 	= models.AutoField(primary_key=True)

class Offered(models.Model):
	sem_id 		= models.ForeignKey(Sem_Info)
	course_id 	= models.ForeignKey(Course)
	cen_dep_info 	= models.ForeignKey(Cen_Dep_Info)
	every_info 	= models.AutoField(primary_key=True)
	user_id         = models.ForeignKey(Profile)

class Teaching(models.Model):
	STUDY_CHOICES = (
	       	('D','Direct'),
               	('I','InDirect'),
		('A','Audit'),
        )

	TYPE_CHOICES = (
		('1','CoTeaching'),
		('2','IndividualTeaching'),
		('3','OtherCentre'),
		('4','GP'),
		('5','DC'),
		('6','ResearchPaper'),
		('7','ITP'),
		('8','CraftCluster'),
	)

	study_type 	= models.CharField(max_length=1, choices=STUDY_CHOICES)
	detail_type 	= models.CharField(max_length=1, choices=TYPE_CHOICES)
	teaching_id 	= models.AutoField(primary_key=True)
	hours 		= models.SmallIntegerField()
	every_info 	= models.ForeignKey(Offered)

class Feedback(models.Model):
	WEEK_CHOICES = (
		('1','First'),
		('2','Second'),
		('3','Third'),
		('4','Forth'),
	)

	week_no 	= models.CharField(max_length=1, choices=WEEK_CHOICES)
	avg_content_rat = models.SmallIntegerField()
	avg_present_rat = models.SmallIntegerField()
	feedback_id 	= models.AutoField(primary_key=True)
	every_info      = models.ForeignKey(Offered)

class Leave_Info(models.Model):
	LEAVE_CHOICES = (
		('1','Earned'),
		('2','Casual'),
		('3','Restricted'),
		('4','Hospital'),
		('5','Maternity'),
	)

	leave_type 	= models.CharField(max_length=1, choices=LEAVE_CHOICES)
	start_date 	= models.DateField()
	reason 		= models.CharField(max_length=1000)
	no_of_days 	= models.SmallIntegerField()
	approved 	= models.BooleanField()
	days_left 	= models.SmallIntegerField()
	user_id 	= models.ForeignKey(Profile)
	leave_id 	= models.AutoField(primary_key=True)

class Leave_Extension_Info(models.Model):
	last_leave_id 	= models.ForeignKey(Leave_Info)
	reason 		= models.CharField(max_length=1000)
	approved 	= models.BooleanField()
	eleave_id 	= models.AutoField(primary_key=True)


