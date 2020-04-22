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
    get_dockerfile_content()
        Returns the necessary content to the dockerfile for redis

    get_docker_compose_content()
        Returns to the docker compose file with the neccessary redis content

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

    def get_dockerfile_content(self):
        """
        Returns the necessary content to the dockerfile for redis

        """

        dockerfile_content: List[str] = [
            'FROM redis:5',
            'RUN apt update'
        ]
        return dockerfile_content

    def get_docker_compose_content(self):
        """
        Returns the necessary content to the docker-compose.yml file for redis

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
        return docker_compose_content