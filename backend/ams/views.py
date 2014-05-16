from django import http
from django.utils import simplejson as json

event1 = {\
    "id" : 0, \
    "name" : "Van Gogh Museum", \
    "description" : "Come in, now!", \
    "latitude" : 42,\
    "longitude" : 20,\
    "start" : "08:30",\
    "end" : "22:30",\
    "street" : "herengracht",\
    "number" : "20",\
    "building" : "",\
    "shop-image" : "http://instagram.com/some.jpg",\
    "type" : "museum"\
  }

def home(request):
    print "Event: " + str(event1)
    jsonEvent1 = json.dumps([event1])
    print "JSON: " + str(jsonEvent1)
    return http.HttpResponse(jsonEvent1, 
      content_type='application/json')
