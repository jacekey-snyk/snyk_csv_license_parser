import csv 
import os
import sys 

file_name = input("Please enter the file with extension name: ")

try:
    csv.field_size_limit(sys.maxsize)
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),file_name),"r", newline='' , encoding='UTF8') as I:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'License_output.csv'),"w", newline='' , encoding='UTF8') as O:
            reader = csv.DictReader(I)
            readerdict=list(reader)
            print(f"{len(readerdict)} rows found in the csv file.")
            header=readerdict[0].keys()
            writer = csv.DictWriter(O,fieldnames=header)
            writer.writeheader()
            for row in readerdict:
                Projects=row["projects"].split(",")
                for project in Projects:
                    row["projects"]=project.strip()
                    writer.writerow(row)

except Exception as E:
    # print(E)
    print("Please Try Again.. If the error presists, contact the developer..")
else:
    print("Done!")