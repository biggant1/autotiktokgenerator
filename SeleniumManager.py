from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import os

class SeleniumManager:
    SELECTOR = "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > section > div > div > div:nth-child(1) > div > div > div > article"
    LOGIN_SELECTOR = "#layers > div"
    REPLY_SELECTOR = "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > section > div > div > div:nth-child(1) > div > div > div > article > div > div > div > div:nth-child(3) > div.css-1dbjc4n.r-1ifxtd0.r-1s2bzr4"
    TIMEOUT=5

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

        chrome_service = Service(os.getenv("CHROME_DRIVER"))

        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.driver.execute_script("window.open('');")

    def __remove_element(self, element: str):
        self.driver.execute_script(f"""
            let element = document.querySelector('{element}');
            if(element) element.remove();
        """)

    def screenshot(self, url: str):
        return self.screenshot_element(url, "html")

    def screenshot_element(self, url: str, element: str):
        self.driver.get(url)
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))

        self.__remove_element(self.LOGIN_SELECTOR)
        self.__remove_element(self.REPLY_SELECTOR)
        elem = self.driver.find_element(By.CSS_SELECTOR, element)
        self.driver.set_window_size(1920, elem.size["height"] + 1000)

        img = elem.screenshot_as_png
        pil_img = Image.open(BytesIO(img))
        return pil_img
    
    def destroy(self):
        self.driver.quit()

