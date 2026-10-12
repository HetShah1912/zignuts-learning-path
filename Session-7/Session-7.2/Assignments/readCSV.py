# Create a program to read a CSV file and print its content.

import csv

with open('library_books.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      print(row["book_id"], "|", row["title"], "|", row["author"], "|", row["genre"], "|",row["publication_year"])   