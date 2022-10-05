import csv
import re
user_file = "some_file.txt" # ask user

email_addresses = []
with open(user_file, 'r') as emails:
    for line in emails:
        line = strip(line)
        if line.find("From:"):
            email_addresses.append(re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', line))

    #reader = csv.reader(csv_file, dialect=csv.excel, delimiter = ';')

    #for row in reader:
        #row = strip(row)
        #if row.find("From:"):
            #email_addresses.append(row) # strip everything except email address