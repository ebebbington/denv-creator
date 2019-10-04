import os
from project.validate import Validate
from project.response import Response

#
# Responsible for holding information regarding the whole project
#
class Project:

    # Initialise the project object with all information relating to it
    def __init__(self):
        # Get project name and check if empty
        self.name = Response.ask_for_input('Project directory name: ')
        Validate.val_is_set(self.name)
        Validate.is_valid_dir_name(self.name)
        # Get project directory to reside in and check if set
        self.dir = Response.ask_for_input("Project path where '{}' will reside: ".format(self.name))
        Validate.val_is_set(self.dir)
        # Append a / to project path if needed
        if self.dir.find('/', len(self.dir) - 1) < 0:
            self.dir = self.dir + '/'
        # Set the root directory and check it doesnt exist as well as being valid
        self.root = self.dir + self.name
        Validate.dir_exists(self.root)
        Validate.is_valid_dir_name(self.root)
        # Get the list of containers to build and check nly one web server is defined
        self.containers = Response.ask_for_input("Containers to Build: ").split()
        Validate.val_is_set(self.containers)
        Validate.check_is_array(self.containers)
        Validate.contains_only_one_web_server(self.containers)
        # Set the path source code will sit in the containers
        self.container_project_path = "/var/www/{}".format(self.name)
        self.container_name_prefix = self.name

    # Check project info with the user
    def check_with_user(self):
        project_info = [
            'Project name: {}'.format(self.name),
            'Project path: {}'.format(self.root),
            'List of containers to build: {}'.format(self.containers)
        ]
        # Loop through the info displaying it
        for item in project_info:
            Response.show_info(item)
        # Check the displayed info is ok with the user
        all_is_ok = Response.ask_for_input('Is this ok? [y/n]: ')
        if all_is_ok == 'n':
            Response.show_error('Some facts were gathered incorrectly')

    # Create the base folders and files and not any dockerfiles or configs
    def create_base_files(self):
        Response.show_info('Creating the foundation of the directory...')
        try:
            os.mkdir(self.root)
            open('{}/README.md'.format(self.root), 'x')
            open('{}/.gitignore'.format(self.root), 'x')
            open('{}/docker-compose.yml'.format(self.root), 'x')
            os.mkdir('{}/src'.format(self.root))
            os.mkdir('{}/.docker'.format(self.root))
        except OSError as err:
            Response.show_error('Unable to create files: {}. Please check the directory and/or remove files'.format(err))
    
    # Write data to a file
    def write_to_file(file, content):
        f = open(file, 'w')
        f.write(content)
        f.close()

    
