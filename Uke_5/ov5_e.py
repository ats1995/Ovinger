import csv
with open("Uke_5/sola_september_table.csv", 'r') as csv_file:
    reader = csv.reader(csv_file, dialect=csv.excel, delimiter = ';')

    for row in reader:
        print(row[3])
    
    #included_cols = [0,1,3]
    #for row in reader:
        #content = list(row[i] for i in included_cols)
        #print(content)