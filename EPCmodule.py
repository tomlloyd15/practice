#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 13:59:50 2023

@author: toby
"""
import requests
import json
import csv

def get_epc_report(auth_token, postcode, building_name=None, address=None):
    

    
    base_url = "https://epc.opendatacommunities.org/api/v1/domestic/search"

    params = {
        "postcode": postcode,
    }

    if building_name:
        params["buildingname"] = building_name
    if address:
        params["address"] = address

    headers = {
        "Authorization": f"Basic {auth_token}",
        "Accept": "application/json"
    }

    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        epc_data = json.loads(response.text)
        return epc_data['rows']  # Return only the 'rows' part of the response
    else:
        print(f"Error: Unable to fetch EPC data. (HTTP {response.status_code})")
        return None

if __name__ == "__main__":
    auth_token = "dG9ieXdpbGtpbnMxQGdtYWlsLmNvbTo0ZTc5OGNkY2U3ZjdjN2Q0ZTY2ZWVlZjdmMGQxNzI4YTNlZjc4YThk"
    postcode = "SW14 8LE"
    building_name = None
    address = None

    epc_report = get_epc_report(auth_token, postcode, building_name, address)

    if epc_report:
        print(json.dumps(epc_report, indent=2))

