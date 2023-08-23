from selenium import webdriver
from selenium.webdriver.common.by import By

from ingestion.models.postings.vehicle import Vehicle


class DescriptiveVehicle(Vehicle):
    def __init__(self,
                 identifier=None,
                 name=None,
                 year=None,
                 make=None,
                 model=None,
                 fleet=None,
                 body_style=None,
                 vin=None,
                 odometer=None,
                 cylinders=None,
                 fuel_type=None,
                 transmission=None,
                 tire_condition=None,
                 is_operable=None,
                 is_startable=None,
                 keys_available=None,
                 ownership_documents=None,
                 mechanical_condition=None,
                 body_notes=None,
                 interior_condition=None,
                 titled=None):
        super().__init__(identifier, name, year, make)
        self.fleet = fleet
        self.model = model
        self.body_style = body_style
        self.vin = vin
        self.odometer = odometer
        self.cylinders = cylinders
        self.fuel_type = fuel_type
        self.transmission = transmission
        self.tire_condition = tire_condition
        self.is_operable = is_operable
        self.is_startable = is_startable
        self.keys_available = keys_available
        self.ownership_documents = ownership_documents
        self.mechanical_condition = mechanical_condition
        self.body_notes = body_notes
        self.interior_condition = interior_condition
        self.titled = titled

    @staticmethod
    def is_descriptive_vehicle(auction_link, fields_threshold=10):
        """

        :param auction_link:
        :param fields_threshold: Min number of fields to be descriptive vehicle
        :return:
        """
        descriptive_lookup = DescriptiveVehicle.get_descriptive_lookup()

        # Get Chrome driver
        driver = webdriver.Chrome()
        driver.get(auction_link)

        # Look for details description box
        description_detail_div = driver.find_element(By.ID, 'details-description')
        if not description_detail_div:
            return False

        # Get details of description and count how many details there are
        description_details = description_detail_div.find_elements(By.TAG_NAME, 'li')
        field_count = len([x for x in description_details if x.text.lower().split(':')[0] in descriptive_lookup])
        if field_count >= fields_threshold:
            return True
        else:
            return False


    @staticmethod
    def get_descriptive_lookup():
        """
        Since auction details can be missing, create a set of all details I've seen to check for existence of them.
        :return: set of details of a descriptive vehicle
        """
        return {
            'fleet #',
            'year',
            'make',
            'model',
            'body style',
            'vin/sn',
            'odometer numbers',
            'engine make/model',
            'cyl',
            'fuel type',
            'transmission type',
            'single axle/dual axle',
            'tire size/type',
            'tire condition',
            'drivetrain',
            'does the unit operate?',
            'does the vehicle start?',
            'are keys available?',
            'ownership documents',
            'mechanical condition',
            'mechanical notes',
            'body condition',
            'body notes',
            'interior condition'
        }



