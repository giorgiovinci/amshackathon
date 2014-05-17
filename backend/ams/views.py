from django import http
from django.utils import simplejson as json
import urllib2
import logging
from google.appengine.api import urlfetch
import cmath
import math
from ams.forthsquare import ForthSquare
from ams.twitter import Twitter


OAUTH_TOKEN='3NX4ATMVS35LKIP25ZOKIVBRGAHFREKGNHTAKQ5NPGMCWOE0'

DEFAULT_RADIUS = 500.0
DEFAULT_LIMIT  = 5

forthsquare = ForthSquare()
twitter = Twitter()

#arts, education,events, food, night, outdoors, professional, residence, shop, travel
CATEGORIES = [('arts','4d4b7104d754a06370d81259'),\
('education','4d4b7105d754a06372d81259'),\
('events','4d4b7105d754a06373d81259'),\
('food','4d4b7105d754a06374d81259'),\
('night','4d4b7105d754a06376d81259'),\
('outdoors','4d4b7105d754a06377d81259'),\
('professional','4d4b7105d754a06375d81259'),\
('residence','4e67e38e036454776db1fb3a'),\
('shop','4d4b7105d754a06378d81259'),\
('travel','4d4b7105d754a06379d81259')]

def venues(request):

    if not request.GET or not request.GET.get(u'll'):
        return http.HttpResponseBadRequest('Wrong data')

    pos = request.GET.get(u'll')
    lat0 = float(pos.split(',')[0])
    lng0 = float(pos.split(',')[1])
    
    categories = []
    param_categories = request.GET.get(u'categories')
    print 'PARAM CATEGORIES: ' + str(param_categories)
    if param_categories:
      categories = param_categories.split(',')

    print '0-point coord:', lat0, lng0

    radius = '&radius=%s' %(DEFAULT_RADIUS)
    limit  = '&limit=%s' %(DEFAULT_LIMIT)

    for categoryName in categories:
      categoryId = getCategoryId(categoryName)
      filter_url_categories = '&categoryId=%s' %(categoryId)
      json_data = forthsquare.venues(pos, limit, radius, filter_url_categories) 

    # print 'data:', json_data
    venues = json_data['response']['venues']
    print "got some venues"

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

def getCategoryId(category):
  for name,id in CATEGORIES:
   if name == category: 
     return id

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

def getPhoto(id):
    foursquareRequest = 'https://api.foursquare.com/v2/venues/%s/photos?limit=1&sort=recent&oauth_token=%s&v=20140517' % (id, OAUTH_TOKEN)

    foursquareResponse = urllib2.urlopen(foursquareRequest)
    json_raw = foursquareResponse.read()
    if not json_raw:
        return None

    json_data = json.loads(json_raw)
    print json_data

    return json_data

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
