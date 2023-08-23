from ingestion.models.postings.mechanical import Mechanical


class Vehicle(Mechanical):
    def __init__(self,
                 identifier=None,
                 name=None,
                 year=None,
                 make=None):
        super().__init__(identifier, name, year, make)
