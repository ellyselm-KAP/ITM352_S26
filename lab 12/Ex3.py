# Parse the ITM Department website to find the people

import urllib.request
from bs4 import BeautifulSoup

itm_url = "https://shidler.hawaii.edu/itm/people"

itm_html = urllib.request.urlopen(itm_url)
html_to_parse = BeautifulSoup(itm_html, "html.parser")

print("Object type:")
print(type(html_to_parse))

print("\nFirst few lines of prettify():")
pretty_html = html_to_parse.prettify().split("\n")
for line in pretty_html[:15]:
    print(line)

# Find and print names of ITM people
list_of_people = html_to_parse.find_all("h2", class_="title")

itm_people = []
for person in list_of_people:
    name = person.text.strip()
    itm_people.append(name)
    print(name)

print("\nTotal people found:", len(itm_people))