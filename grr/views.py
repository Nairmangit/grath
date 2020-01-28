from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from .models import test
from .forms import LogForm, Form
import datetime, qsstats

# Create your views here.
def index(request):
    form = LogForm
    context =  {'form' : form}
    return render(request, 'grr/index.html', context)

def lk(request):
    form = Form()
    context =  {'form' : form}
    return render(request, 'grr/lk.html', context)

@require_POST

def logg (request):
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    return redirect('lk')

def loggout (request):
    return redirect('index')

def grath(request):
    time = datetime.datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
    qwe = test.objects.all()
    values = []
    for qwe.test in qwe:
        if qwe.test.dat.date() == time:
            values = values + [(qwe.test.dat, int(qwe.test.tem))]
    #qwe = qwe.filter(dat = time)
    #qss = qsstats.QuerySetStats(qs, 'dat', aggregate=None)
    #print (datetime.date.today())
    #today = datetime.datetime.strptime(request.POST['date'], '%Y-%m-%d')
    #seven_days_ago = today - datetime.timedelta(days=1)
    #today = today + datetime.timedelta(days=1)
    #values = qss.time_series(seven_days_ago, today, interval = 'days')
    #values = [(test.dat, int(test.tem)) for test in qwe]
    context =  {'values' : values}
    return render(request, 'grr/grath.html', context)
