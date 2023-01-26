import json
import os
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.settings import WHATSAPP_VERIFY_TOKEN
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# @api_view(['GET', 'POST'])
@csrf_exempt
def validate_api(request):
    if request.method == 'GET':
        params = request.GET
        if params.get('hub.verify_token') == WHATSAPP_VERIFY_TOKEN and params.get('hub.mode') == 'subscribe':
            return HttpResponse(params.get('hub.challenge'))
        return HttpResponse("ERROR")

    elif request.method == 'POST':
            payload = json.loads(request.body.decode('utf-8'))
            print(payload)
            
            return HttpResponse("OK", status=200)
    return HttpResponse("ERROR", status=400)
