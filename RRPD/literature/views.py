from http.client import HTTPResponse
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError , JsonResponse
from .models import  titleM
import requests
from django.template import loader
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def reference(request):
    # latest_referenceM = referenceM.objects()
    # context = {"latest_referenceM": latest_referenceM}
    return render(request,"index.html")



def my_model(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title',[])
        doi = data.get('Doi',[])





        for i in range(2):
            my_titleM = titleM(
                title = title[i],
                Doi = doi[i],
            )
            my_titleM.save()

        return JsonResponse({'message': "Data saved"})
    
    return JsonResponse({'message': "Invalid request."})


   