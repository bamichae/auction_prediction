"""
Specific posting
"""
from selenium import webdriver

from ingestion.crawler.descriptive_vehicle_posting import DescriptiveVehiclePosting
from ingestion.models.postings.descriptive_vehicle import DescriptiveVehicle


class Posting:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_specific_posting(self, auction_link):
        if DescriptiveVehicle.is_descriptive_vehicle(auction_link):
            return DescriptiveVehiclePosting(auction_link)

        # TODO: Add more options
        return None

    def store_details(self, auction_link):
        specific_posting = self.get_specific_posting(auction_link)
        # TODO: remove at some point
        if not specific_posting:
            return
        specific_posting.parse_posting()
        return specific_posting

