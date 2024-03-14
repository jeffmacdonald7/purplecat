#!/usr/bin/python
import os
import subprocess

config_file="/etc/purplecat/purplecat.conf"
config_path="/etc/purplecat/"

def check_for_config_file():
    # Read the list of needed files pwdfrom the file
  try:    
    with open(config_file, "r") as file:
      for line in file.readlines():
        print(line)
  except FileNotFoundError:
        print("no  " + config_file + "assuming new install ")
        create_new_config_file()
  except PermissionError:
        print ("Error: cant open " + config_file + " for reading ")

def create_new_config_file():
  # Run the uuidgen command and capture its output
   uuid_proc = subprocess.run(['uuidgen'], capture_output=True, text=True)
   uuid=uuid_proc.stdout.strip()
   print("uuid is "+ uuid )


if __name__ == "__main__":
    check_for_config_file()


