# ---------------- PATIENT MANAGEMENT ----------------

def load_patients():
    records = []
    try:
        with open("PATIENT_FILE", "r") as file:
            for line in file:
                line = line.strip()
                if line != "":
                    records.append(line.split("|"))
    except FileNotFoundError:
        pass
    except OSError:
        print("Could not read patient records.")
    return records

def save_patients():
    try:
        with open("PATIENT_FILE", "a") as file:
            for patient in patients:
                file.write("|".join(patient) + "\n")
    except OSError:
        print("Could not save patient records.")

patients = load_patients()

def register_patient():
    patient_id = input("Enter patient ID: ").strip().upper()

    for patient in patients:
        if patient[0] == patient_id:
            print("Patient ID already exists.")
            return

    name = input("Enter patient name: ").strip()
    age1 = input("Enter patient age: ").strip()
    department = input("Enter department: ").strip()

    try:
        age = int(age1)
        if age <= 0:
            print("Age must be positive.")
            return
    except ValueError:
        print("Please enter a valid age.")
        return

    if patient_id == "" or name == "" or department == "":
        print("All details are required.")
        return

    patients.append([patient_id, name, str(age), department])
    save_patients()
    print("Patient registered successfully.")


def show_patients():
    if len(patients) == 0:
        print("No patients registered.")
        return

    print("\n--- PATIENT RECORDS ---")
    for patient in patients:
        print("ID:", patient[0], "| Name:", patient[1],
              "| Age:", patient[2], "| Department:", patient[3])


# ---------------- DOCTOR MANAGEMENT ----------------

def load_doctors():
    records = []
    try:
        with open("DOCTOR_FILE", "r") as file:
            for line in file:
                line = line.strip()
                if line != "":
                    records.append(line.split("|"))
    except FileNotFoundError:
        pass
    except OSError:
        print("Could not read doctor records.")
    return records


def save_doctors():
    try:
        with open("DOCTOR_FILE", "w") as file:
            for doctor in doctors:
                file.write("|".join(doctor) + "\n")
    except OSError:
        print("Could not save doctor records.")


doctors = load_doctors()


class Doctor:
    def __init__(self, doctor_id, name, department):
        self.doctor_id = doctor_id
        self.name = name
        self.department = department

    def calculate_consultation_fee(self):
        return 300


class GeneralPhysician(Doctor):
    def calculate_consultation_fee(self):
        return 300


class Specialist(Doctor):
    def calculate_consultation_fee(self):
        return 600


class Surgeon(Doctor):
    def calculate_consultation_fee(self):
        return 1000


def get_doctor_fee(doctor):
    if doctor[3] == "Specialist":
        doctor_object = Specialist(doctor[0], doctor[1], doctor[2])
    elif doctor[3] == "Surgeon":
        doctor_object = Surgeon(doctor[0], doctor[1], doctor[2])
    else:
        doctor_object = GeneralPhysician(doctor[0], doctor[1], doctor[2])
    return doctor_object.calculate_consultation_fee()


def add_sample_doctors():
    if len(doctors) == 0:
        doctors.append(["D101", "Aman Sharma", "General Medicine", "GeneralPhysician"])
        doctors.append(["D102", "Neha Verma", "Cardiology", "Specialist"])
        doctors.append(["D103", "Rahul Mehta", "Surgery", "Surgeon"])
        save_doctors()


def show_doctors():
    if len(doctors) == 0:
        print("No doctors available.")
        return

    print("\n--- DOCTOR RECORDS ---")
    for doctor in doctors:
        print("ID:", doctor[0], "| Name:", doctor[1],
              "| Department:", doctor[2], "| Type:", doctor[3],
              "| Consultation Fee: Rs.", get_doctor_fee(doctor))


def add_doctor():
    doctor_id = input("Enter doctor ID: ").strip().upper()

    for doctor in doctors:
        if doctor[0] == doctor_id:
            print("Doctor ID already exists.")
            return

    name = input("Enter doctor name: ").strip()
    department = input("Enter department: ").strip()

    print("1. General Physician (Rs. 300)")
    print("2. Specialist (Rs. 600)")
    print("3. Surgeon (Rs. 1000)")
    choice = input("Choose doctor type: ").strip()

    if choice == "1":
        doctor_type = "GeneralPhysician"
    elif choice == "2":
        doctor_type = "Specialist"
    elif choice == "3":
        doctor_type = "Surgeon"
    else:
        print("Invalid doctor type.")
        return

    if doctor_id == "" or name == "" or department == "":
        print("All details are required.")
        return

    doctors.append([doctor_id, name, department, doctor_type])
    save_doctors()
    print("Doctor added successfully.")


# ---------------- MAIN MENU ----------------

add_sample_doctors()

while True:
    print("\n====== MODULE 1: PATIENT AND DOCTOR MANAGEMENT ======")
    print("1. Register patient")
    print("2. Show patients")
    print("3. Show doctors")
    print("4. Add doctor")
    print("0. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        register_patient()
    elif choice == "2":
        show_patients()
    elif choice == "3":
        show_doctors()
    elif choice == "4":
        add_doctor()
    elif choice == "0":
        print("Exiting Module 1.")
        break
    else:
        print("Invalid choice. Try again.")


