from re import M
from django.db import models

# Create your models here.
class RequestType (models.Model):
    irequest_type_id=models.AutoField(primary_key=True)
    srequest_type_name=models.CharField(max_length=500)
    srequest_type_description=models.CharField(max_length=500)
    dcreated_date=models.DateField()
    dupdated_date=models.DateField()
    screated_by=models.CharField(max_length=500)
    supdated_by=models.CharField(max_length=500)
    cstatus=models.CharField(max_length=1)

class UserRequest (models.Model):
    iuser_request_id=models.AutoField(primary_key=True)
    sproblem_name=models.CharField(max_length=500)
    sproblem_description=models.CharField(max_length=500)
    icompany_id=models.IntegerField()
    cresolution_status=models.CharField(max_length=1)
    ddate_raised=models.DateField()
    dcreated_date=models.DateField()
    dupdated_date=models.DateField()
    screated_by=models.CharField(max_length=500)
    supdated_by=models.CharField(max_length=500)
    cstatus=models.CharField(max_length=1)

class EngineerAction (models.Model):
    iengineer_action_id=models.AutoField(primary_key=True)
    iuser_request_id=models.IntegerField()
    irequest_type_id=models.IntegerField()
    stask_name=models.CharField(max_length=500)
    stask_description=models.CharField(max_length=500)
    scode_files_altered=models.CharField(max_length=500)
    dtask_date=models.DateField()
    dcreated_date=models.DateField()
    dupdated_date=models.DateField()
    screated_by=models.CharField(max_length=500)
    supdated_by=models.CharField(max_length=500)
    cstatus=models.CharField(max_length=1)
    
class CompanyDetails (models.Model):
    icompany_details_id=models.AutoField(primary_key=True)
    scompany_name=models.CharField(max_length=500)
    dcreated_date=models.DateField()
    dupdated_date=models.DateField()
    screated_by=models.CharField(max_length=500)
    supdated_by=models.CharField(max_length=500)
    cstatus=models.CharField(max_length=1)