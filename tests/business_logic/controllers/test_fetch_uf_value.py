from business_logic.controllers.uf import fetch_uf_value
from datetime import date
from typing import Optional
import pytest
from business_logic.exceptions import SIIException


@pytest.mark.parametrize(
    "target_date, expected_value",
    [
        (date(2023, 3, 2), "35.529,90"),
        (date(2023, 2, 20), "35.428,93"),
        (date(2021, 7, 10), "29.737,50"),
        (date(2023, 12, 20), None),
    ],
)
def test_fetch_uf_value(target_date: date, expected_value: Optional[str]):
    """
    GIVEN   a `target_date`
    WHEN    the `fetch_uf_value` is called
    THEN    the returned value should math with the expected value
    """
    # GIVEN
    # WHEN
    returned_value = fetch_uf_value(target_date=target_date)

    # THEN
    assert expected_value == returned_value.uf_value


@pytest.mark.parametrize(
    "target_date",
    [
        date(2024, 3, 2),
        date(2012, 2, 20),
    ],
)
def test_invalid(target_date: date):
    """
    GIVEN   a invalid `target_date`
    WHEN    the `fetch_uf_value` is called
    THEN    should be raise an `SIIException`
    """
    # GIVEN
    # WHEN
    with pytest.raises(expected_exception=SIIException):
        # THEN
        fetch_uf_value(target_date=target_date)
