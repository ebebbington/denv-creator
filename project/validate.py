import os
import re
from project.response import Response

class Validate:

    def dir_exists(dir):
        if os.path.exists(dir):
            Response.show_error('The {} directory already exists'.format(dir))

    def check_is_array(vals):
        if not isinstance(vals, list):
            Response.show_error('The given containers is not a list')

    def contains_only_one_web_server(container_list):
        possible_web_servers = [
            'nginx',
            'apache'
        ]
        count = 0
        for container in container_list:
            for possible_web_server in possible_web_servers:
                # Create the count
                if possible_web_server == container:
                    count = count + 1
                # Check if more thn 2 servers are defined
                if count > 1:
                    Response.show_error('You have defined more than one web server')

    def is_valid_dir_name(dir):
        match = re.match("^[\w\-./]+$", dir)
        if not match:
            Response.show_error('{} is not a valid directory'.format(dir))

    def val_is_set(val):
        if len(val) < 1:
            Response.show_error('You did not specify a value')
