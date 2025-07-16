import csv
import argparse
from collections import defaultdict


def read_csv_and_find_duplicates(csv_filename):
    email_count = defaultdict(int)
    empty_email_lines = []
    duplicate_emails = []
    line_number = 1

    with open(csv_filename, mode='r') as file:
        reader = csv.DictReader(file)

        # Normalize headers to lowercase
        headers = {header.lower(): header for header in reader.fieldnames}

        # Determine the email header key
        email_header = headers.get('emailid', headers.get('email'))

        if not email_header:
            print("No valid email header found in the CSV file.")
            return

        for row in reader:
            email = row[email_header].strip()
            if not email:
                empty_email_lines.append(line_number)
            email_count[email] += 1
            line_number += 1

    duplicates = {email: count for email, count in email_count.items() if count > 1}

    if duplicates:
        print("Duplicate email addresses and their counts:")
        for email, count in duplicates.items():
            duplicate_emails.append(email)
            print(f"{email}: {count} times")
    else:
        print("No duplicate email addresses found.")

    print(f"Total duplicate email addresses: {len(duplicates)}")

    if empty_email_lines:
        print("Rows with empty email addresses:")
        for line in empty_email_lines:
            print(f"Line {line}")
    else:
        print("No rows with empty email addresses found.")
    print(f"Total rows with empty email addresses: {len(empty_email_lines)}")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Identify duplicate and empty email addresses in a CSV file.")
    parser.add_argument('csv_filename', type=str, help='Path to the CSV file')
    return parser.parse_args()


def main():
    args = parse_arguments()
    read_csv_and_find_duplicates(args.csv_filename)


if __name__ == "__main__":
    main()
