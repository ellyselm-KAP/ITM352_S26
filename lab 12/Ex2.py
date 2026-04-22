# Grab 1 month interest rate data from the Treasury website

import ssl
import pandas as pd
import urllib.request
import lxml

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603"

ssl._create_default_https_context = ssl._create_unverified_context

print("Opening URL:", url)
web_page = urllib.request.urlopen(url)

# read_html returns a list of tables
tables = pd.read_html(web_page)

# use the first table
int_rate_table = tables[0]

print("\nColumn names:")
print(int_rate_table.columns)

print("\n1 Month Treasury Rates:\n")
for index, row in int_rate_table.iterrows():
    print(f"Date: {row['Date']}, 1 Mo Rate: {row['1 Mo']}")