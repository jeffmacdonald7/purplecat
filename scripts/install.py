#!/usr/bin/python
import os, sys
import subprocess

version="00002"
proc_name="purplecat install.py"
config_file="/etc/purplecat/purplecat.conf"
config_path="/etc/purplecat/"
new_install_defaults="#  this file create by " + proc_name 
new_install_defaults+="version " + version + "\n\n"
uuid=""



def check_for_config_file():
    # Read the list of needed files pwdfrom the file
  
  if not os.path.isfile(config_file):
     create_new_config_file()
  

def create_new_config_file():
   new_install_defaults=generate_new_uuid()
   if not os.path.exists(config_path):
     try:
       os.mkdir(config_path)
     except OSError as error:
        print ("Error: cant create " + config_path)
        sys.exit(1)
   if not os.path.exists(config_file):
     with open(config_file, 'x') as cf:
      # Write the variables to the 
      print ("writing config file new ")
      cf.write(new_install_defaults)
 
def check_root_user():
    if os.geteuid() != 0:
        print("Error: This script must be run as root. Exiting...")
        sys.exit(1)

def check_sysstat_present():
   if not os.path.exists("/var/log/sysstat"):
     try:
      subprocess.run(["apt-get", "install", "sysstat"], check=True)
      print("sysstat installed successfully.")
     except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def check_nginx_present():
   if not os.path.exists("/etc/nginx/nginx.conf"):
     try:
      subprocess.run(["apt-get", "install", "nginx"], check=True)
      print("sysstat installed successfully.")
     except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def generate_new_uuid():
  # Run the uuidgen command and capture its output
   print ("generate_new_uuid called ")
   uuid_proc = subprocess.run(['uuidgen'], capture_output=True, text=True)
   uuid=uuid_proc.stdout.strip()
   return new_install_defaults + "machineid="+ uuid + "\n"



if __name__ == "__main__":
    check_root_user()
    check_for_config_file()
    check_sysstat_present()
    


