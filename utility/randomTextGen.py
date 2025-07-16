import csv
import random


def generate_random_text(prefix, num_records):
    text_list = []
    for i in range(num_records):
        text_list.append(f"{prefix}{random.randint(1, num_records)}")
    return text_list


def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow([row])


def main():
    total_records = 150000
    unique_records_interval = 5000
    num_unique_texts = total_records // unique_records_interval
    remaining_records = total_records % unique_records_interval

    data = []

    for i in range(num_unique_texts):
        prefix = f"demo{i + 1}"
        unique_text_list = generate_random_text(prefix, unique_records_interval)
        data.extend(unique_text_list)

    # Add remaining records
    prefix = f"demo{num_unique_texts + 1}"
    remaining_text_list = generate_random_text(prefix, remaining_records)
    data.extend(remaining_text_list)

    write_to_csv("../learnings/random_text.csv", data)


if __name__ == "__main__":
    main()
