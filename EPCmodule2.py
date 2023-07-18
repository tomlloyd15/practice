

import requests
import json
import pandas as pd

def get_epc_report(auth_token, postcode, building_name=None, address=None):
    domestic_base_url = "https://epc.opendatacommunities.org/api/v1/domestic/search"
    non_domestic_base_url = "https://epc.opendatacommunities.org/api/v1/non-domestic/search"

    domestic_params = {"postcode": postcode}
    non_domestic_params = {"postcode": postcode}

    if building_name:
        domestic_params["buildingname"] = building_name
        non_domestic_params["buildingname"] = building_name

    if address:
        domestic_params["address"] = address
        non_domestic_params["address"] = address

    headers = {
        "Authorization": f"Basic {auth_token}",
        "Accept": "application/json"
    }

    epc_data = []

    domestic_response = requests.get(domestic_base_url, params=domestic_params, headers=headers)
    non_domestic_response = requests.get(non_domestic_base_url, params=non_domestic_params, headers=headers)

    try:
        if domestic_response.status_code == 200:
            domestic_epc_data = json.loads(domestic_response.text)
            if 'rows' in domestic_epc_data and domestic_epc_data['rows']:
                epc_data.extend(domestic_epc_data['rows'])
    except json.JSONDecodeError:
        print("Error: Invalid JSON response for domestic EPC data.")

    try:
        if non_domestic_response.status_code == 200:
            non_domestic_epc_data = json.loads(non_domestic_response.text)
            if 'rows' in non_domestic_epc_data and non_domestic_epc_data['rows']:
                epc_data.extend(non_domestic_epc_data['rows'])
    except json.JSONDecodeError:
        print("Error: Invalid JSON response for non-domestic EPC data.")
    
    # Create a pandas DataFrame and print the table
    if epc_data:
        df = pd.DataFrame(epc_data)
        print(df[['address', 'current-energy-rating']])


if __name__ == "__main__":
    auth_token = "dG9ieXdpbGtpbnMxQGdtYWlsLmNvbTo0ZTc5OGNkY2U3ZjdjN2Q0ZTY2ZWVlZjdmMGQxNzI4YTNlZjc4YThk"
    postcode = "SW14 8LE"
    building_name = None
    address = None

    get_epc_report(auth_token, postcode, building_name, address)
