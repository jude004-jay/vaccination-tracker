# Vaccination Tracker

A Python program built with Object-Oriented Programming (OOP) that tracks vaccinations in a community clinic. It was created for **PROG211 Object-Oriented Programming 1** (Health domain) at Limkokwing University of Creative Technology, Sierra Leone.

## Problem Solved

Clinics often find it hard to keep track of which patients have received which vaccine doses. This program records each dose given to a patient and checks whether the patient has completed the full vaccine course.

## Project Structure

| File | Purpose |
|---|---|
| `models.py` | Contains the classes: `Vaccine`, `VaccinationRecord`, `Patient` and `Clinic` |
| `main.py` | Demo program that creates objects and shows them interacting |
| `LICENSE` | MIT open-source licence |
| `README.md` | Project documentation |

## OOP Concepts Used

- **Classes and objects:** four classes, each with attributes and methods. Objects interact: a `Clinic` holds `Patient` objects, a `Patient` holds `VaccinationRecord` objects, and each record refers to a `Vaccine`.
- **Data structure (dictionary):** `Clinic.patients` stores all patients using their unique ID as the key. `add_patient()` and `display_all_patients()` add and display the records.
- **Tuple:** `Vaccine.dose_schedule_days` stores a fixed dose schedule, e.g. `(0, 28)`.
- **Instance methods:** `add_dose()`, `is_fully_vaccinated()` and `display_info()`.
- **Class method:** `Patient.generate_id()` uses a class-level counter to create unique IDs (P001, P002, ...).

## How This Solution Meets Digital Public Goods (DPG) Standards

1. **Open-source:** The full source code is public on GitHub under the MIT licence, so anyone can use, study, modify and share it.
2. **Inclusive and accessible design:** The program uses only standard Python, with no paid software, internet connection or special hardware. The output is clear plain text that works with screen readers and on low-spec computers.
3. **Privacy-respecting:** No sensitive personal data is stored. There are no names, phone numbers or addresses. Each patient is identified only by an automatically generated ID (e.g. `P001`) and an age.
4. **Modular and reusable:** The data classes in `models.py` are kept separate from the demo in `main.py`. Other developers can import the classes into their own projects, such as a larger health information system, without changing them.

## How to Run

1. Install [Python 3](https://www.python.org/downloads/).
2. Download or clone this repository.
3. Open a terminal in the project folder and run:

```
python main.py
```

## Example Usage (Sample Output)

```
--- Available vaccines ---
COVID-19: 2 dose(s), schedule (days from first dose): (0, 28)
Measles: 1 dose(s), schedule (days from first dose): (0,)
P001 already completed COVID-19.

=== Freetown Community Clinic: 2 patient(s) ===
Patient P001 | Age: 25
   - COVID-19, dose 1 on 2026-10-28
   - COVID-19, dose 2 on 2026-10-28
Patient P002 | Age: 4
   - Measles, dose 1 on 2026-10-28

--- Status check ---
P001 fully vaccinated against COVID-19? True
P002 fully vaccinated against COVID-19? False
```

The program creates two vaccines and two patients, records doses, refuses a third COVID-19 dose for P001 because the course is already complete, and then reports each patient's vaccination status.

## Author

**Name:** YOUR FULL NAME
**Student ID:** YOUR STUDENT ID
**Course:** PROG211 Object-Oriented Programming 1
**Institution:** Limkokwing University of Creative Technology, Sierra Leone

## Licence

This project is released under the MIT Licence. See the `LICENSE` file for details.