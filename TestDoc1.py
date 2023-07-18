#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 22:27:25 2023

@author: toby
"""

from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
from docx import Document
from EPCmodule import get_epc_report

# Set the path to the Word document template
template = "SurveyTemplateMerger.docx"

# Create a MailMerge object with the template
document = MailMerge(template)
print(document.get_merge_fields())

# Perform mail merge
document.merge(Username='Toby')

# Write the merged document to a file
document.write('test-output.docx')

# Set the necessary variables for retrieving the EPC report
auth_token = "dG9ieXdpbGtpbnMxQGdtYWlsLmNvbTo0ZTc5OGNkY2U3ZjdjN2Q0ZTY2ZWVlZjdmMGQxNzI4YTNlZjc4YThk"
postcode = "SW14 8LE"
building_name = None
address = "219"

# Retrieve the EPC report using the EPCmodule
epc_report = get_epc_report(auth_token, postcode, building_name, address)

# Create a new document to store the EPC report table
report_document = Document()

# Create a table in the new document
table = report_document.add_table(rows=1, cols=2)
table.style = 'Table Grid'

# Add a header row to the table
header_row = table.rows[0]
header_row.cells[0].text = 'Address'
header_row.cells[1].text = 'EPC Score'

# Add data to the table from the EPC report
for property_data in epc_report:
    address = property_data['address']
    epc_score = property_data['current-energy-rating']
    row = table.add_row().cells
    row[0].text = address
    row[1].text = epc_score

# Save the report document with the EPC table
report_document.save('epc-report.docx')
