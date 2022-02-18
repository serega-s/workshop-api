from decimal import Decimal
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from datetime import date

# choices


class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class OperationBase(BaseModel):
    date: date
    kind: OperationKind
    amount: Decimal
    description: Optional[str]


class Operation(OperationBase):
    id: int

    class Config:
        orm_mode = True


class OperationCreate(OperationBase):
    ...


class OperationUpdate(OperationBase):
    ...