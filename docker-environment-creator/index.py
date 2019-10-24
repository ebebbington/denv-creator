# Import the project class
from project.main import Project

# Create a new object of the project
Project = Project()

# Set the directory of where to put the new project
Project.set_path()

# Run the project method to get the project containers
Project.get_list_of_containers()

# Prefix the container names with something
Project.get_prefix_for_containers()

# Creates the base directories and files
Project.create_base_files()

# TODO :: Add the start of the dockerfile e.g. services:
Project.init_docker_compose_file()

# TODO :: Create all container files and configurations
Project.create_containers_from_container_list()

# TODO :: Add network block to docker-compose file
Project.add_network_block_to_compose_file()

# Finally initialise the git repo
Project.init_git_repo()

# TODO :: Remove the files and directories related to docker-environment-creator
# e.g. import shutil
#      shutil.rmtree(os.getcwd() + '/docker-environment-creator')

# NOTES

# mounted directory is called src
# nginx port is 3001
# phpfpm port is 3002
# NEW NAME docker builder?