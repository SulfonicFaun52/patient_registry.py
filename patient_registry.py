class PatientRegistry:
    """
    Manages patient records using a dictionary as a simulated database.
    """

    def __init__(self):
        self._patients = {}   # dictionary database
        self._next_id = 101   # starting ID

    def _generate_id(self):
        """Generate a unique patient ID"""
        pid = f"P-{self._next_id}"
        self._next_id += 1
        return pid

    # REQ-01
    def register_patient(self, name: str) -> str:
        """
        Creates a new patient record with a unique ID.
        """
        patient_id = self._generate_id()

        self._patients[patient_id] = {
            "patient_id": patient_id,
            "name": name
        }

        return patient_id

    # REQ-02
    def get_patient(self, patient_id: str) -> dict:
        """
        Retrieve a patient record using their ID.
        """
        if patient_id in self._patients:
            return self._patients[patient_id]
        else:
            raise ValueError("Patient ID not found.")

    # REQ-04
    def update_patient_name(self, patient_id: str, new_name: str) -> dict:
        """
        Update patient name while keeping ID unchanged.
        """
        if patient_id not in self._patients:
            raise ValueError("Patient ID not found.")

        self._patients[patient_id]["name"] = new_name
        return self._patients[patient_id]

    # REQ-05
    def delete_patient(self, patient_id: str) -> bool:
        """
        Delete a patient record.
        """
        if patient_id in self._patients:
            del self._patients[patient_id]
            return True
        else:
            raise ValueError("Patient ID not found.")

    def list_patients(self):
        """
        Return all patient records.
        """
        return list(self._patients.values())