from models import Patient, Address


def run_demo():
    address = Address(
        city="Karimnagar",
        state="Telangana",
        pin="35353"
    )

    patient = Patient(
        name="Li Xun",
        age=18,
        email="LandP@icici.com",
        weight=70.0,
        height=1.72,
        address=address,
        contact_details={"Discord": "raioku"}
    )

    print("Patient:", patient.name)
    print("BMI:", patient.bmi)
    print("JSON:", patient.model_dump_json())


if __name__ == "__main__":
    run_demo()