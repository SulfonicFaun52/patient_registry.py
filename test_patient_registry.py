import pytest
from patient_registry import PatientRegistry


def setup_registry():
    return PatientRegistry()


# ---------- UNIT TESTS ----------

def test_register_patient():
    registry = setup_registry()
    pid = registry.register_patient("Ryan")
    assert pid.startswith("P-")
    assert registry.get_patient(pid)["name"] == "Ryan"


def test_get_patient():
    registry = setup_registry()
    pid = registry.register_patient("Alice")
    patient = registry.get_patient(pid)
    assert patient["patient_id"] == pid


def test_update_patient():
    registry = setup_registry()
    pid = registry.register_patient("Bob")
    updated = registry.update_patient_name(pid, "New Bob")
    assert updated["name"] == "New Bob"


def test_delete_patient():
    registry = setup_registry()
    pid = registry.register_patient("Charlie")
    registry.delete_patient(pid)

    with pytest.raises(ValueError):
        registry.get_patient(pid)


def test_invalid_get():
    registry = setup_registry()
    with pytest.raises(ValueError):
        registry.get_patient("P-999")


# ---------- COMPONENT TEST ----------

def test_workflow():
    registry = PatientRegistry()

    pid = registry.register_patient("Ryan")
    registry.update_patient_name(pid, "Updated Ryan")
    patient = registry.get_patient(pid)

    assert patient["name"] == "Updated Ryan"
    assert patient["patient_id"] == pid