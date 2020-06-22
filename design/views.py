from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import Http404

# Create your views here.
from .models import script

def index(request):
    script_list=script.objects.all()
    return render(request, 'design/index.html', {'script_list':script_list} )