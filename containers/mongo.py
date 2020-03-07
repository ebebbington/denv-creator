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
    write_to_docker_compose_file(root_path: str)
        Appends to the docker compose file with the neccessary mongo content

    create_env_file(root_path: str)
        Creates the environmental file
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

    def write_to_docker_compose_file(self, root_path: str):
        """
        Writes the neccessary content to the docker-compose.yml file for mongo

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
        file = open('{}/docker-compose.yml'.format(root_path), 'a')
        for text in docker_compose_content:
            file.write(text + '\n')

    def create_env_file(self, root_path: str):
        """
        Creates the environment file

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
        file = open('{}/.docker/env/mongo.env'.format(root_path), 'a')
        for text in content:
            file.write(text + '\n')