import os
from project.validate import Validate
from project.response import Response

#
# Responsible for holding information regarding the whole project
#
class Project:

    # Initialise the project object with all information relating to it
    def __init__(self):
        # Set the project directory to be the parent folder
        self.dir = '../'

    # Gets the input, validates it and checks with the user
    def get_project_name(self):
        self.name = Response.ask_for_input('Project directory name: ')
        # then validate it
        Validate.is_valid_dir_name(self.name)
        # then check with the user
        project_name_is_ok = Response.ask_for_input('Project name: {}. Is this ok? [y/n]: '.format(self.name)).lower()
        if project_name_is_ok != 'y':
            Response.show_error('Exiting...')

    # get the input, and check with the user
    def get_list_of_containers(self):
        self.containers = Response.ask_for_input("Containers to Build: ").split()
        # then lower case each item
        self.containers = [x.lower() for x in self.containers]
        # check with the user
        project_containers_are_ok = Response.ask_for_input('Containers: {}. Is this ok? [y/n]: '.format(self.containers)).lower()
        if project_containers_are_ok != 'y':
            Response.show_error('Exiting...')

    # Define the project root to be the projects full directory
    def set_project_root(self):
        self.root = os.getcwd()

    # Create the directory of the project root
    def create_project_dir(self):
        Response.show_log('Creating {}'.format(self.root))
        os.mkdir(self.root)

    # Add the generic network block to the docker-compose file to allow networking between the containers
    def add_network_block_to_compose_file(self):
        # TODO
        Response.show_error('add_network_block_to_compose_file NOT IMPLEMENTED')

    # Initialise a git repository
    def init_git_repo(self):
        # TODO
        Response.show_error('init_git_repo NOT IMPLEMENTED')

    # Create the containers
    def create_containers_from_container_list(self):
        # TODO
        Response.show_error('create_containers_from_container_list NOT IMPLEMENTED')
    
    # Create the base folders and files and not any dockerfiles or configs
    def create_base_files(self):
        try:
            Response.show_log('Creating {}/LICENSE.txt'.format(self.root))
            open('{}/LICENSE.txt'.format(self.root), 'x')
            Response.show_log('Creating {}/.gitignore'.format(self.root))
            open('{}/.gitignore'.format(self.root), 'x')
            Response.show_log('Creating {}/docker-compose.yml'.format(self.root))
            open('{}/docker-compose.yml'.format(self.root), 'x')
            Response.show_log('Creating {}/src'.format(self.root))
            os.mkdir('{}/src'.format(self.root))
            Response.show_log('Creating {}/.docker'.format(self.root))
            os.mkdir('{}/.docker'.format(self.root))
            Response.show_log('Creating {}/.docker/config'.format(self.root))
            os.mkdir('{}/.docker/config'.format(self.root))
            Response.show_log('Creating {}/.docker/data'.format(self.root))
            os.mkdir('{}/.docker/data'.format(self.root))
            Response.show_log('Creating {}/.docker/env'.format(self.root))
            os.mkdir('{}/.docker/env'.format(self.root))
        except OSError as err:
            Response.show_error('Unable to create files: {}. Please check the directory and/or remove files. Are you specifying Unix or Windows paths for your respective OS?'.format(err))