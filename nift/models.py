from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
	SEX_CHOICES = (
		('M','Male'),
		('F','Female'),
	)

	STATUS_CHOICES = (
		('M','Married'),
		('U','Unmarried'),
	)

	user_id 	= models.OneToOneField(User, primary_key=True) 
        email 		= models.EmailField()
        sex        	= models.CharField(max_length=1, choices=SEX_CHOICES)
	dob 	   	= models.DateField()
	phone_no   	= models.CharField(max_length=15)
	marital_status  = models.CharField(max_length=1, choices=STATUS_CHOICES)
	street 		= models.CharField(max_length=200)
	zip_code 	= models.CharField(max_length=15)
	city 		= models.CharField(max_length=30)
	state 		= models.CharField(max_length=30)

	def __unicode__(self):
		return self.user_id.username

class Profile(models.Model):
	DESIGNATION_CHOICES = (
		(1,'Professor'),
		(2,'Assistant Professor'),
		(3,'Associate Professor'),
		(4,'Senior Professor'),
		(5,'Assistant'),
		(6,'Registrar'),
		(7,'Centre Coordinator'),
		(8,'Director General'),
		(9,'Director'),
	)
	
	CENTRE_CHOICES = (
                (1,'Bhopal'),
                (2,'Bhubaneshwar'),
                (3,'Bengaluru'),
                (4,'Delhi'),
                (5,'Kangra'),
                (6,'Chennai'),
                (7,'Kolkatta'),
                (8,'Mumbai'),
                (9,'Gandhinagar'),
                (10,'Raebareli'),
                (11,'Jodhpur'),
                (12,'Patna'),
                (13,'Hyderabad'),
                (14,'Shillong'),
                (15,'Kannur'),
        )

        DEPARTMENT_CHOICES = (
                (1,'Fashion Design'),
                (2,'Leather Design'),
                (3,'Accessory Design'),
                (4,'Textile Design'),
                (5,'Knitwear Design'),
                (6,'Fashion Communication'),
                (7,'Apparel Production'),
                (8,'Design Space'),
                (9,'Fashion Management'),
                (10,'Fashion Technology'),
        )
                      
	user_id         = models.ForeignKey(User, primary_key=True)
	join_date 	= models.DateField()
	designation 	= models.IntegerField(max_length = 1, choices=DESIGNATION_CHOICES)
	department 	= models.IntegerField(max_length= 2, choices=DEPARTMENT_CHOICES)
	centre 		= models.IntegerField(max_length= 2, choices=CENTRE_CHOICES)
	room_no 	= models.CharField(max_length=10)
	past_positions 	= models.CharField(max_length=150, blank=True)
	experience 	= models.IntegerField(null=True)
	expertise 	= models.CharField(max_length=150, blank=True)
	image 		= models.ImageField(upload_to='image/', null=True)

	def __unicode__(self):
		return self.user_id.user_id.username

class Attendance(models.Model):
	date 		= models.DateField(auto_now=True)
	present 	= models.BooleanField()
	user_id 	= models.ForeignKey(User)
	attendance_id 	= models.AutoField(primary_key=True)

        def __unicode__(self):
		return u'%s %s' % (self.user_id.user_id.username, self.date)

	class Meta:
		unique_together = ('date','user_id')

class Sem_Info(models.Model):
	TERM_CHOICES = (
		(1,'Winter'),
		(2,'Autumn'),
        )

	term 		= models.IntegerField(max_length=1, choices=TERM_CHOICES)
	year 		= models.IntegerField(max_length=4)
	sem_id 		= models.AutoField(primary_key=True)
	
	def __unicode__(self):
	        return self.term, self.year

	class Meta:
		unique_together = ('term','year')


class Course(models.Model):
	
	course_id 	= models.CharField(max_length=20, primary_key=True)
	course_name     = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.course_name

	class Meta:
		unique_together = ('course_id','course_name')

class Cen_Dep_Info(models.Model):
	CENTRE_CHOICES = (
		(1,'Bhopal'),
		(2,'Bhubaneshwar'),
		(3,'Bengaluru'),
		(4,'Delhi'),
		(5,'Kangra'),
		(6,'Chennai'),
		(7,'Kolkatta'),
		(8,'Mumbai'),
		(9,'Gandhinagar'),
		(10,'Raebareli'),
		(11,'Jodhpur'),
		(12,'Patna'),
		(13,'Hyderabad'),
		(14,'Shillong'),
		(15,'Kannur'),
	)

	DEPARTMENT_CHOICES = (
	        (1,'Fashion Design'),
	        (2,'Leather Design'),
	        (3,'Accessory Design'),
	        (4,'Textile Design'),
	        (5,'Knitwear Design'),
	        (6,'Fashion Communication'),
	        (7,'Apparel Production'),
	        (8,'Design Space'),
	        (9,'Fashion Management'),
		(10,'Fashion Technology'),
	)
	
	centre_name 	= models.IntegerField(max_length=2)
	department_name = models.IntegerField(max_length=2)
	cen_dep_id 	= models.AutoField(primary_key=True)

	def __unicode__(self):
	        return self.centre_name, self.department_name

	class Meta:
		unique_together = ('centre_name','department_name')

