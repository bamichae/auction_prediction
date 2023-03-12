from ingestion.models.postings.mechanical import Mechanical


class Vehicle(Mechanical):
    def __init__(self,
                 id,
                 name,
                 year,
                 make):
        super().__init__(id, name, year, make)
