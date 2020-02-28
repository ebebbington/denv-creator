# Import the project class
from project import Project

# Create a new object of the project
Project = Project()

# Set the directory of where to put the new project
Project.set_path()

# Run the project method to get the project containers
Project.get_list_of_containers()

# from pprint import pprint
# pprint(vars(Project))

# Prefix the container names with something
#Project.get_prefix_for_containers()

# Creates the base directories and files
Project.create_base_files()

# Add the starting block to the docker-compose.yml file
Project.init_docker_compose_file()

# Create all container files and configurations
Project.create_containers_from_container_list()

# Add network block to docker-compose.yml file
Project.add_network_block_to_compose_file()

# Finally initialise the git repo
Project.init_git_repo()

# Remove this directory
#Project.clean_up()

# NOTES

# mounted directory is called src
# nginx port is 3001
# phpfpm port is 3002
# NEW NAME docker builder?