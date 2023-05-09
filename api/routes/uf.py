from fastapi import APIRouter, status, HTTPException

from business_logic.controllers import uf_controller
from datetime import date
from schemas import UF
from business_logic.exceptions import SIIException

router = APIRouter()


@router.get("/", response_model=UF, status_code=status.HTTP_200_OK)
def fetch_uf_value(target_date: date):
    """
    Fetch the uf value based on the given date
    """
    if target_date < date(2013, 1, 1):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Target date less than 2013-01-01",
        )

    try:
        return uf_controller.fetch_uf_value(target_date=target_date)
    except SIIException:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="There was an error with SII API",
        )
