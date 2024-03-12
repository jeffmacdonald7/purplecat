#!/usr/bin/python
import os

config_file="/etc/purplecat/purplecat.conf"

def check_files():
    # Read the list of needed files pwdfrom the file
  try:    
    with open(config_file, "r") as file:
      for line in file.readlines():
        print(line)
  except FileNotFoundError:
        print("Error: " + config_file + " not found "  )
        return
  except PermissionError:
        print ("cant open " + config_file + " for reading ")

if __name__ == "__main__":
    check_files()

