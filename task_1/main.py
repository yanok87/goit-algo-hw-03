"""This module copies the content of the pictures folder"""

from pathlib import Path
import shutil
import os


def copy_files(source_dir: Path, destination_dir: str = "dist") -> None:
    """This function creates a new folder and copies the contens of the pictures folder"""

    source_dir = os.path.abspath(source_dir)
    destination_dir = os.path.abspath(destination_dir)

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1][1:]
            destination_subdir = os.path.join(destination_dir, extension)

            if not os.path.exists(destination_subdir):
                os.makedirs(destination_subdir)

            destination_file = os.path.join(destination_subdir, file)

            try:
                shutil.copyfile(source_path, destination_file)
            except Exception as e:
                print(f"Error copying file {source_path}: {e}")


if __name__ == "__main__":

    folder = Path("/Users/ianamatrosova/dev/GoIT/algos/goit-algo-hw-03/task_1/pictures")
    try:
        copy_files(folder)
        print("Files copied successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
