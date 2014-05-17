from django import http
from django.utils import simplejson as json
import urllib2
import logging
from google.appengine.api import urlfetch
import cmath
import math

'''
#https://github.com/tweepy/tweepy
from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Cursor
from tweepy import API
import simplejson as json

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="hzs08p3vTJj0MoGQHehA"
consumer_secret="Ff7IdfhvauZO1avHEopivnaiWyu8BKq8Ylexi9Qkc"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token="1705695660-52T71aE6khDGfoHsv9LWv3fLqrFzoU2Nt78SvmK"
access_token_secret="M8tG2nReGfYp2nPDRMLLrY4aVwyZ4gkd7MM06ioV9YZan"

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

def tweets(request):
    api = API(auth)
    #ll="52.378688,4.900504"
    radius="0.02km"
    if not request.GET or not request.GET.get(u'll'):
        return http.HttpResponseBadRequest('Wrong data')

    pos = request.GET.get(u'll')

    tweetList = list()

    for tweet in Cursor(api.search,
                               q="",
                               rpp=10,
                                geocode=ll+','+radius,
                               result_type="recent",
                               include_entities=True,
                               lang="en").items():
            tweetText= tweet.text.encode('UTF-8')
            tweetList.append({'text': tweetText, 'user_photo':tweet.user.profile_image_url})

            #print json.dumps({'text': tweetText, 'user_photo':tweet.user.profile_image_url})

    result = json.dumps(tweetList)
    print 'result:', result
    response = http.HttpResponse(result, 
      content_type='application/json')
    response["Access-Control-Allow-Origin"] = "*"
    return response
'''

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
DEFAULT_RADIUS = 100.0
DEFAULT_SPREAD_ANGLE = 60

logger = logging.getLogger(__name__)

def venueInRadarRange(lat0, lng0, alpha, beta, gamma, radius, spreadAngle, lat, lng, distance):
    #TODO:implement the function
    difflat = lat - lat0
    difflng = lng - lng0

    print 'diff:', difflat, difflng

    (r, phi) = cmath.polar(complex(difflat, difflng))
    phi = math.degrees(phi)
    if phi < 0:
        phi += 360
    print 'r, phi:', r, phi, alpha
    print 'r, radius, distance:', r, radius, distance
    print 'phi, alpha:', phi, alpha, abs(phi - alpha)

    result = distance < radius and abs(phi - alpha) < spreadAngle / 2.0
    print result

    return result


def home(request):
#    pos = '52.378688,4.900504'
#    print 'request:', request
#    logger.debug('request')

    if not request.GET or not request.GET.get(u'll'):
        return http.HttpResponseBadRequest('Wrong data')

#    print request.GET
#    print request.GET.get(u'll')
    pos = request.GET.get(u'll')
    lat0 = float(pos.split(',')[0])
    lng0 = float(pos.split(',')[1])
    print '0-point coord:', lat0, lng0

    foursquareRequest = 'https://api.foursquare.com/v2/venues/search?ll=%s&oauth_token=%s&v=20140517' % (pos, OAUTH_TOKEN)
    foursquareResponse = urllib2.urlopen(foursquareRequest)
    json_raw = foursquareResponse.read()
    json_data = json.loads(json_raw)

    print 'data:', json_data
    venues = json_data['response']['venues']
    print len(venues)
    print venues

    print 'point1'

    if request.GET.get('alpha') and request.GET.get('beta') and request.GET.get('gamma'):
        print 'point2'
        alpha = float(request.GET.get('alpha'))
        beta  = float(request.GET.get('beta'))
        gamma = float(request.GET.get('gamma'))
        if request.GET.get('radius'):
            float(request.GET.get('radius'))
        else:
            radius = DEFAULT_RADIUS


        venuesInRadar = list()
        for i in venues:
#            print i
            if 'url' in i:
                print i['url']
            if i and i.get('location') and i.get('location').get('lat') and i.get('location').get('lng') and i.get('location').get('distance'):
                lat = float(i.get('location').get('lat'))
                lng = float(i.get('location').get('lng'))
                distance = float(i.get('location').get('distance'))
                print 'lat:', lat
                print 'lng:', lng
                print 'distance:', distance
                if venueInRadarRange(lat0, lng0, alpha, beta, gamma, radius, DEFAULT_SPREAD_ANGLE, lat, lng, distance):
                    venuesInRadar.append(i)

        print len(venuesInRadar)
        print venuesInRadar
        print 'point3'
    else:
        venuesInRadar = venues
    '''
        if len(venuesInRadar) == 1:
            # return detailed information
            response = http.HttpResponse(venuesInRadar[0], 
              content_type='application/json')
            response["Access-Control-Allow-Origin"] = "*"
            return response
    '''

    print 'point4'
    response = http.HttpResponse(venuesInRadar, 
      content_type='application/json')
    response["Access-Control-Allow-Origin"] = "*"
    return response

'''
    response = http.HttpResponse(json_raw, 
      content_type='application/json')
    response["Access-Control-Allow-Origin"] = "*"
    return response
'''

def comments(request):
#    id = '4a688ba1f964a52088ca1fe3'
    if not request.GET or not request.GET.get(u'id'):
        return http.HttpResponseBadRequest('Wrong data')

    id = request.GET.get(u'id')

    foursquareRequest = 'https://api.foursquare.com/v2/venues/%s/tips?sort=recent&oauth_token=%s&v=20140517' % (id, OAUTH_TOKEN)

    foursquareResponse = urllib2.urlopen(foursquareRequest)
    json_raw = foursquareResponse.read()
#    json_data = json.loads(json_raw)

    response = http.HttpResponse(json_raw, 
      content_type='application/json')
    response["Access-Control-Allow-Origin"] = "*"
    return response
