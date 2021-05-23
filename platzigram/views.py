"vistas de platzigram"

from django.http import HttpResponse

"utilities"
from datetime import datetime
import json



def hello_world(request):

    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse("Hi, current server time is {now}".format(now = str(now)))

def sort_integers(request):

    numbers= request.GET['numbers']

    numbers = list(map(int,numbers.split(",")))
    numbers = sorted(numbers)

    data = {
        'status':'ok',
        'numbers':numbers,
        'messaje':'integers sorted succesfully'
    }


    return HttpResponse(json.dumps(data, indent=4), content_type='application/json' )


def say_hi(request,name, age):
    "return a greeting"
    if age < 12 :
        message = "Sorry {}, you re not allowed here".format(name)
    else:
        message = "Hello {}, welcome to platzigram".format(name)
    
    return HttpResponse(message)