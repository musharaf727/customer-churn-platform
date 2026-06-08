from pydantic import BaseModel


class Customer(BaseModel):

    Gender: str

    MonthlyCharges: float

    TenureMonths: int

    Contract: str