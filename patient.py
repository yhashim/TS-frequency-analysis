from asyncio.windows_events import NULL
from contextlib import nullcontext
import imp

patients = []

class Patient:
    def __init__(self, first_name, last_name, gender, diagnosis, implant_date):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.diagnosis = diagnosis
        self.implant_date = implant_date

        self.channel_coordinates = []
        self.coordinates = []

        self.graphs = []

        patients.append(self)

    def __repr__(self):
        return "first name: %s, last name: %s, gender: %s, diagnosis: %s, implant date: %s" % (self.first_name, self.last_name, self.gender, self.diagnosis, self.implant_date)
