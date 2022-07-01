from random import choice
from numpy import result_type
import tweepy
import os

from TwitterStream import TwitterStream
from config import ACCOUNT_IDS

class TwitterManager:
    def __init__(self, video_callback):
        access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        consumer_key = os.getenv("TWITTER_API_KEY")
        consumer_secret = os.getenv("TWITTER_API_KEY_SECRET")

        auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
        self.stream = TwitterStream(video_callback, consumer_key, consumer_secret, access_token, access_token_secret)
        self.stream.filter(follow=ACCOUNT_IDS)

    @staticmethod
    def get_url_from_tweet(tweet):
        return f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id_str}"