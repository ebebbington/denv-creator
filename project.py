import os
from validate import Validate
from response import Response

class Project:
    """
    A class used to represent the Project

    ...

    Attributes
    ----------

    Methods
    -------
    set_path()
        Defines and sets the root path of the project

    get_list_of_containers()
        Uses the Response class to get an input list for the containers

    get_prefix_for_containers()
        Gets input from the user to save a prefix that would be added to each container name

    add_network_block_to_compose_file()
        Adds the network section to the docker-compose.yml file so all containers are linked

    init_git_repo()
        Run a command to initialise a git repository in the project root

    create_containers_from_container_list()
        Logic for implementing each container the user specified

    init_docker_compose_file()
        Creates the docker-compose.yml file adding "services:" to start off the file before containers are added

    create_base_files()
        Creates th generic base files and directories such as src, .docker etc
    """

    def set_path(self):
        """
        Saves the directory the user was in when they ran the main script to be used as the project root

        e.g. The path in the bash prompt
        """
        name = Response.ask_for_input("Project name (lowercase, hyphen-seperated): ")
        self.name = name
        self.path = os.getcwd() + '/' + name

    def get_list_of_containers(self):
        """
        Get a list of containers from the user using the input() method

        Converts the input to lowercase and to an array.
        """
        self.containers = Response.ask_for_input("Containers to Build: ").split()
        # then lower case each item
        self.containers = [x.lower() for x in self.containers]
        # check with the user
        Response.show_info('Containers: {}'.format(self.containers))
        project_containers_are_ok = Response.ask_for_input('Is this ok? [y/n]: ').lower()
        if project_containers_are_ok != 'y':
            Response.show_error('Exiting...')

    def get_prefix_for_containers(self):
        """
        Ask the user for a prefix to add to every container name (One to Many)
        """
        # TODO :: Issue #13 - use the Response class to get input from the user, then assign that to "Project.container_prefix"
        Response.show_error('get_prefix_for_containers NOT IMPLEMENTED')

    def add_network_block_to_compose_file(self):
        """
        Add the network block to the docker-compose.yml file to link all containers
        """
        text_block = [
            'network:',
            '  {}-network:'.format(self.container_prefix),
            '    driver: bridge'
        ]
        # TODO :: Issue #9 - write this text to the docker-compose.yml file. make sure to append it and use the 'self.path' for the directory
        Response.show_error('add_network_block_to_compose_file NOT IMPLEMENTED')

    def init_git_repo(self):
        """
        Initialises a new git repository
        """

        # TODO :: Issue #10 - run the following command on the terminal for the user: git init
        # see for help: https://stackoverflow.com/questions/13744473/command-line-execution-in-different-folder
        Response.show_error('init_git_repo NOT IMPLEMENTED')

    def create_containers_from_container_list(self):
        """
        Logic for creating each container fies based on the containers asked for
        """

        # TODO :: (Edward) Using a 'switch' statement, make a case for every container we have and build those if it matches
        Response.show_error('create_containers_from_container_list NOT IMPLEMENTED')

    def init_docker_compose_file(self):
        """
        Add the first part of the dockerfile before any containers are added
        """
        text = [
            'version: "3"',
            '  services:'
        ]
        # TODO :: Issue #15 write this text to the docker-compose.yml file. make sure to append it and use the 'self.path' for the directory
        Response.show_error('init_docker_compose_file NOT IMPLEMENTED')
    
    def clean_up():
        import shutil
        shutil.rmtree(os.getcwd() + '/docker-environment-creator')
        Response.show_info('Cleaned.')

    # Create the base folders and files and not any dockerfiles or configs
    def create_base_files(self):
        """
        Creates all the base files and directories for the project
        """

        try:
            Response.show_log('Creating {}'.format(self.path))
            os.mkdir('{}'.format(self.path))
            Response.show_log('Creating {}/LICENSE.txt'.format(self.path))
            open('{}/LICENSE.txt'.format(self.path), 'x')
            Response.show_log('Creating {}/.gitignore'.format(self.path))
            open('{}/.gitignore'.format(self.path), 'x')
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
            Response.show_log('Creating {}/README.md'.format(self.path))
            open('{}/README.md'.format(self.path), 'x')
        except OSError as err:
            Response.show_error('Unable to create files: {}. Please check the directory and/or remove files. Are you specifying Unix or Windows paths for your respective OS?'.format(err))