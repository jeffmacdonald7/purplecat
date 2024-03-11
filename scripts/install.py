#!/usr/bin/python
import os

needed_files=""

def check_files():
    # Read the list of needed files from the file
  try:    
    with open("needed_files.txt", "r") as file:
        #debug
        print("checking for " + file )
        needed_files = [line.strip() for line in file.readlines()]

  except FileNotFoundError:
        print("Error: The 'needed_files.txt' file is missing.")
        return

    # Check if the needed files exist
missing_files = []
for file in needed_files:
        if not os.path.isfile(file):
            missing_files.append(file)

    # Prompt the user to install missing files
if missing_files:
        print("The following files are missing:")
        for file in missing_files:
            print(file)
        answer = input(file + " missing please install first as purplecat needs it ")

        if answer.lower() == "y":
            # Install the missing files using a package manager or your preferred method
            # ...
            pass
        else:
            print("Please install the missing files manually.")
else:
        print("All needed files are present.")

if __name__ == "__main__":
    check_files()

