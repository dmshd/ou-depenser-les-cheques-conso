

import csv
import json
import os

print("Listing JSON files in the current directory...")
count = 0

for f in os.listdir(os.curdir):
    if os.path.isfile(f) and f.endswith('.json'):
        count += 1
        print("JSON file found :", f)
        with open(f) as json_file:
            data = json.load(json_file)
            pos = f.find('.') 
            csv_file_name = f[:pos] + ".csv"
            csv_file = open(csv_file_name, "w")
            csv_writer = csv.writer(csv_file)

            row_count = 0
            #  c for company
            for c in data:
                if count == 0:
                    #  writing headers of csv file
                    header = c.keys()
                    csv_writer.writerow(header)
                    count += 1
    
            #  writing data of csv file
            csv_writer.writerow(c.values())
            csv_file.close()
            print(f, "has been converted to", csv_file_name)

        print(count, "JSON file(s) found.")

#  pre-tests 
"""
with open('affiliates.json') as json_f:
    j = json.load(json_f)


pretty_json = json.dumps(json_obj, indent=2)
print(pretty_json)
"id": "278952",
    "name": "EXKI",
    "ref": "BECO2799",
    "address": "Avenue V\u00e9sale 1",
    "zip_code": "1300",
    "city": "Wavre",
    "state": "",
    "country": "BE",
    "tel": "",
    "website": "",
    "email": "",
    "soon_available": "0",
    "latitude": "50.7318535",
    "longitude": "4.5862284",
    "type": "Ch\u00e8que consommation",
    "categories": "Restaurant"


#  affiliates json to csv
affiliates_csv_file = open('affiliates.csv', 'w')
csv_writer = csv.writer(affiliates_csv_file)
count = 0
#  c for company
for c in j:
   
    print("ID :", c["id"])
    print("Name :", c["name"])
   "
    if count == 0:
        header = c.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(c.values())

affiliates_csv_file.close()
"""
