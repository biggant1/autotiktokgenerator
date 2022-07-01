import tweepy

from config import ACCOUNT_IDS

class TwitterStream(tweepy.Stream):
    def __init__(self, callback, consumer_key, consumer_secret, access_token, access_token_secret):
        self.callback = callback
        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret)
        print("Twitter stream initalized!")

    def on_status(self, status):
        try:
            if "media" in status.entities and not status.in_reply_to_status_id and status.user.id_str in ACCOUNT_IDS:
                self.callback(status)
        except KeyError:
            pass
        return super().on_status(status)