### Code for the Duckweed Imaging system - a GUI to capture and name image files with Raspberry Pi Camera Module 3 and the Raspberry Pi 4b

### To make use of the updating function, need to install git on the Raspberry Pi first and clone the repository from atgoke.github.com
# Run this in the Raspberry Pi terminal when the Pi is first setup:
# sudo apt-get update
# sudo apt-get install git
# git clone https://github.com/atgoke/DuckweedImager.git


### Import libraries and functions
import os
import subprocess
from libcamera import controls
from picamera2 import Picamera2


### First make sure that this code is up-to-date version from Github
# Define file paths
repo_path = "/path/to/your/local/repo"
file_path = "/path/to/your/local/file.txt"

# Check for changes
def is_up_to_date(repo_path):
    try:
        # Navigate to the repository path
        os.chdir(repo_path)
        
        # Fetch the latest updates from the remote repository
        subprocess.run(['git', 'fetch'], capture_output=True, text=True)
        
        # Check the status of the local repository
        result = subprocess.run(['git', 'status', '-uno'], capture_output=True, text=True)
        
        if "Your branch is up to date" in result.stdout:
            print("The local repository is up-to-date.")
            return True
        else:
            print("The local repository is not up-to-date.")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Pull changes
def pull_latest_changes(repo_path):
    try:
        # Navigate to the repository path
        os.chdir(repo_path)
        
        # Pull the latest changes from the remote repository
        result = subprocess.run(['git', 'pull'], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Successfully pulled the latest changes!")
            return result.stdout
        else:
            print(f"An error occurred while pulling changes: {result.stderr}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Save changes
def update_local_file(file_path, content):
    try:
        # Write the pulled content to the local file
        with open(file_path, 'w') as file:
            file.write(content)
        print("Local file updated successfully!")
    except Exception as e:
        print(f"An error occurred while updating the file: {e}")

# Execute check, pull, save
if is_up_to_date(repo_path):
    print("Proceeding with the script as the repository is up-to-date.")
else:
    print("Updating the repository with the latest changes.")
    pulled_content = pull_latest_changes(repo_path)
    if pulled_content:
        update_local_file(file_path, pulled_content)

### Duckweed Imager GUI