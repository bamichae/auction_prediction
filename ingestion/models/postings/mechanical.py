from ingestion.models.postings.base_posting import BasePosting


class Mechanical(BasePosting):
    def __init__(self,
                 identifier=None,
                 name=None,
                 year=None,
                 make=None):
        super().__init__(identifier, name)
        self.year = year
        self.make = make
