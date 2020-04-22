import config

"""
...
Usage
---------
mongo = mongo('prefix name e.g. myprojectname')
mongo.write_to_*()

"""

class Mongo:
    """
    A class used to represent the mongo container

    ...

    Attributes
    ----------
    prefix : str
        The prefix applied for all container names
    container_name : str
        the name to give the containr inside the dockerfile

    Methods
    -------
    get_docker_compose_content()
        Returns to the docker compose file with the neccessary mongo content

    get_env_content(root_path: str)
        Returns the environmental file content
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
            a formatted string that defines the name of the docker file for mongo
        """
        self.prefix: str = prefix_for_containers
        self.container_name: str = prefix_for_containers + '_mongo'

    def get_docker_compose_content(self):
        """
        Returns the neccessary content to the docker-compose.yml file for mongo

        """

        docker_compose_content: List[str] = [
            "  mongodb:",
            "    container_name: {}".format(self.container_name),
            "    image: mongo",
            "    ports:",
            '      "27017:27017"',
            "    env_file:",
            "      - ./.docker/env/mongo.env",
            "    networks:",
            "      - {}-network".format(self.prefix)
        ]
        return docker_compose_content

    def get_env_content(self):
        """
        Returns the environment file content

        """
        content = [
            'MONGODB_ROOT_USERNAME=root',
            'MONGODB_ROOT_PASSWD=rootpassword',
            'MONGODB_ROOT_ROLE=root',
            'MONGODB_USERNAME=user',
            'MONGODB_PASSWD=password',
            'MONGODB_DBNAME=db',
            'MONGODB_ROLE=readWrite'
        ]
        return content