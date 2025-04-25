from os import makedirs


def create_path(path):
    try:
        makedirs(path)
        print(f"{path} created.")
    except FileExistsError:
        print(f"{path} exists.")