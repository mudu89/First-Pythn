from django.db import models

# Create your models here.
#skill_set =(('1','Java/J2EE'),('2','Python'),('3','Reactjs'),('4','.net'),('5','PL/SQL'))
class jobopenings(models.Model):
    #job_skill_set = models.CharField(max_length=200,blank=True,choices=skill_set)
    job_Id = models.IntegerField(null=False, default=1000)
    job_Position = models.CharField(max_length=200, blank=True)
    job_Skill_set = models.CharField(max_length=200, blank=True)
    job_Desc = models.CharField(max_length=1000, blank=True)
    job_Openings = models.IntegerField(null=True)
    job_Post_Date = models.DateField(null=True)
    job_Status = models.CharField(max_length=20, blank=True)
    job_Contact_Person = models.CharField(max_length=200, blank=True)

