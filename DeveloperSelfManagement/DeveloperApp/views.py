from django.shortcuts import render

# allows other domains to access our api
from django.views.decorators.csrf import csrf_exempt
# pass incoming data into data model
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from DeveloperApp.models import RequestType,UserRequest,EngineerAction,CompanyDetails
from DeveloperApp.serializers import RequestTypeSerializer,UserRequestSerializer,EngineerActionSerializer,CompanyDetailsSerializer

@csrf_exempt
def RequestTypeApi(request, id=2):
    if request.method=='GET':
        requestTypes= RequestType.objects.all()
        requestTypes_serializer= RequestTypeSerializer(requestTypes,many=True)#converting data to json
        return JsonResponse(requestTypes_serializer.data,safe=False)
    elif request.method=='POST':
        requestTypes_data=JSONParser().parse(request)
        requestTypes_serializer=RequestTypeSerializer(data=requestTypes_data)# converting to model
        if requestTypes_serializer.is_valid():
            requestTypes_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("failed to add",safe=False)
    elif request.method=='PUT':
        requestTypes_data=JSONParser().parse(request)
        requestTypes=RequestType.objects.get(irequest_type_id=requestTypes_data["irequest_type_id"])
        requestTypes_serializer=RequestTypeSerializer(requestTypes,data=requestTypes_data)
        if requestTypes_serializer.is_valid():
            requestTypes_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("failed to add",safe=False)
    elif request.method=='DELETE':
        requestTypes=RequestType.objects.get(irequest_type_id=id)
        requestTypes.delete()
        return JsonResponse("Deleted Successfully", safe=False)
@csrf_exempt
def UserRequestApi(request, id=2):
    if request.method=='GET':
        userRequest= UserRequest.objects.all()
        userRequest_serializer= UserRequestSerializer(userRequest,many=True)#converting data to json
        return JsonResponse(userRequest_serializer.data,safe=False)
    elif request.method=='POST':
        userRequest_data=JSONParser().parse(request)
        userRequest_serializer=UserRequestSerializer(data=userRequest_data)# converting to model
        if userRequest_serializer.is_valid():
            userRequest_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("failed to add",safe=False)
    elif request.method=='PUT':
        userRequest_data=JSONParser().parse(request)
        userRequest=UserRequest.objects.get(iuser_request_id=userRequest_data["iuser_request_id"])
        userRequest_serializer=UserRequestSerializer(userRequest,data=userRequest_data)
        if userRequest_serializer.is_valid():
            userRequest_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("failed to add",safe=False)
    elif request.method=='DELETE':
       userRequest=UserRequest.objects.get(iuser_request_id=id)
       userRequest.delete()
       return JsonResponse("Deleted Successfully", safe=False)