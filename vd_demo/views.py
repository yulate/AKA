import json
import requests
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


def Index(request):
    return render(request, 'index.html')

def Development_log(request):
    return render_to_response('Development_log.html')

@method_decorator(csrf_exempt)
def HttpTesting(request):
    return render(request, 'HttpTesting.html')

csrf_exempt
def HttpTesting_Post(request):
    url = request.POST['url']
    value = request.POST['value']
    req = requests.post(url,data=json.dumps(value),headers={'Content-Type':'application/json'})
    connect = {
        req : req
    }
    # return render(request,'HttpTesting.html',connect)
    return HttpResponse(req)