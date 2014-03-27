from django.http import HttpResponse
from .models import Event
from django.core import serializers
import  datetime
def hello(request):
    return HttpResponse('hello world')
def create_event(request):
    if request.method is 'POST':
        year=request['POST'].get('year')
        month=request['POST'].get('month')
        dat=request['POST'].get('dat')
        hours=request['POST'].get('hours')
        mit=request['POST'].get('mit')
        showname=request['POST'].get('showname')
        showtime=datetime.datetime(year,month,dat,hours,mit)
        # datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
        e=Event(showtime=showtime,showname=showname)
        e.save()
        data=serializers.serialize('json', e)
        return HttpResponse(data)
    else:
        return HttpResponse('Hi there')
def list_event(request):
    events=Event.objects.all()
    data = serializers.serialize('json', events)
    return HttpResponse(data)


