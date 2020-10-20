from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .forms import UpdateForm

from .models import Squirrel

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
    }

    return render(request,'squirrel/index.html',context)

def update(request,squirrel_id):
    
    if request.method == 'POST':
        squirrel=get_object_or_404(Squirrel,pk=squirrel_id)
        form = UpdateForm(request.POST, instance=squirrel)
        if form.is_valid():
            squirrel.save()
            return redirect('/sightings/')
    
    squirrel=get_object_or_404(Squirrel,pk=squirrel_id)
    form = UpdateForm(instance=squirrel)
    context ={
            'form':form,
    }

    return render(request,'squirrel/update.html',context)

def add(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    
    form = UpdateForm()
    context ={
            'form':form,
    }

    return render(request,'squirrel/add.html',context)
