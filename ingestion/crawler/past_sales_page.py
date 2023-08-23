"""
Page of all past postings
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from ingestion.crawler.posting import Posting


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
        self.click_go()
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

    def select_auction_item_link(self, link_text):
        self.driver.get(link_text)
        time.sleep(1)

    def get_auction_links(self):
        """
        Get auction links from month page
        :return:
        """
        links = []
        # Get href from <a /> tag
        auction_items = self.driver.find_elements(By.XPATH, "//a[contains(@href, '/auction/') and contains(@href, '/item/')]")

        # Store auction links
        for auction_item in auction_items:
            links.append(auction_item.get_property('href'))
        return links

    def run(self):
        test = []
        # Home page
        self.past_sales_page()
        for month_index in range(1, self.get_total_months_to_query()):
            # Click month
            self.select_month_dropdown(month_index)

            # Search for links
            auction_links = self.get_auction_links()
            for auction_link in auction_links:
                # Click links
                print(auction_link)
                posting = Posting()
                test.append(posting.store_details(auction_link))

            # Return to home page
            self.past_sales_page()
