import csv
import json

#create list
sales_data = []

#open csv file 
with open("SalesJan2009.csv", "r") as infile:
    csvreader = csv.reader(infile)
    for row in csvreader: #create dictionary of each line and add to list
        sales_data.append({'Transaction_date':row[0].strip('"'),'Product':row[1].strip('"'),'Price':row[2].strip('"'),'Payment_Type':row[3].strip('"'),'Name':row[4].strip('"'), 'City':row[5].strip('"'),'State':row[6].strip('"'),'Country':row[7].strip('"')})

#open json file
with open("transaction_data.json", "w") as outfile:
    json.dump(sales_data, outfile, indent = 5) #put list of dictionaries into json file

#close files   
infile.close()
outfile.close()
