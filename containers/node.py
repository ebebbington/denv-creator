import config

"""
...
Usage
---------
Node = Node('prefix name e.g. myprojectname')
Node.write_to_*()

"""

class Node:
    """
    A class used to represent the Node container

    ...

    Attributes
    ----------
    prefix : str
        The prefix applied for all container names
    container_name : str
        the name to give the containr inside the dockerfile
    dockerfile_name : str
        a formatted string that defines the name of the docker file for node

    Methods
    -------
    get_dockerfile_content()
        Gets the neccessary content for the dockerfile for node

    get_docker_compose_content()
        Gets to the docker compose content for node
    """

    def __init__(self, prefix_for_containers: str):
        """
        Parameters
        ----------
        prefix : str
            The prefix applied to all container names
        container_name : str
            the name to give the containr inside the dockerfile
        dockerfile_name : str
            a formatted string that defines the name of the docker file for node
        """
        self.prefix: str = prefix_for_containers
        self.container_name: str = prefix_for_containers + '_node'
        self.dockerfile_name: str = 'node.dockerfile'

    def get_dockerfile_content(self):
        """
        Writes the neccessary content to the dockerfile for node

        """

        dockerfile_content: List[str] = [
            'FROM node:10.15.3',
            '# Update and install required packages',
            'RUN apt-get update',
            '',
            'RUN     yes | npm i pm2 -g'
        ]
        return dockerfile_content

    def get_docker_compose_content(self):
        """
        Returns the neccessary content for the docker-compose.yml file for node

        """

        docker_compose_content: List[str] = [
            "  node:",
            "    container_name: {}".format(self.container_name),
            "    build:",
            "      context: .",
            "      dockerfile: .docker/{}".format(self.dockerfile_name),
            "    volumes:",
            "      - ./src:/var/www/src",
            "    working_dir: /var/www/src",
            "    command: bash -c 'You can build and start your server here'",
            "    networks:",
            "      - {}-network".format(self.prefix)
        ]
        return docker_compose_content