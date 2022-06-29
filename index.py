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

def main():
    sm = SeleniumManager()
    twit = TwitterManager()

    topic = choice(VIDEO_TOPIC)
    url, text = twit.get_tweet_data(topic)
    try:
        img = sm.screenshot_element(url, SeleniumManager.SELECTOR)
    except TimeoutException:
        return print("Failed to find selector")

    video = VideoManager.generate_video(img)
    tm = TiktokManager()
    tm.upload_video(f"{random_prefix()} {topic.capitalize()}! {gen_hashtags(topic)}", path.abspath(video))

if __name__ == "__main__":
    main()