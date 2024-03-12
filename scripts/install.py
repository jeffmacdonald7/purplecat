#!/usr/bin/python
import os

config_file="/etc/purplecat/purplecat.conf"
config_path="/etc/purplecat/"

def check_for_config_file():
    # Read the list of needed files pwdfrom the file
  try:    
    with open(config_file, "r") as file:
      for line in file.readlines():
        print(line)
  except FileNotFoundError:
        print("Error: " + config_file + " not found "  )
        return
  except PermissionError:
        print ("Error: cant open " + config_file + " for reading ")

def create_new_config_file():
   print ("here ")


if __name__ == "__main__":
    check_for_config_file()

