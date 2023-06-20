from http.client import HTTPResponse
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError , JsonResponse
from .models import  titleM
import requests
from django.template import loader



# Create your views here.
def reference(request):
    # latest_referenceM = referenceM.objects()
    # context = {"latest_referenceM": latest_referenceM}
    return render(request,"index.html")



def my_model(request):
    if request.method == 'POST':
        title = request.POST.getlist('title[]')
        doi = request.POST.getlist('Doi[]')


        for i in range(len(title)):
            titleM.objects.create(title=title(i), Doi=doi[i])

        return HttpResponse('Data saved successfully')
    else:
        return HttpResponseBadRequest('Invalid request method')


    #     json_data = json.loads(request.body)
    #     my_instance = referenceM(**json_data)
    #     my_instance.save()

    #     return HttpResponse('Data saved successfully')
    
    # return HttpResponse('Invaid request method')