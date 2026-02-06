from pydantic import BaseModel

class CorepOutput(BaseModel):
    capital_type: str
    amount: str
    risk_weight: str
    template_section: str
