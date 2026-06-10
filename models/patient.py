from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated


class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):

    name: Annotated[
        str,
        Field(
            max_length=50,
            title="Name of the Patient",
            description="The length of the name should be less than 50",
            examples=["Rahul", "Ramesh"],
        ),
    ]

    age: int = Field(gt=0, lt=120)
    email: Optional[EmailStr] = None
    linked_in_Url: Optional[AnyUrl] = None
    gender: str = "Male"

    weight: Annotated[float, Field(gt=0, strict=True)]
    height: Annotated[float, Field(gt=0)]

    married: Annotated[
        bool,
        Field(default=False, description="Is the patient married or not"),
    ]

    address: Address

    allergies: Optional[List[str]] = Field(default=None)
    contact_details: Dict[str, str]

    @field_validator("email", mode="after")
    @classmethod
    def email_validator(cls, value):
        if value is None:
            return value
        valid_domains = ["hdfc.com", "icici.com"]
        domain_name = value.split("@")[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        return value

    @field_validator("name", mode="after")
    @classmethod
    def transform(cls, value):
        return value.upper()

    @model_validator(mode="after")
    def validate_emergency_contact(model):
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError("Patients older than 60 must have an emergency contact")
        return model

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height) ** 2, 2)