import config

"""
...
Usage
---------
Sql = Sql('prefix name e.g. myprojectname')
Sql.write_to_*()

"""

class Sql:
    """
    A class used to represent the Sql container

    ...

    Attributes
    ----------
    prefix : str
        The prefix applied for all container names
    container_name : str
        the name to give the containr inside the dockerfile
    dockerfile_name : str
        a formatted string that defines the name of the docker file for sql

    Methods
    -------
    get_dockerfile_content()
        Returns the necessary content to the dockerfile for sql

    get_docker_compose_content()
        Returns to the docker compose file with the necessary sql content

    create_dump_file(root_path: str)
        Creates an empty dump file

    create_env_file(root_path: str)
        Creates an environmental file and adds the default credentials
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
            a formatted string that defines the name of the docker file for sql
        """
        self.prefix: str = prefix_for_containers
        self.container_name: str = prefix_for_containers + '_sql'
        self.dockerfile_name: str = 'sql.dockerfile'

    def get_dockerfile_content(self):
        """
        Returns the neccessary content to the dockerfile for sql

        """

        dockerfile_content: List[str] = [
            'FROM mysql:5.6',
            '# Update and install required packages',
            'RUN apt-get update -y',
            '',
            'COPY    ./.docker/data/sql-data-dump.sql /docker-entrypoint-initdb.d/'
        ]
        return dockerfile_content

    def create_dump_file(self, root_path: str):
        """
       Creates an empty dump file

        """
        open('{}/.docker/data/sql-data-dump.sql'.format(root_path), 'x').close()

    def create_env_file(self, root_path: str):
        """
        Creates an environmental file with default credentials

        """
        content = [
            'MYSQL_ROOT_PASSWORD=rootpassword',
            'MYSQL_DATABASE=db',
            'MYSQL_USER=user',
            'MYSQL_PASSWORD=password'
        ]
        file = open('{}/.docker/env/sql.env'.format(root_path), 'x')
        for text in content:
            file.write(text + '\n')

    def get_docker_compose_content(self):
        """
        Returns the necessary content to the docker-compose.yml file for sql

        """

        docker_compose_content: List[str] = [
            "  sql:",
            "    container_name: {}".format(self.container_name),
            "    build:",
            "      context: .",
            "      dockerfile: .docker/{}".format(self.dockerfile_name),
            "    ports:",
            '      - "3007:3006"',
            "    env_file:",
            "      - ./.docker/env/sql.env",
            "    networks:",
            "      - {}-network".format(self.prefix)
        ]
        return docker_compose_content