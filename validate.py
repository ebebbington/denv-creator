import os
import re
from response import Response

class Validate:
    """
    A class used to perform any type of validation

    ...

    Methods
    -------
    dir_exists(dir)
        Checks if the given directory exists

    is_valid_dir_name(dir)
        Checks the passed in directory name against some RegEx for determining a valid directory name
    """

    def dir_exists(dir):
        """
        Checks if a given directory exists on the file system

        Parameters
        ----------
        dir : str
            The directory to check
        """

        if os.path.exists(dir):
            Response.show_error('The {} directory already exists'.format(dir))

    def is_valid_dir_name(dir):
        """
        Checks a given directory name against regex to make sure its a valid directory name

        Parameters
        ----------
        dir : str
            The directory to check against
        """

        match = re.match("^[\w\-./]+$", dir)
        if not match:
            Response.show_error('{} is not a valid directory'.format(dir))