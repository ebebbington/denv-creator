import config
import os

"""
...
Usage
---------
mongoseeder = mongoseeder('prefix name e.g. myprojectname')
mongoseeder.write_to_*()

"""

class MongoSeeder:
    """
    A class used to represent the mongoseeder container

    ...

    Attributes
    ----------
    prefix : str
        The prefix applied for all container names
    container_name : str
        the name to give the containr inside the dockerfile
    dockerfile_name : str
        a formatted string that defines the name of the docker file for mongoseeder

    Methods
    -------
    write_to_dockerfile()
        Writes the neccessary content to the dockerfile for mongoseeder

    write_to_docker_compose_file()
        Appends to the docker compose file with the neccessary mongoseeder content
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
            a formatted string that defines the name of the docker file for mongoseeder
        """
        self.prefix: str = prefix_for_containers
        self.container_name: str = prefix_for_containers + '_mongoseeder'
        self.dockerfile_name: str = 'mongoseeder.dockerfile'

    def create_dump_dir(self, root_path):
        """
        Create the empty data dump directory
        """

        os.mkdir('{}/.docker/data/mongo-data-dump'.format(root_path))

    def write_to_dockerfile(self, root_path: str):
        """
        Writes the neccessary content to the dockerfile for mongoseeder

        """

        dockerfile_content: List[str] = [
            'FROM mongo',
            'COPY ./.docker/data/mongo-data-dump /mongo_data',
            'CMD mongorestore --host mongodb --db db /mongo_data'
        ]
        file = open('{}/.docker/{}'.format(root_path, self.dockerfile_name), 'w')
        for text in dockerfile_content:
            file.write(text + '\n')

    def write_to_docker_compose_file(self, root_path: str):
        """
        Writes the neccessary content to the docker-compose.yml file for mongoseeder

        """

        docker_compose_content: List[str] = [
            "  mongoseeder:",
            "    container_name: {}".format(self.container_name),
            "    build:",
            "      context: .",
            "      dockerfile: .docker/{}".format(self.dockerfile_name),
            "    depends_on:",
            "      - mongodb",
            "    networks:",
            "      - {}-network".format(self.prefix)
        ]
        file = open('{}/docker-compose.yml'.format(root_path), 'a')
        for text in docker_compose_content:
            file.write(text + '\n')