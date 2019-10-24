import os
import re
from project.response import Response

class Validate:

    def dir_exists(dir):
        if os.path.exists(dir):
            Response.show_error('The {} directory already exists'.format(dir))

    def is_valid_dir_name(dir):
        match = re.match("^[\w\-./]+$", dir)
        if not match:
            Response.show_error('{} is not a valid directory'.format(dir))