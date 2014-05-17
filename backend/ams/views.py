from django import http
from django.utils import simplejson as json
import urllib2
import logging
from google.appengine.api import urlfetch
import cmath
import math
from ams.forthsquare import ForthSquare
from ams.twitter import Twitter

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


OAUTH_TOKEN='3NX4ATMVS35LKIP25ZOKIVBRGAHFREKGNHTAKQ5NPGMCWOE0'

DEFAULT_RADIUS = 100.0

forthsquare = ForthSquare()
twitter = Twitter()

<<<<<<< HEAD

    photo = getPhoto(venue['id'])
    if photo:
#        print photo
#        print type(photo)
        if photo.get('response').get('photos').get('count') != 0:
#            print 'source:', photo.get('response').get('photos').get('items')[0]
            res['photo'] = photo.get('response').get('photos').get('items')[0]


    return res
=======
>>>>>>> 61a216a9f7ca2284cfdba41fde188dc1c571e4f4

def venues(request):

#    pos = '52.378688,4.900504'
#    print 'request:', request
#    logger.debug('request')
    t = Twitter()
    if not request.GET or not request.GET.get(u'll'):
        return http.HttpResponseBadRequest('Wrong data')

#    print request.GET
#    print request.GET.get(u'll')
    pos = request.GET.get(u'll')
    lat0 = float(pos.split(',')[0])
    lng0 = float(pos.split(',')[1])
    print '0-point coord:', lat0, lng0

    foursquareRequest = 'https://api.foursquare.com/v2/venues/search?ll=%s&limit=5&radius=%s&oauth_token=%s&v=20140517' % (pos, DEFAULT_RADIUS, OAUTH_TOKEN)
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
#                    res = {'lat' : lat, 'lng': lng, 'id' : i['id'].encode("utf-8"), 'name' : i['name'].encode("utf-8") }
                    venuesInRadar.append(forthsquare.getVenueData(i))

        print len(venuesInRadar)
        print venuesInRadar
        print 'point3'
    else:
        venuesInRadar = list()
        for i in venues:
            venuesInRadar.append(forthsquare.getVenueData(i))

    '''
        if len(venuesInRadar) == 1:
            # return detailed information
            response = http.HttpResponse(venuesInRadar[0], 
              content_type='application/json')
            response["Access-Control-Allow-Origin"] = "*"
            return response
    '''

    print venuesInRadar
    print type(venuesInRadar)
    print 'point4'
    response = http.HttpResponse(json.dumps(venuesInRadar), 
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

    response = http.HttpResponse(json.dumps(json_raw), 
      content_type='application/json')
    response["Access-Control-Allow-Origin"] = "*"
    return response

<<<<<<< HEAD
def getPhoto(id):
    foursquareRequest = 'https://api.foursquare.com/v2/venues/%s/photos?limit=1&sort=recent&oauth_token=%s&v=20140517' % (id, OAUTH_TOKEN)

    foursquareResponse = urllib2.urlopen(foursquareRequest)
    json_raw = foursquareResponse.read()
    if not json_raw:
        return None

    json_data = json.loads(json_raw)
    print json_data

    return json_data
=======

>>>>>>> 61a216a9f7ca2284cfdba41fde188dc1c571e4f4

def photos(request):
#    id = '4a688ba1f964a52088ca1fe3'
    if not request.GET or not request.GET.get(u'id'):
        return http.HttpResponseBadRequest('Wrong data')

    id = request.GET.get(u'id')

    foursquareRequest = 'https://api.foursquare.com/v2/venues/%s/photos?limit=1&sort=recent&oauth_token=%s&v=20140517' % (id, OAUTH_TOKEN)

    foursquareResponse = urllib2.urlopen(foursquareRequest)
    json_raw = foursquareResponse.read()
#    json_data = json.loads(json_raw)

    if not json_raw:
        return http.DoesNotExist('photo does not exist')

    response = http.HttpResponse(json.dumps(json_raw), 
      content_type='application/json')
    response["Access-Control-Allow-Origin"] = "*"
    return response

def tweets(request):
    radius="0.02km"
    if not request.GET or not request.GET.get(u'll'):
      return http.HttpResponseBadRequest('Wrong data')

    pos = request.GET.get(u'll')
    result = twitter.tweets(radius, pos)
    response = http.HttpResponse(result, 
      content_type='application/json')
    response["Access-Control-Allow-Origin"] = "*"
    return response
