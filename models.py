"""Core classes for the Vaccination Tracker.
Privacy note: no names, phone numbers or addresses are stored.
Patients are identified only by a generated ID and an age.
"""
from datetime import date


class Vaccine:
    """Describes a type of vaccine."""

    def __init__(self, name, doses_required, dose_schedule_days):
        self.name = name
        self.doses_required = doses_required
        self.dose_schedule_days = dose_schedule_days  # tuple, e.g. (0, 28)

    def display_info(self):
        print(f"{self.name}: {self.doses_required} dose(s), "
              f"schedule (days from first dose): {self.dose_schedule_days}")


class VaccinationRecord:
    """One dose of one vaccine given to a patient."""

    def __init__(self, vaccine, dose_number, date_given=None):
        self.vaccine = vaccine
        self.dose_number = dose_number
        self.date_given = date_given or date.today()

    def display_info(self):
        print(f"   - {self.vaccine.name}, dose {self.dose_number} "
              f"on {self.date_given}")


class Patient:
    """An anonymous patient identified only by ID and age."""

    _counter = 0  # class attribute shared by all patients

    def __init__(self, patient_id, age):
        self.patient_id = patient_id
        self.age = age
        self.records = []

    @classmethod
    def generate_id(cls):
        """Class method: creates the next unique ID (P001, P002, ...)."""
        cls._counter += 1
        return f"P{cls._counter:03d}"

    def doses_received(self, vaccine):
        """Count how many doses of this vaccine the patient has had."""
        return sum(1 for r in self.records if r.vaccine.name == vaccine.name)

    def add_dose(self, vaccine):
        """Instance method: record the next dose of a vaccine."""
        if self.is_fully_vaccinated(vaccine):
            print(f"{self.patient_id} already completed {vaccine.name}.")
            return None
        dose_number = self.doses_received(vaccine) + 1
        record = VaccinationRecord(vaccine, dose_number)
        self.records.append(record)
        return record

    def is_fully_vaccinated(self, vaccine):
        return self.doses_received(vaccine) >= vaccine.doses_required

    def display_info(self):
        print(f"Patient {self.patient_id} | Age: {self.age}")
        if not self.records:
            print("   (no vaccinations recorded)")
        for record in self.records:
            record.display_info()


class Clinic:
    """Manages patients. Uses ONE data structure: a dictionary (ID -> Patient)."""

    def __init__(self, name):
        self.name = name
        self.patients = {}

    def add_patient(self, age):
        """Create a patient with a generated ID and store it."""
        patient = Patient(Patient.generate_id(), age)
        self.patients[patient.patient_id] = patient
        return patient

    def get_patient(self, patient_id):
        return self.patients.get(patient_id)

    def display_all_patients(self):
        print(f"\n=== {self.name}: {len(self.patients)} patient(s) ===")
        for patient in self.patients.values():
            patient.display_info()