from docxtpl import DocxTemplate
import requests
import json

#  Code for spatial planning application search
search_radius = "0.3"  # search radius in KM - Note Keep as string!
postcode = "BA14 9DH"  # centre of search radius

"""
Alternative Location Format
Latitude = "..."
Longitude = "..."
"""

# Get data
applic_search_url = f"https://www.planit.org.uk/api/applics/json?krad={search_radius}&pcode={postcode}"
x = requests.get(applic_search_url)
# print(x.text)

x_dict = x.json()  # Convert to Dictionary
print(x_dict["records"][11])

doc = DocxTemplate("Files/planningTemplate.docx")

planningRows = []

for n in range(len(x_dict["records"])):
    print(n)
    address = x_dict["records"][n]["address"]
    areaName = x_dict["records"][n]["area_name"]
    description = x_dict["records"][n]["description"]
    consultedDate = x_dict["records"][n]["consulted_date"]
    decidedDate = x_dict["records"][n]["decided_date"]
    try:
        decision = x_dict["records"][n]["other_fields"]["decision"]
    except KeyError:
        decision = ""

    planningRows.append({"address": address, "areaName": areaName, "description": description,
                         "consultDate": consultedDate, "decideDate": decidedDate, "decision": decision})

context = {
    "planningRows": planningRows
}

doc.render(context)

doc.save("Files/Example.docx")
