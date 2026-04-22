# Retrieve Hawaii mortgage rates

import requests
from bs4 import BeautifulSoup

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find_all("tr")

print("Bank and Rates:\n")

current_bank = ""

for row in rows:
    cols = row.find_all("td")
    cols = [col.get_text(strip=True) for col in cols]

    if len(cols) == 5:
        # This row has bank name
        current_bank = cols[0]
        term = cols[1]
        rate = cols[2]

    elif len(cols) == 4:
        # This row continues same bank
        term = cols[0]
        rate = cols[1]
    else:
        continue

    print(f"{current_bank} | {term} | {rate}")