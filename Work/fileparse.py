# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_header=True, delimiter=None):
    """
    Parse a CSV file into a list of records
    """
    with open(filename) as f:
        if delimiter:
            # Separate values in each row by indicated delimiter
            rows = csv.reader(f, delimiter=delimiter)
        else:
            rows = csv.reader(f)

        if has_header:
            # Read the file headers
            headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            if has_header:
                headers = select
                indices = [headers.index(colname) for colname in select]
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]

            if has_header:
                # Make a dictionary
                record = dict(zip(headers, row))
                records.append(record)
            else:
                # Make a tuple
                record = tuple(row)
                records.append(record)

    return records


print(parse_csv('Data/portfolio.csv'))
