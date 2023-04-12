import csv

domains = []

with open('websites/nl.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        domain = row[1]
        if domain.endswith('.nl'):
            domains.append('https://www.' + domain)

# Write the domains list to a text file
with open('websites/nl.txt', 'w') as txt_file:
    for i in range(500):
        txt_file.write(domains[i] + '\n')