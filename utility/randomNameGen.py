import csv
from faker import Faker
from datetime import datetime
import argparse


class DataGenerator:
    def __init__(self):
        self.fake = Faker()
        self.used_emails = set()

    def generate_unique_data(self, num_rows: int, start_user_id: int) -> list[tuple]:
        """Generate unique user data with random names and formatted email addresses."""
        data = []
        for i in range(num_rows):
            while True:
                first_name = self.fake.first_name()
                last_name = self.fake.last_name()
                user_id = start_user_id + i
                email_id = f"{first_name}.{user_id}@rqimail.laerdalblr.in"

                if email_id not in self.used_emails:
                    self.used_emails.add(email_id)
                    entry = (
                        user_id, first_name, " ", last_name, email_id, "Physician", "Active"
                    )
                    data.append(entry)
                    break

        return data

    def write_to_csv(self, data: list[tuple], csv_filename: str) -> None:
        """Write the generated data to a CSV file."""
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["userId", "firstname", "middlename", "lastname", "emailId", "jobtitle", "status"])
            writer.writerows(data)
        print(f"CSV file '{csv_filename}' generated successfully.")


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments for number of rows and starting user ID."""
    parser = argparse.ArgumentParser(description="Generate a CSV file with dummy user data.")
    parser.add_argument('num_rows', type=int, help='Number of rows of data to generate')
    parser.add_argument('start_user_id', type=int, help='Starting user ID')
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    current_date = datetime.now().strftime("%Y-%m-%d")
    csv_filename = f"generated_data_{current_date}.csv"

    data_generator = DataGenerator()
    generated_data = data_generator.generate_unique_data(args.num_rows, args.start_user_id)
    data_generator.write_to_csv(generated_data, csv_filename)


if __name__ == "__main__":
    main()
