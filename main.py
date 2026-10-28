from models import Vaccine, Clinic


def main():
    # Create vaccine objects (schedules are tuples)
    covid = Vaccine("COVID-19", 2, (0, 28))
    measles = Vaccine("Measles", 1, (0,))

    print("--- Available vaccines ---")
    covid.display_info()
    measles.display_info()

    # Create the clinic and patients (objects interacting)
    clinic = Clinic("Freetown Community Clinic")
    p1 = clinic.add_patient(age=25)
    p2 = clinic.add_patient(age=4)

    # Record doses
    p1.add_dose(covid)
    p1.add_dose(covid)
    p1.add_dose(covid)      # should be refused: already completed
    p2.add_dose(measles)

    clinic.display_all_patients()

    print("\n--- Status check ---")
    print(f"{p1.patient_id} fully vaccinated against COVID-19? "
          f"{p1.is_fully_vaccinated(covid)}")
    print(f"{p2.patient_id} fully vaccinated against COVID-19? "
          f"{p2.is_fully_vaccinated(covid)}")


if __name__ == "__main__":
    main()