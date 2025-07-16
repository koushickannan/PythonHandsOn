import csv, random, sys, datetime
import string

from faker import Faker

fake = Faker()
number_of_records = int(sys.argv[1])


def random_date(start_year, end_year, separator):
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)

    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)

    if separator == '-':
        date_formatted = "{:02d}-{:02d}-{:04d}".format(month, day, year)
    elif separator == '/':
        date_formatted = "{:02d}/{:02d}/{:04d}".format(month, day, year)
    else:
        date_formatted = ''
        print('Allowed Separator - or /')

    return date_formatted


def generate_random_string(length):
    characters = string.ascii_letters
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


with open('DI_' + str(number_of_records) + 'Records_' + datetime.datetime.now().strftime('%Y_%m_%d_%H-%M-%S') + '.csv',
          mode='w', newline='', encoding='utf-8') as file:
    file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    file_writer.writerow(['UserId', 'FirstName', 'MiddleName', 'LastName', 'Email',
                          'JobCode', 'JobName', 'HireDate', 'Status', 'DateOfBirth',
                          'Gender', 'YearsofExperiences', 'ActiveDate', 'InactiveDate'])

    for _ in range(number_of_records):
        emailVal = generate_random_string(5) + '@rqimail.laerdalblr.in'
        file_writer.writerow(
            [emailVal, generate_random_string(5), 'API', generate_random_string(5), emailVal,
             '', generate_random_string(5), '', 'Active', '',
             random.choice(['Male', 'Female']), fake.random_int(min=2, max=20), '', ''])