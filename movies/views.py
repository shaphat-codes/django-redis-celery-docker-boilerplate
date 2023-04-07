from django.shortcuts import render
from django_celery_results.models import TaskResult
from . serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
    

@api_view(['GET'])
def List(request):
    items = TaskResult.objects.all()
    serializer = TaskResultSerializer(items, many=True)
    return Response(serializer.data)

   