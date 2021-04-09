import csv
with open('sample.csv','r')as csv_file:
    read_content=csv.DictReader(csv_file)
    for line in read_content:
        print(line)
