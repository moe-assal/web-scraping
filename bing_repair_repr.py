import os


def rename_numerically(path_to_file, extension):
    images = os.listdir(path_to_file)
    for i, image in enumerate(images):
        old_directory = os.path.join(path_to_file, image)
        new_directory = os.path.join(path_to_file, i.__str__() + extension)
        os.rename(old_directory, new_directory)


def repair(path_to_file, extension, last_name):
    error = 0
    for i in range(last_name + 1):
        try:
            old_directory = os.path.join(path_to_file, str(i) + extension)
            new_directory = os.path.join(path_to_file, str(i - error) + extension)
            os.rename(old_directory, new_directory)
        except FileNotFoundError:
            error += 1