class Offered(models.Model):
	sem_id 		= models.ForeignKey(Sem_Info)
	course_id 	= models.ForeignKey(Course)
	cen_dep_id 	= models.ForeignKey(Cen_Dep_Info)
	user_id         = models.ForeignKey(User)
 	every_id        = models.AutoField(primary_key=True)

	def __unicode__(self):
		return self.user_id.user_id.username

	class Meta:
		unique_together = ('sem_id','course_id','cen_dep_id')

class Teaching(models.Model):
	STUDY_CHOICES = (
	       	('D','Direct'),
               	('I','InDirect'),
		('A','Audit'),
        )

	TYPE_CHOICES = (
		(1,'CoTeaching'),
		(2,'IndividualTeaching'),
		(3,'OtherCentre'),
		(4,'GP'),
		(5,'DC'),
		(6,'ResearchPaper'),
		(7,'ITP'),
		(8,'CraftCluster'),
	)

	study_type 	= models.CharField(max_length=1, choices=STUDY_CHOICES)
	detail_type 	= models.IntegerField(max_length=1, choices=TYPE_CHOICES, null=True)	
	hours 		= models.DecimalField(max_digits=5,decimal_places=2)
	every_id 	= models.ForeignKey(Offered)
	user_id 	= models.ForeignKey(User)
	teaching_id     = models.AutoField(primary_key=True)

	def __unicode__(self):
		return self.user_id.user_id.username

	class Meta:
		unique_together = ('study_type','detail_type','every_id','user_id')

class Feedback(models.Model):
	
	start_date	= models.DateField()
	end_date   	= models.DateField()
	avg_content_rat = models.DecimalField(max_digits=5,decimal_places=2,null=True)
	avg_present_rat = models.DecimalField(max_digits=5,decimal_places=2,null=True)
	every_id        = models.ForeignKey(Offered)
	feedback_id     = models.AutoField(primary_key=True)
	
	def __unicode__(self):
		return self.week_no, self.month

	class Meta:
		unique_together = ('start_date','end_date','every_id')

class Leave_Details(models.Model):

        LEAVE_CHOICES = (
                 (1,'Earned'),
                 (2,'Casual'),
                 (3,'Restricted'),
                 (4,'Hospital'),
                 (5,'Maternity'),
        )

        leave_type      = models.IntegerField(max_length=1, choices=LEAVE_CHOICES)
	user_id 	= models.ForeignKey(User)
	days_left 	= models.IntegerField()
	leave_d_id      = models.AutoField(primary_key=True)

	def __unicode__(self):
		return self.user_id.user_id.username

	class Meta:
		unique_together = ('leave_type','user_id')

class Leave_Info(models.Model):

	LEAVE_CHOICES = (
                 (1,'Earned'),
                 (2,'Casual'),
                 (3,'Restricted'),
                 (4,'Hospital'),
                 (5,'Maternity'),
        )
	STATUS = (
                 (1,'Rejected'),
                 (2,'Approved'),
                 (6,'pending by registrar'),
                 (7,'pending by cc'),
                 (9,'pending by director')
        )

        leave_type      = models.IntegerField(max_length=1, choices=LEAVE_CHOICES)
        start_date      = models.DateField()
        reason          = models.CharField(max_length=1000)
        no_of_days      = models.IntegerField()
        status          = models.IntegerField(max_length=1, choices=STATUS)
        user_id         = models.ForeignKey(User)
        applied_date    = models.DateField(auto_now=True)
        leave_id        = models.AutoField(primary_key=True)
        reject_reason   = models.CharField(max_length = 150, blank = True) 
        cc_date         = models.DateField(null = True)
        registrar_date  = models.DateField(null = True)
        director_date   = models.DateField(null = True)
 
	def __unicode__(self):
                return self.user_id.user_id.username

	class Meta:
		unique_together = ('start_date','leave_type','reason','user_id','applied_date')

class Leave_Extension_Info(models.Model):

	LEAVE_CHOICES = (
                 (1,'Earned'),
                 (2,'Casual'),
                 (3,'Restricted'),
                 (4,'Hospital'),
                 (5,'Maternity'),
        )
        STATUS = (
                 (1,'Rejected'),
                 (2,'Approved'),
                 (6,'pending by registrar'),
                 (7,'pending by cc'),
                 (9,'pending by director'),
        )

	last_leave_id   = models.OneToOneField(Leave_Info, primary_key=True)
        leave_type      = models.IntegerField(max_length=1, choices=LEAVE_CHOICES)
        reason          = models.CharField(max_length=1000)
        status          = models.IntegerField(max_length=1, choices=STATUS)
        no_of_days      = models.IntegerField()
        applied_date    = models.DateField(auto_now=True)
	user_id 	= models.ForeignKey(User)
	end_date	= models.DateField()
	start_date	= models.DateField()
        reject_reason = models.CharField(max_length = 150, blank = True) 
        cc_date         = models.DateField(null = True)
        registrar_date  = models.DateField(null = True)
        director_date   = models.DateField(null = True)
         
        def __unicode__(self):
                return self.last_leave_id.user_id.user_id.username
