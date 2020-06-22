from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import Http404

# Create your views here.
from .models import structure

def index(request):
    structure_list=structure.objects.all()
    return render(request, 'synthesis/index.html', {'structure_list':structure_list} )

def detail(request, structure_id):
    struct = get_object_or_404(structure, pk=structure_id)
    return render(request, 'synthesis/detail.html', {'struct':struct})
