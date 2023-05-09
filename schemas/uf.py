from pydantic import BaseModel
from typing import Optional


class UF(BaseModel):
    uf_value: Optional[str]
