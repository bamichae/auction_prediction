from ingestion.models.postings.vehicle import Vehicle


class DescriptiveVehicle(Vehicle):
    def __init__(self,
                 id,
                 name,
                 year,
                 make,
                 model,
                 body_style,
                 vin, odometer,
                 cylinders,
                 fuel_type,
                 transmission,
                 tire_condition,
                 is_operable,
                 is_startable,
                 keys_available,
                 ownership_documents,
                 mechanical_condition,
                 body_notes,
                 interior_condition,
                 titled):
        super().__init__(id, name, year, make)
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
