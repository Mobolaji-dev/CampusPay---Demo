# app/schemas/wallet.py
from pydantic import BaseModel

class WalletResponse(BaseModel):
    user_id: str
    role: str
    full_name: str
    available_balance: str
    locked_balance: str
    bank_account_number: str | None = None
    bank_name: str | None = None