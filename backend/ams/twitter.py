from google.appengine.api import urlfetch
from django.utils import simplejson as json
import sys
sys.path.insert(0, 'libs')

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

class Twitter:
  def test():
    return "Hi there!"