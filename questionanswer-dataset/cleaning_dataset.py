import csv

with open('dataset.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    # print(csv_reader)
    for row in csv_reader:
        if (row[2] == 'yes' or row[2] == 'Yes' or row[2] == 'no' or row[2] == 'No' and len(row) == 6):
            if(row[3] == 'easy' or row[3] == 'medium' or row[3] == 'hard'):
                if(row[4] == 'easy' or row[4] == 'medium' or row[4] == 'hard'):
                    print(row[0]+","+row[1]+","+row[2].lower()+","+row[3].lower()+","+row[4].lower())
    
    # for row in csv_reader:
    #     if line_count == 0:
    #         print(f'Column names are {", ".join(row)}')
    #         line_count += 1
    #     print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
    #     line_count += 1
    # print(f'Processed {line_count} lines.')