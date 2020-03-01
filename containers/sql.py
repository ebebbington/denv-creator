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
    write_to_dockerfile(root_path: str)
        Writes the neccessary content to the dockerfile for sql

    write_to_docker_compose_file(root_path: str)
        Appends to the docker compose file with the neccessary sql content

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

    def write_to_dockerfile(self, root_path: str):
        """
        Writes the neccessary content to the dockerfile for sql

        """

        dockerfile_content: List[str] = [
            'FROM mysql:5.6',
            '# Update and install required packages',
            'RUN apt-get update -y',
            '',
            'COPY    ./.docker/data/sql-data-dump.sql /docker-entrypoint-initdb.d/'
        ]
        file = open('{}/.docker/{}'.format(root_path, self.dockerfile_name), 'w')
        for text in dockerfile_content:
            file.write(text + '\n')

    def create_dump_file(self, root_path: str):
        """
       Creates an empty dump file

        """
        open('{}/.docker/data/sql-data-dump.sql'.format(root_path), 'x')

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

    def write_to_docker_compose_file(self, root_path: str):
        """
        Writes the neccessary content to the docker-compose.yml file for sql

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
        file = open('{}/docker-compose.yml'.format(root_path), 'a')
        for text in docker_compose_content:
            file.write(text + '\n')