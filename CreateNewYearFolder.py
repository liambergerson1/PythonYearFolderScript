# Python modules that will be used
import os
import datetime

# Declare the directories that will be used within the root directory
directories = ["Entries", "TM Results", "Backups", "PDF Results"]
# Declare the root directory
source_directory = "C:\\Users\\Liam Bergerson\\OneDrive\\Desktop\\Swim and Dive"
# Check the current year and convert it to a string
current_year = datetime.datetime.now().year
directory_name = str(current_year)

# Function to create directories based on the year
def create_year_directory():
    # Change directory to the root directory
    os.chdir(source_directory)
    # Use the current year as the variable in the function
    directory_name = str(current_year)
    # A loop that creates the year directories based on the directories list declared earlier
    for directory in directories:
        # A conditional statement that if the directory exists, that directory will be the new working directory
        if os.path.exists(directory):
            os.chdir(directory)
            # A conditional statement that if a directory for a year does not exist, a new year directory will be created
            if not os.path.exists(directory_name):
                # Year directory is created
                os.mkdir(directory_name)
                # Newly created directory is the new working directory
                os.chdir(directory_name)
                # Two directories are created, one for both genders
                os.mkdir("Boys")
                os.mkdir("Girls")
                # A print statement that confirms that the directories have been created
                print("Year ", directory_name,  "has been created")
                # Changing directories to the root directory to continue the loop
                os.chdir(source_directory)
            else:
                # If the year directory already exists, a print statement will be printed and the directory will not be created
                print("Year ", directory_name,  "already exists")
# Executing the function
create_year_directory()


