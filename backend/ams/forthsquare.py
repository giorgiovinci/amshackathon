from google.appengine.ext import ndb
from google.appengine.api import urlfetch
from django.utils import simplejson as json

import urllib2
import logging
import cmath
import math


OAUTH_TOKEN='3NX4ATMVS35LKIP25ZOKIVBRGAHFREKGNHTAKQ5NPGMCWOE0'


class ForthSquare:

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

  def getVenueData(self, venue):
      res = { 
      'lat'  : venue.get('location').get('lat'),
      'lng'  : venue.get('location').get('lng'),
      'id'   : venue['id'].encode("utf-8"),
      'name' : venue['name'].encode("utf-8") }

      if 'address' in venue.get('location'):
          res['address'] = venue.get('location').get('address')

      if 'postalCode' in venue.get('location'):
          res['postalCode'] = venue.get('location').get('postalCode')

      if 'formattedPhone' in venue.get('contact'):
          res['formattedPhone'] = venue.get('contact').get('formattedPhone')


      photo = self.getPhoto(venue['id'])
      if photo:
  #        print photo
  #        print type(photo)
          if photo.get('response').get('photos').get('count') != 0:
  #            print 'source:', photo.get('response').get('photos').get('items')[0]
              res['photo'] = photo.get('response').get('photos').get('items')[0]


      return res

  def getPhoto(self, id):
      foursquareRequest = 'https://api.foursquare.com/v2/venues/%s/photos?limit=1&sort=recent&oauth_token=%s&v=20140517' % (id, OAUTH_TOKEN)

      foursquareResponse = urllib2.urlopen(foursquareRequest)
      json_raw = foursquareResponse.read()
      if not json_raw:
          return None

      json_data = json.loads(json_raw)
      print json_data

      return json_data