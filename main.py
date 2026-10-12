with open('spots.csv', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

import csv

with open('spots.csv', mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        print(f"{row['name']} is {row['noise']}.")
