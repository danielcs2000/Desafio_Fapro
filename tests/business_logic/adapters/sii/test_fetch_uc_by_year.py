from business_logic.adapters.sii import fetch_uf_by_year
import pytest


@pytest.mark.parametrize(
    "year", [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
)
def test_fetch_uf_by_year(year: int):
    """
    GIVEN   a year
    WHEN    the `fetch_uf_by_year` is called
    THEN    a table with all data by year should be returned
    """
    # GIVEN
    # WHEN
    table_data = fetch_uf_by_year(year=year)

    # THEN
    assert table_data is not None
    assert len(table_data) == 31
    assert all(len(data) == 12 for data in table_data)
