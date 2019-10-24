import os
from project.validate import Validate
from project.response import Response

class Project:
    """
    A class used to represent the Project

    ...

    Methods
    -------
    set_path()
        Defines and sets the root path of the project

    get_list_of_containers()
        Uses the Response class to get an input list for the containers

    get_prefix_for_containers()
        Gets input from the user to save a prefix that would be added to each container name

    write_to_config_file_without_php_fpm()
        Writes the neccessary content to the config file where the php-fpm support is commented out
    """

    def set_path(self):
        self.path = os.getcwd()

    def get_list_of_containers(self):
        self.containers = Response.ask_for_input("Containers to Build: ").split()
        # then lower case each item
        self.containers = [x.lower() for x in self.containers]
        # check with the user
        Response.show_info('Containers: {}'.format(self.containers))
        project_containers_are_ok = Response.ask_for_input('Is this ok? [y/n]: ').lower()
        if project_containers_are_ok != 'y':
            # TODO run the project again
            Response.show_error('Exiting...')

    def get_prefix_for_containers(self):
        Response.show_error('get_prefix_for_containers NOT IMPLEMENTED')

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

    def init_docker_compose_file():
        # TODO
        Response.show_error('init_docker_compose_file NOT IMPLEMENTED')
    
    # Create the base folders and files and not any dockerfiles or configs
    def create_base_files(self):
        try:
            Response.show_log('Creating {}/LICENSE.txt'.format(self.path))
            open('{}/LICENSE.txt'.format(self.root), 'x')
            Response.show_log('Creating {}/.gitignore'.format(self.path))
            open('{}/.gitignore'.format(self.root), 'x')
            Response.show_log('Creating {}/docker-compose.yml'.format(self.path))
            open('{}/docker-compose.yml'.format(self.path), 'x')
            Response.show_log('Creating {}/src'.format(self.path))
            os.mkdir('{}/src'.format(self.path))
            Response.show_log('Creating {}/.docker'.format(self.path))
            os.mkdir('{}/.docker'.format(self.path))
            Response.show_log('Creating {}/.docker/config'.format(self.path))
            os.mkdir('{}/.docker/config'.format(self.path))
            Response.show_log('Creating {}/.docker/data'.format(self.path))
            os.mkdir('{}/.docker/data'.format(self.path))
            Response.show_log('Creating {}/.docker/env'.format(self.path))
            os.mkdir('{}/.docker/env'.format(self.path))
        except OSError as err:
            Response.show_error('Unable to create files: {}. Please check the directory and/or remove files. Are you specifying Unix or Windows paths for your respective OS?'.format(err))