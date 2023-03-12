from ingestion.models.postings.base_posting import BasePosting


class Mechanical(BasePosting):
    def __init__(self, id, name, year, make):
        super().__init__(id, name)
        self.year = year
        self.make = make
