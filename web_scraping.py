import json

import cyrtranslit
import requests
from bs4 import BeautifulSoup
import pandas as pd
import converter


class Web_scraping:

    def web_scraping(self, day=1, city="beograd"):

        match city:
            case "beograd":
                url = f"https://elektrodistribucija.rs/planirana-iskljucenja-beograd/Dan_{day}_Iskljucenja.htm"

            case "novi_sad":
                url = f"https://elektrodistribucija.rs/planirana-iskljucenja-srbija/NoviSad_Dan_{day}_Iskljucenja.htm"

            case "kraljevo":
                url = f"https://elektrodistribucija.rs/planirana-iskljucenja-srbija/Kragujevac_Dan_{day}_Iskljucenja.htm"

            case "kragujevac":
                url = f"https://elektrodistribucija.rs/planirana-iskljucenja-srbija/Kragujevac_Dan_{day}_Iskljucenja.htm"

            case "nis":
                url = f"https://elektrodistribucija.rs/planirana-iskljucenja-srbija/Nis_Dan_{day}_Iskljucenja.htm"
            case _:
                url = f"https://elektrodistribucija.rs/planirana-iskljucenja-beograd/Dan_{day}_Iskljucenja.htm"

        # EPS URL

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15',
        }

        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            values = soup.findAll('table')[1]('tr')

            data = []
            if city == "beograd":
                for row in values:
                    cell = row.find_all('td')
                    opstina = cell[0].get_text()
                    vreme = cell[1].get_text()
                    adresa = cell[2].get_text()

                    data.append([opstina, vreme, adresa])
            else:
                for row in values:
                    cell = row.find_all('td')
                    ogranak = cell[0].get_text()
                    opstina = cell[1].get_text()
                    vreme = cell[2].get_text()
                    adresa = cell[3].get_text()

                    data.append([ogranak, opstina, vreme, adresa])

            return data

        except Exception as error:
            print('Caught this error: ' + repr(error))

    def export_csv(self, data):
        try:
            df = pd.DataFrame(data, columns=['opstina', 'vreme', 'adresa'])
            df.to_csv('data.csv', index=False)
        except Exception as e:
            print(f"Error is {e}")
