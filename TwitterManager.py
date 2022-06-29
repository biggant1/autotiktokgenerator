from random import choice
from twitter import Twitter, OAuth
import os

class TwitterManager:
    def __init__(self):
        self.client = Twitter(
            auth=OAuth(os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET"), os.getenv("TWITTER_API_KEY"), os.getenv("TWITTER_API_KEY_SECRET")))

    def __find_longest_tweet(self, tweets):
        return max(tweets, key=lambda tweet: len(tweet['full_text']))

    def __find_random_tweet(self, tweets):
        return choice(tweets)

    def get_tweet_data(self, keyword: str) -> tuple[str, str]:
        query = f'"{keyword}" exclude:replies'
        result = self.client.search.tweets(q=query, result_type="popular", count=50, tweet_mode="extended", lang="en")
        tweet = self.__find_random_tweet(result['statuses'])
        return (f"https://twitter.com/{tweet['user']['screen_name']}/status/{tweet['id_str']}", tweet['full_text'])