from django.db import models

# Create your models here.
class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveSmallIntegerField()
	remarks=models.TextField()

	def __str__(self):
		#return self.id
		return str(self.id)+'-'+self.name

class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	address=models.TextField()
	gender=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	profile_pic=models.ImageField(upload_to='profile_pic/',default='')

	def __str__(self):
		return self.fname+'-'+self.lname
