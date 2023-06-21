from django.shortcuts import redirect, render
from http.client import HTTPResponse
import json
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError , JsonResponse
from django.core import serializers
from .models import  projectM
import requests
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def projectCreate(request):
    return render(request,"projectCreate.html")

def save_data(request):
    if request.method == 'POST':
        pro_name = request.POST.get('proName')
        if pro_name:
            my_projectM = projectM(project_name=pro_name)
            my_projectM.save()

            serialized_project = serializers.serialize('json', [my_projectM])
            return redirect('reference' + serialized_project)
        else:
            return JsonResponse({'error': 'Invalid data'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
            