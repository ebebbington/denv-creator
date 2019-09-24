import os

class Validate:

    def dir_exists(dir):
        if os.path.exists(dir):
            print('The {} directory already exists'.format(dir))
            exit()

    def populate_list_of_servers():
        self.servers = [
            'nginx'
        ]

    def check_is_array(vals):
        if not isinstance(vals, list):
            print('The given containers is not a list')
            exit()

    def path_exists(path):
        try:
            open(path, 'x')
            return true
        except:
            return false

    def contains_only_one_web_server(container_list):
        possible_web_servers = [
            'nginx'
        ]
        count = 0
        for i in container_list:
            # Create the count
            if possible_web_servers == container[i]:
                count = count + 1
            # Check if more thn 2 servers are defined
            if count > 1:
                print('You have defined more than one web server')
                exit()
        
    def is_set(val):
        if not val:
            return false
        return true
