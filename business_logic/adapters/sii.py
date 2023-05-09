import requests
from bs4 import BeautifulSoup
import logging
from typing import Optional, List

logger = logging.getLogger(__name__)


def fetch_uf_by_year(year: int) -> Optional[List[List[str]]]:
    """
    Fetch uf data by year from `Servicio de Impuestos Internos (SII) de Chile`
    Returns `None` if some error occurs
    """
    try:
        url = f"https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm"
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")

        try:
            table = soup.find_all("table")[-1]
            table_values = []
            rows = table.find_all("tr")
            for row in rows:
                row_values = []
                cells = row.find_all("td")
                for cell in cells:
                    row_values.append(cell.text.strip())
                if row_values:
                    table_values.append(row_values)
            return table_values
        except IndexError as e:
            return None
    except Exception as e:
        return None
