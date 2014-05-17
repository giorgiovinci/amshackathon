from django import http
from django.utils import simplejson as json
import urllib2
import logging
from google.appengine.api import urlfetch

'''
event1 = {\
    "id" : 1, \
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
'''

OAUTH_TOKEN='3NX4ATMVS35LKIP25ZOKIVBRGAHFREKGNHTAKQ5NPGMCWOE0'

logger = logging.getLogger(__name__)

def home(request):
#    pos = '52.378688,4.900504'
#    print 'request:', request
#    logger.debug('request')

    if not request.GET or not request.GET.get(u'll'):
        return http.HttpResponseBadRequest('Wrong data')

#    print request.GET
#    print request.GET.get(u'll')
    pos = request.GET.get(u'll')

    foursquareRequest = 'https://api.foursquare.com/v2/venues/search?ll=%s&oauth_token=%s&v=20140517' % (pos, OAUTH_TOKEN)
    foursquareResponse = urllib2.urlopen(foursquareRequest)
    json_raw = foursquareResponse.read()
#    json_data = json.loads(json_raw)

    return http.HttpResponse(json_raw, 
      content_type='application/json')

def comments(request):
#    id = '4a688ba1f964a52088ca1fe3'
    if not request.GET or not request.GET.get(u'id'):
        return http.HttpResponseBadRequest('Wrong data')

    id = request.GET.get(u'id')

    foursquareRequest = 'https://api.foursquare.com/v2/venues/%s/tips?sort=recent&oauth_token=%s&v=20140517' % (id, OAUTH_TOKEN)

    foursquareResponse = urllib2.urlopen(foursquareRequest)
    json_raw = foursquareResponse.read()
#    json_data = json.loads(json_raw)

    return http.HttpResponse(json_raw, 
      content_type='application/json')
