#https://github.com/tweepy/tweepy
from tweepy.streaming import StreamListener
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

api = API(auth)
ll="52.378688,4.900504"
radius="0.02km"
for tweet in Cursor(api.search,
                           q="",
                           rpp=10,
						   geocode=ll+','+radius,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items():
	tweetText= tweet.text.encode('UTF-8')
	print json.dumps({'text': tweetText, 'user_photo':tweet.user.profile_image_url})
