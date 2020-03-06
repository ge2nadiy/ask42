from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ask42App.models import Input
from ask42App.serializers import InputSerializer
from django.core import serializers


def home(request):
    return render(request, 'index.html')


class InputView(ModelViewSet):
    serializer_class = InputSerializer
    queryset = Input.objects.all()


def second_page(request):
    return HttpResponse(serializers.serialize('json', Input.objects.all()))
