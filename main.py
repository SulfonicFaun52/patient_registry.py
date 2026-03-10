from patient_registry import PatientRegistry

def run_application():
    registry = PatientRegistry()

    while True:
        print("\nPatient Record System")
        print("1. Register a new patient")
        print("2. Retrieve patient by ID")
        print("3. Update patient name")
        print("4. Delete patient")
        print("5. List all patients")
        print("6. Go back")
        
        choice = input("Choose option (1-6): ")

        try:

            if choice == "1":
                name = input("Enter patient name: ")
                pid = registry.register_patient(name)
                print(f"Patient registered with ID: {pid}")

            elif choice == "2":
                pid = input("Enter patient ID: ")
                patient = registry.get_patient(pid)
                print(patient)

            elif choice == "3":
                pid = input("Enter patient ID: ")
                name = input("Enter new name: ")
                updated = registry.update_patient_name(pid, name)
                print("Updated record:", updated)

            elif choice == "4":
                pid = input("Enter patient ID: ")
                registry.delete_patient(pid)
                print("Patient deleted.")

            elif choice == "5":
                patients = registry.list_patients()

                if not patients:
                    print("No patients found.")
                else:
                    for p in patients:
                        print(p)

            elif choice == "6":
                break

            else:
                print("Please choose 1–6")

        except ValueError as e:
            print("Error:", e)


def main():

    while True:
        print("\nMain Menu")
        print("1. Run Application")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            run_application()

        elif choice == "2":
            print("Exiting system...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()1

