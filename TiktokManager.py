from re import L
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent, FakeUserAgentError
import os

class TiktokManager:
    CAPTION_SELECTOR = "public-DraftStyleDefault-block"
    VIDEO_SELECTOR = ".jsx-1545465582.file"
    POST_SELECTOR = "button.css-n99h88"
    TIMEOUT = 5
    VIDEO_TIMEOUT = 60

    def __init__(self):
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument(
            f"user-agent={self.__get_user_agent()}")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--user-data-dir=C:/Users/Cameron/Documents/autoshortmaker/chrome_data')
        chrome_options.add_argument('--no-first-run --no-service-autorun --password-store=basic')

        self.driver = uc.Chrome(options=chrome_options)

    def upload_video(self, caption, video_path):
        self.driver.get('https://www.tiktok.com/upload?lang=en')
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        self.driver.switch_to.frame(0)
        self.driver.implicitly_wait(1)

        self.__set_caption(caption)
        self.__set_video(video_path)

        WebDriverWait(self.driver, self.VIDEO_TIMEOUT).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.VIDEO_SELECTOR)))
        self.driver.implicitly_wait(1)

        post_button = self.driver.find_element(By.CSS_SELECTOR, self.POST_SELECTOR)
        post_button.click()
        print("Post button clicked!")

        time.sleep(10)

    def __set_caption(self, caption):
        element = self.driver.find_element(By.CLASS_NAME, self.CAPTION_SELECTOR)
        element.send_keys(caption)

    def __set_video(self, video_path):
        element = self.driver.find_element(By.TAG_NAME, "input")
        element.send_keys(video_path)

    def __get_user_agent(self) -> str:
        try:
            return UserAgent().chrome
        except FakeUserAgentError:
            return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"

    def destroy(self):
        self.driver.quit()
