from random import choice
from dotenv import load_dotenv
from selenium.common.exceptions import TimeoutException
from SeleniumManager import SeleniumManager
from TiktokManager import TiktokManager
from TwitterManager import TwitterManager
from VideoManager import VideoManager
from config import VIDEO_TOPIC
from util import random_prefix, gen_hashtags
from os import path

load_dotenv()

class Main:
    def __init__(self):
        self.twit = TwitterManager(self.create_video)

    def create_video(self, status):
        sm = SeleniumManager()
        try:
            img = sm.screenshot_element(TwitterManager.get_url_from_tweet(status), SeleniumManager.SELECTOR)
        except TimeoutException:
            return print("Failed to find selector")
        sm.destroy()
        video = VideoManager.generate_video(img)
        tm = TiktokManager()
        tm.upload_video(f"{gen_hashtags()}", path.abspath(video))
        tm.destroy()
    
if __name__ == "__main__":
    main = Main()