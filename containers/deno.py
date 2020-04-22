import config

"""
...
Usage
---------
deno = Deno('prefix name e.g. myprojectname')
deno.write_to_*()

"""

class Deno:
    """
    A class used to represent the Deno container

    ...

    Attributes
    ----------
    prefix : str
        The prefix applied for all container names
    container_name : str
        the name to give the container inside the dockerfile
    dockerfile_name : str
        a formatted string that defines the name of the docker file for node

    Methods
    -------
    get_dockerfile_content()
        Gets the necessary content for the dockerfile for deno

    get_docker_compose_content()
        Gets to the docker compose content for deno
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
            a formatted string that defines the name of the docker file for deno
        """
        self.prefix: str = prefix_for_containers
        self.container_name: str = prefix_for_containers + '_deno'
        self.dockerfile_name: str = 'deno.dockerfile'
        self.port = config.ports['deno']

    def get_dockerfile_content(self):
        """
        Writes the necessary content to the dockerfile for deno

        """

        dockerfile_content: List[str] = [
            'FROM debian:stable-slim',
            '',
            'RUN apt update -y',
            'RUN apt install bash curl unzip -y',
            '',
            'RUN curl -fsSL https://deno.land/x/install/install.sh | DENO_INSTALL=/usr/local sh -s v0.39.0',
            'RUN export DENO_INSTALL="/root/.local"',
            'RUN export PATH="$DENO_INSTALL/bin:$PATH"'
        ]
        return dockerfile_content

    def get_docker_compose_content(self):
        """
        Returns the necessary content for the docker-compose.yml file for node

        """

        docker_compose_content: List[str] = [
            "  drash:",
            "    container_name: {}".format(self.container_name),
            "    build:",
            "      context: .",
            "      dockerfile: .docker/{}".format(self.dockerfile_name),
            "    volumes:",
            "      - ./src:/var/www/src",
            "    working_dir: /var/www/src",
            "    ports:",
            '      - "{}:{}"'.format(self.port, self.port),
            '    command: bash -c "deno --allow-net app.ts"',
            "    networks:",
            "      - {}-network".format(self.prefix)
        ]
        return docker_compose_content