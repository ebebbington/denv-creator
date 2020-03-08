import config

"""
...
Usage
---------
redis = redis('prefix name e.g. myprojectname')
redis.write_to_*()

"""

class Redis:
    """
    A class used to represent the redis container

    ...

    Attributes
    ----------
    prefix : str
        The prefix applied for all container names
    container_name : str
        the name to give the containr inside the dockerfile
    port : int
        port for redis to run on
    dockerfile_name : str
        a formatted string that defines the name of the docker file for redis

    Methods
    -------
    write_to_dockerfile()
        Writes the neccessary content to the dockerfile for redis

    write_to_docker_compose_file()
        Appends to the docker compose file with the neccessary redis content

    write_to_config_file()
        Writes the neccessary content to the config file with php-fpm support
    """

    def __init__(self, prefix_for_containers: str):
        """
        Parameters
        ----------
        prefix : str
            The prefix applied to all container names
        container_name : str
            the name to give the containr inside the dockerfile
        port : int
            port for redis to run on
        dockerfile_name : str
            a formatted string that defines the name of the docker file for redis
        """
        self.prefix: str = prefix_for_containers
        self.container_name: str = prefix_for_containers + '_redis'
        self.port: int = config.ports['redis']
        self.dockerfile_name: str = 'redis.dockerfile'

    def write_to_dockerfile(self, root_path: str):
        """
        Writes the neccessary content to the dockerfile for redis

        """

        dockerfile_content: List[str] = [
            'FROM redis:5',
            'RUN apt update'
        ]
        file = open('{}/.docker/{}'.format(root_path, self.dockerfile_name), 'w')
        for text in dockerfile_content:
            file.write(text + '\n')

    def write_to_docker_compose_file(self, root_path: str):
        """
        Writes the neccessary content to the docker-compose.yml file for redis

        """

        docker_compose_content: List[str] = [
            "  redis:",
            "    container_name: {}".format(self.container_name),
            "    build:",
            "      context: .",
            "      dockerfile: .docker/{}".format(self.dockerfile_name),
            "    ports:",
            "      - '{}:{}'".format(self.port, self.port),
            "    networks:",
            "      - {}-network".format(self.prefix)
        ]
        file = open('{}/docker-compose.yml'.format(root_path), 'a')
        for text in docker_compose_content:
            file.write(text + '\n')