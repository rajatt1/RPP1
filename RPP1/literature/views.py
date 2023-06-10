from http.client import HTTPResponse
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError , JsonResponse
from .models import referenceM
import requests
from django.template import loader



# Create your views here.
def reference(request):
    # latest_referenceM = referenceM.objects()
    # context = {"latest_referenceM": latest_referenceM}
    return render(request,"index.html")



def my_model(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        my_instance = referenceM(**json_data)
        my_instance.save()

        return HttpResponse('Data saved successfully')
    
    return HttpResponse('Invaid request method')