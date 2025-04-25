from os import makedirs


def create_path(path):
    parts = path.split('/')
    path = '/'.join(parts[:-1])
    try:
        makedirs(path)
        print(f"{path} created.")
    except FileExistsError:
        print(f"{path} exists.")