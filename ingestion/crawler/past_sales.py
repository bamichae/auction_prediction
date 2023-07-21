"""
Page of all past postings
"""
import os

from selenium import webdriver
from os.path import join, dirname, realpath
class PastSales:
    def __int__(self):
        self.base_url = 'https://www.auctionsinternational.com/pastsales'
        self.driver = None

        self.initialize()

    def initialize(self):
        # TODO: get chromedriver working
        webdriver_path = join(dirname(dirname(realpath(__file__))), 'chromedriver_linux64', 'chromedriver')
        self.driver = webdriver.Chrome()

    def click_go(self):
        pass

    def home_page(self):
        self.driver.get(self.base_url)

    def run(self):
        self.home_page()