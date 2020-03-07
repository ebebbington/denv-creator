import config

"""
...
Usage
---------
Python = Python('prefix name e.g. myprojectname')
Python.write_to_*()

"""

class Python:
    """
    A class used to represent the Python container

    ...

    Attributes
    ----------
    prefix : str
        The prefix applied for all container names
    container_name : str
        the name to give the containr inside the dockerfile
    dockerfile_name : str
        a formatted string that defines the name of the docker file for python

    Methods
    -------
    write_to_dockerfile()
        Writes the neccessary content to the dockerfile for python

    write_to_docker_compose_file()
        Appends to the docker compose file with the neccessary python content
    """

    def __init__(self, prefix_for_containers: str):
        """
        Parameters
        ----------
        prefix : str
            The prefix applied to all container names
        container_name : str
            the name to give the container inside the dockerfile
        dockerfile_name : str
            a formatted string that defines the name of the docker file for python
        """
        self.prefix: str = prefix_for_containers
        self.container_name: str = prefix_for_containers + '_python'
        self.dockerfile_name: str = 'python.dockerfile'

    def write_to_dockerfile(self, root_path: str):
        """
        Writes the neccessary content to the dockerfile for python

        """

        dockerfile_content: List[str] = [
            'FROM python:3',
            '# Update and install required packages',
            'RUN apt-get update -y \\',
            '    && apt install -y --no-install-recommends nodejs npm \\',
            '',
            'RUN npm install -g npm@latest \\',
            '    && yes | npm i -g pm2 \\',
            '    && pip install --upgrade pip \\',
            '    && pip install --upgrade pip \\',
            '    && pip install eventlet \\',
            '    && pip install -U python-dotenv \\',
            '    && pip install Flask \\',
            '    && pip install flask-socketio'
        ]
        file = open('{}/.docker/{}'.format(root_path, self.dockerfile_name), 'w')
        for text in dockerfile_content:
            file.write(text + '\n')

    def write_to_docker_compose_file(self, root_path: str):
        """
        Writes the neccessary content to the docker-compose.yml file for python

        """

        docker_compose_content: List[str] = [
            "  python:",
            "    container_name: {}".format(self.container_name),
            "    build:",
            "      context: .",
            "      dockerfile: .docker/{}".format(self.dockerfile_name),
            "    volumes:",
            "      - ./src:/var/www/src",
            "    working_dir: /var/www/src",
            "    command: bash -c 'You can build and start your server here e.g python main.py'",
            "    networks:",
            "      - {}-network".format(self.prefix)
        ]
        file = open('{}/docker-compose.yml'.format(root_path), 'a')
        for text in docker_compose_content:
            file.write(text + '\n')