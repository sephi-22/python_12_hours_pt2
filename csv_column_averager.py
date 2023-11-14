#Write a function that reads a CSV file and calculates the average of the numbers in a given column.
import csv
def average_of_column(csv_filename, column_index):
    with open(csv_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader, None)  # Skip header row
        if header is None:
            print("Error: Empty CSV file.")
            return 0

        total, count = 0, 0
        for row in reader:
            if column_index < len(row):
                total += float(row[column_index])
                count += 1

        return total / count if count else 0

average_result = average_of_column('examplecsv.csv', 1)
print(average_result)

