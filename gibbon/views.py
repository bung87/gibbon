from django.http import HttpResponse
from  django.shortcuts  import  render
from .models import Event
from django.core import serializers
import  datetime
def hello(request):
    return render(request,'index.html')

def create_event(request):
    if request.method == 'POST':
        # year=request['POST'].get('year')
        # month=request['POST'].get('month')
        # dat=request['POST'].get('dat')
        # hours=request['POST'].get('hours')
        # mit=request['POST'].get('mit')
        showname=request.POST.get('showname')
        # showtime=datetime.datetime(year,month,dat,hours,mit)

        # datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
        showtime=datetime.datetime.strptime(request.POST.get('showtime'),'%Y-%m-%d %H:%M')
        e=Event.objects.create(showtime=showtime,showname=showname,state=0)
        e.save()
        # data=serializers.serialize('json', e)
        return HttpResponse('')
    else:
        return HttpResponse('Hi there')
def list_event(request):
    events=Event.objects.all()
    data = serializers.serialize('json', events)
    return HttpResponse(data)


