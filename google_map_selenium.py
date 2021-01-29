import requests, time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd

class Web_driver:
    def __init__(self, chrome_options=None):
        path = '$PATH_OF_CHROMEDRIVER'
        if chrome_options:
            chrome_options = Options()
            chrome_options.add_argument("--kiosk")
            chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(path, chrome_options=chrome_options)

    def get_map_of_destination(self, lat, lng, height):
        url = f'https://www.google.com.tw/maps/@{lat},{lng},{height}m/data=!3m1!1e3?hl=zh-TW'
        self.driver.get(url)
        
    def skip_sidebar(self):
        button = self.driver.find_element_by_class_name('searchbox-directions')
        button.click()
        time.sleep(3)
        button = self.driver.find_element_by_class_name('widget-directions-close')
        button.click()

    def screen_shot(self, image_name='image.png'):
        self.driver.save_screenshot(image_name)

class Web_driver:
    def __init__(self, chrome_options=None):
        path = '/home/herry/chromedriver_linux64/chromedriver'
        chrome_options = None
        if chrome_options:
            chrome_options = Options()
            chrome_options.add_argument("--kiosk")
            chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(path, chrome_options=chrome_options)
        url = f'https://www.google.com.tw/maps/@23.546162,120.6402133,8z?hl=zh-TW'
        self.driver.get(url)

    def search_place(self, place):
        def parser_latlng(url):
            l_latlng = url.split('@')[1].split(',')
            return {'lat': l_latlng[0], 'lng': l_latlng[1]}

        self.driver.refresh()
        searchbox = self.driver.find_element_by_id("searchboxinput")
        searchbox.send_keys(place)
        searchbox.send_keys(Keys.ENTER)
        time.sleep(5)
        return parser_latlng(self.driver.current_url)
