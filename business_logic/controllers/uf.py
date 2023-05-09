from business_logic.adapters import sii_adapter
from datetime import date
from schemas import UF
from business_logic.exceptions import SIIException


def fetch_uf_value(target_date: date) -> UF:
    """
    Fetch the uf value based on a given date
    """
    year = target_date.year
    uf_year_data = sii_adapter.fetch_uf_by_year(year=year)

    if uf_year_data is None:
        raise SIIException

    month = target_date.month
    day = target_date.day
    uf_value = uf_year_data[day - 1][month - 1]

    return UF(uf_value=uf_value if uf_value != "" else None)
