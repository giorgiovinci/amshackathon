from google.appengine.api import urlfetch
from django.utils import simplejson as json
import sys
sys.path.insert(0, 'libs')

#https://github.com/tweepy/tweepy
'''
To fix _ssl issue on Mac
http://stackoverflow.com/questions/16192916/importerror-no-module-named-ssl-with-dev-appserver-py-from-google-app-engine/16937668#16937668

'''
from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Cursor
from tweepy import API

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

l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class Twitter:
  def tweets(self,radius,pos):
    print "start twitter api" 
    api = API(auth)
    tweetList = list()

    for tweet in Cursor(api.search,
                               q="",
                               rpp=10,
                                geocode=pos+','+radius,
                               result_type="recent",
                               include_entities=True,
                               lang="en").items():
            tweetText= tweet.text.encode('UTF-8')
            tweetList.append({'text': tweetText, 'user_name':tweet.user.name, 'user_photo':tweet.user.profile_image_url})

            #print json.dumps({'text': tweetText, 'user_photo':tweet.user.profile_image_url})

    result = json.dumps(tweetList)
    print 'result:', result
    return result