# Import the project class
from project.main import Project
# Import the response class
from project.response import Response

# Create a new object of the project
Project = Project()

# Run the project method to get the project name 
#Project.get_project_name()

# Run the project method to get the project containers
Project.get_list_of_containers()

# Set the project root directory
Project.set_project_root()

# Creates the base directories and files
Project.create_base_files()

# TODO :: Create all container files and configurations
Project.create_containers_from_container_list()

# TODO :: Add network block to docker-compose file
Project.add_network_block_to_compose_file()

# Finally initialise the git repo
Project.init_git_repo()

# TODO :: Remove the files and directories related to docker-environment-creator
# e.g. import shutil
#      shutil.rmtree(os.getcwd() + 'docker-environment-creator')