#!/usr/bin/python
import os, sys
import subprocess

version="00001"
proc_name="purplecat install.py"
config_file="/etc/purplecat/purplecat.conf"
config_path="/etc/purplecat/"
new_install_defaults="#  this file create by " + proc_name 
new_install_defaults+="version " + version + "\n\n"
uuid=""



def check_for_config_file():
    # Read the list of needed files pwdfrom the file
  try:    
    with open(config_file, "r") as file:
      for line in file.readlines():
        print("")
        # WORK on reading in previous config
  except FileNotFoundError:
        print("Info: no " + config_file + " assuming new install ")
        create_new_config_file()
  except PermissionError:
        print ("Error: cant open " + config_file + " for reading ")

def create_new_config_file():

  
   if not os.path.exists(config_path):
     try:
       os.mkdir(config_path)
     except OSError as error:
        print ("Error: cant create " + config_path)
        sys.exit(1)
   if not os.path.exists(config_file):
     with open(config_file, 'w') as cf:
      # Write the variables to the 
      print ("writing config file new ")
      cf.write(new_install_defaults)
 
def check_root_user():
    if os.geteuid() != 0:
        print("Error: This script must be run as root. Exiting...")
        sys.exit(1)

def generate_new_uuid():
  # Run the uuidgen command and capture its output
   uuid_proc = subprocess.run(['uuidgen'], capture_output=True, text=True)
   uuid=uuid_proc.stdout.strip()



if __name__ == "__main__":
    check_root_user()
    check_for_config_file()
    


