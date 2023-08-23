import logging

from selenium import webdriver
from selenium.webdriver.common.by import By

import logging
logging.basicConfig(level=logging.DEBUG)

from ingestion.models.postings.descriptive_vehicle import DescriptiveVehicle


class DescriptiveVehiclePosting:
    def __init__(self, auction_link):
        self.descriptive_posting = DescriptiveVehicle()
        self.auction_link = auction_link

    def parse_posting(self):
        self.parse_description()

    def parse_description(self):
        # Get webdriver
        driver = webdriver.Chrome()
        driver.get(self.auction_link)

        # Get descriptive div
        description_detail_div = driver.find_element(By.ID, 'details-description')
        description_details = description_detail_div.find_elements(By.TAG_NAME, 'li')

        # Description detail
        for description_detail in description_details:
            self.assign_field(description_detail.text)

    def assign_field(self, field):
        field = field.lower()
        key, value = field.split(':')
        if 'fleet #' == key:
            self.descriptive_posting.fleet = value
        elif 'year' == key:
            self.descriptive_posting.year = value
        elif 'make' == key:
            self.descriptive_posting.make = value
        elif 'model' == key:
            self.descriptive_posting.model = value
        elif 'body style' == key:
            self.descriptive_posting.body_style = value
        elif 'vin/sn' == key:
            self.descriptive_posting.vin = value
        elif 'odometer numbers' == key:
            self.descriptive_posting.odometer = value
        elif 'cyl' == key:
            self.descriptive_posting.cylinders = value
        elif 'fuel type' == key:
            self.descriptive_posting.fuel_type = value
        elif 'transmission type' == key:
            self.descriptive_posting.transmission = value
        elif 'tire condition' == key:
            self.descriptive_posting.tire_condition = value
        elif 'does the unit operate?' == key:
            self.descriptive_posting.is_operable = value
        elif 'does the vehicle start?' == key:
            self.descriptive_posting.is_startable = value
        elif 'are keys available?' == key:
            self.descriptive_posting.keys_available = value
        elif 'ownership documents' == key:
            self.descriptive_posting.ownership_documents = value
        elif 'mechanical condition' == key:
            self.descriptive_posting.mechanical_condition = value
        elif 'body notes' == key:
            self.descriptive_posting.body_notes = value
        elif 'interior condition' == key:
            self.descriptive_posting.interior_condition = value
        else:
            logging.info(f'Skipped field: {key}:{value}')
