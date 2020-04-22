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
    get_dockerfile_content()
        Returns the necessary content to the dockerfile for mongoseeder

    get_docker_docker_compose_content()
        Returns to the docker compose file with the necessary mongoseeder content

    create_dump_dir()
        Creates a basic dump directory to seed from
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

    def create_dump_dir(self, root_path: str):
        """
        Create the empty data dump directory
        """

        os.mkdir('{}/.docker/data/mongo-data-dump'.format(root_path))

    def get_dockerfile_content(self):
        """
        Returns the neccessary content to the dockerfile for mongoseeder

        """

        dockerfile_content: List[str] = [
            'FROM mongo',
            'COPY ./.docker/data/mongo-data-dump /mongo_data',
            'CMD mongorestore --host mongodb --db db /mongo_data'
        ]
        return dockerfile_content

    def get_docker_compose_content(self):
        """
        Returns the neccessary content to the docker-compose.yml file for mongoseeder

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
        return docker_compose_content