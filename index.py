# Import the project class
from classes.project import Project

# Create a new object of the project
Project = Project()
# Checks with he user all info given is correct
Project.check_with_user()
# Creates the base directories and files
Project.create_base_files()
# Creates all container files and configurations
exit()
Project.configure_containers()
# Finall initialise the git repo
Project.init_git_repo