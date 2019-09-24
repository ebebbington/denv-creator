import os
from classes.validate import Validate

class Project:

    def __init__(self):
        self.name = str(input('Main directory name: '))
        self.dir = str(input("Project path where '{}' will reside: ".format(self.name)))
        if self.dir.find('/', len(self.dir) - 1) < 0:
            self.dir = self.dir + '/'
        self.root = self.dir + self.name
        Validate.dir_exists(self.root)
        self.containers = input("Containers to Build: ").split()
        Validate.check_is_array(self.containers)
        Validate.contains_only_one_web_server(self.containers)
        self.container_path = "/var/www/{}".format(self.name)
        self.container_name_prefix = self.name

    def create_base_files(self):
        try:
            os.mkdir(self.root)
            open('{}/README.md'.format(self.root), 'x')
            open('{}/.gitignore'.format(self.root), 'x')
            open('{}/docker-compose.yml'.format(self.root), 'x')
            os.mkdir('{}/src'.format(self.root))
            os.mkdir('{}.docker'.format(self.root))
        except OSError as err:
            print('Unable to create files: {}. Please chekc the directory and/or remove files'.format(err))
            exit()

    def create_dir(dir):
        try:
            os.mkdir(dir)
            return true
        except:
            return false

    def create_file(file):
        open(file, 'x')
    
    def write_to_file(file, content):
        f = open(file, 'w')
        f.write(content)
        f.close()
