from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Squirrel

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
    }

    return render(request,'squirrel/index.html',context)

def detail(request,squirrel_id):
    squirrel =get_object_or_404(Squirrel, pk=squirrel_id)

    context ={
            'squirrel':squirrel,
    }

    return render(request,'squirrel/detail.html',context)

