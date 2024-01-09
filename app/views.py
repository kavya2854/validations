from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def create_school(request):
    ESFO = SchoolForm()
    d={'schools':ESFO}
    if request.method == 'POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            Sn=SFDO.cleaned_data['Sname']
            Sp=SFDO.cleaned_data['Sprincipal']
            Sl=SFDO.cleaned_data['Slocation']
            Se=SFDO.cleaned_data['email']
            SCe=SFDO.cleaned_data['confirmemail']
            p=SFDO.cleaned_data['password']
            cp=SFDO.cleaned_data['confirmPassword']
            SO=School.objects.get_or_create(Sname=Sn,Sprincipal=Sp,Slocation=Sl,email=Se,confirmemail=SCe,password=p,confirmPassword=cp)[0]
            SO.save()
            return HttpResponse('School is created...')
        else:
            return HttpResponse('Invalid data')
    return render(request,'create_school.html',d)