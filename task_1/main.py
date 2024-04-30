"""This module copies the content of the pictures folder"""

from pathlib import Path
import shutil


def parse_input(user_input):
    """This function parses user input"""
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args


def copy_files(source_dir: Path, destination_dir: str) -> None:
    """This function creates a new folder and copies the contens of the pictures folder"""
    source_dir = Path(source_dir)
    destination_dir = Path(destination_dir)

    if source_dir.is_dir():
        for child in source_dir.iterdir():
            if child.is_file():
                extension = child.suffix[1:]
                destination_subdir = destination_dir / extension
                destination_subdir.mkdir(parents=True, exist_ok=True)
                destination_file = destination_subdir / child.name
                print("destination_file ", destination_file)

                try:
                    shutil.copyfile(child, destination_file)
                except Exception as e:
                    print(f"Error copying file {child}: {e}")

            else:
                copy_files(child, destination_dir)


def main():
    """This function prompts user to enter a path to folder and a destination folder"""

    while True:
        user_input = input("Enter a path to folder to copy and a destination folder: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            folder = command
            destination = args[0] if len(args) > 0 else "dist"
            try:
                copy_files(folder, destination)
                print("Files copied successfully.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                break


if __name__ == "__main__":

    main()
