"""This module copies the content of the pictures folder"""

from pathlib import Path
import shutil
import argparse


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

    parser = argparse.ArgumentParser(
        description="Copy files recursively and sort them by extension."
    )
    parser.add_argument("source_dir", type=str, help="Path to the source directory")
    parser.add_argument(
        "destination_dir",
        nargs="?",
        type=str,
        default="dist",
        help='Path to the destination directory (default is "dist")',
    )
    args = parser.parse_args()

    try:
        copy_files(args.source_dir, args.destination_dir)
        print("Files copied successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":

    main()
