"""
Page of all past postings
"""
import os
import select
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class PastSalesPage:
    def __init__(self):
        self.base_url = 'https://www.auctionsinternational.com/pastsales'
        self.driver = webdriver.Chrome()
        self.current_month_index = 0

    def past_sales_page(self):
        self.driver.get('https://www.auctionsinternational.com/pastsales')
        self.driver.implicitly_wait(2)

    def click_go(self):
        go_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/fieldset/table/tbody/tr[2]/td/form/input[1]')
        go_button.click()

    def select_month_dropdown(self, index):
        """
        Select the month
        :param index:
        :return:
        """
        drop_down_box = Select(self.driver.find_element(By.XPATH, '//*[@id="pastsales[months]"]'))
        drop_down_box.select_by_index(index)
        time.sleep(1)

    def get_total_months_to_query(self):
        """
        Get valid months of data that's queryable (starts at 1 due to default invalid month)
        :return:
        """
        drop_down_box = Select(self.driver.find_element(By.XPATH, '//*[@id="pastsales[months]"]'))
        options = drop_down_box.options
        return len(options) - 1
    def select_month(self):
        self.select_month_dropdown(self.current_month_index)

    def run(self):
        self.past_sales_page()
        for month_index in range(1, self.get_total_months_to_query()):
            self.select_month_dropdown(month_index)
            self.click_go()


