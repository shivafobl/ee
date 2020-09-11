from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class EeeStudentRegister(models.Model):



	user=models.ForeignKey(User,on_delete=models.CASCADE)
	image=models.ImageField(upload_to="pics/",null=True)
	dob=models.DateField(null=True)
	mobileno=models.CharField(max_length=10,null=True)






	





	# #user=models.ForeignKey(User,on_delete=models.CASCADE)

	# student_name=models.CharField(max_length=10)
	# user_name=models.CharField(max_length=10,null=True)
	# phone_num=models.IntegerField()
	# email=models.EmailField()
	# age=models.IntegerField()
	# #password=models.CharField(max_length=12,null=True)

	


	def __str__(self):
		return self.student_name

		
class Faculty(models.Model):
	emp_id=models.CharField(max_length=10)
	name=models.CharField(max_length=100)
	email=models.EmailField()
	phone=models.IntegerField(null=True,blank=True)

	def __str__(self):
		return self.name

	































