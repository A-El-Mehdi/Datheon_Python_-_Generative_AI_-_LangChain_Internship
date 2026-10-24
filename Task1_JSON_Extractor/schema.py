from pydantic import BaseModel

class Invoice(BaseModel):
    invoice_number: str | None = None
    date: str | None = None
    vendor: str
    total: float
    currency: str