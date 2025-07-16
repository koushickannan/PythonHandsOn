import os


def path_os():
    abs_file_path = os.path.join(os.path.dirname(__file__))
    print(abs_file_path)
    abs_file_path_1 = os.path.join(os.path.dirname(abs_file_path))
    print(abs_file_path_1)


def my_family(age):
    family = {
        'Dad': range(30, 60),
        'Mom': range(50),
        'Child': range(0, 5)
    }

    for member, age_range in family.items():
        if age in age_range:
            return member

    return "unknown"


if __name__ == "__main__":
    print(my_family(35))
    # path_os()
