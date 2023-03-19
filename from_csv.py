# add the records in csv file to the database at dna_str table

import csv
from cs50 import SQL
from helpers import hash_str


# open the database
db = SQL("sqlite:///dna_str_db.db")

# open the csv file
with open("large.csv", "r") as file:
    reader = csv.DictReader(file)

    # iterate over the csv file
    for row in reader:
        # get the STR counts
        STRs = ["AGATC", "TTTTTTCT", "AATG", "TCTAG", "GATA", "TATC", "GAAA", "TCTG"]
        count = []
        for STR in STRs:
            count.append(int(row[STR]))

        # print the STR counts
        print(count)
        # print name
        print(row["name"])

        # add the new DNA STR to the database
        try:
            db.execute("INSERT INTO dna_str (owner_name, hashed, AGATC, TTTTTTCT, AATG, TCTAG, GATA, TATC, GAAA, TCTG) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                       row["name"], hash_str(count), count[0], count[1], count[2], count[3], count[4], count[5], count[6], count[7])
        except:
            print("Error")




