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

@api_view(['GET', 'POST'])
def validate_api(request):      
    if request.method == 'POST':
            payload = json.loads(request.body.decode('utf-8'))
            print(payload)
    
            return Response({'msg': 'success'}, status=status.HTTP_200_OK)
    elif request.method == 'GET':
        params = request.query_params
        if params.get('hub.verify_token') == WHATSAPP_VERIFY_TOKEN and params.get('hub.mode') == 'subscribe':
            return Response(params.get('hub.challenge'), status=status.HTTP_200_OK)
        return Response("ERROR", status=status.HTTP_400_BAD_REQUEST)
