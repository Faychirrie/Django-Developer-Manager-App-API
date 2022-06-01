#helps convert the complex types of model instances into native python data types 
# that can then be easily rendered into json or other content types
from pyexpat import model
from rest_framework import serializers
from DeveloperApp.models import RequestType,UserRequest,EngineerAction,CompanyDetails

class RequestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=RequestType
        fields=('irequest_type_id','srequest_type_name','srequest_type_description','dcreated_date','dupdated_date','screated_by','supdated_by','cstatus')

class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserRequest
        fields=('iuser_request_id','sproblem_name','sproblem_description','icompany_id','cresolution_status','ddate_raised','dcreated_date','dupdated_date','screated_by','supdated_by','cstatus')
       

class EngineerActionSerializer(serializers.ModelSerializer):
    class Meta:
        model=EngineerAction
        fields=('iengineer_action_id','iuser_request_id','irequest_type_id','stask_name','stask_description','scode_files_altered','dtask_date',' dcreated_date','dupdated_date',' screated_by','supdated_by','cstatus')

class CompanyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyDetails
        fields=('icompany_details_id','scompany_name',' dcreated_date','dupdated_date',' screated_by','supdated_by','cstatus')
  