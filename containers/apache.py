import config

"""
...
Usage
---------
apache = apache('prefix name e.g. myprojectname')
apache.write_to_*()

"""

class Apache:
    """
    A class used to represent the apache container

    ...

    Attributes
    ----------
    prefix : str
        The prefix applied for all container names
    container_name : str
        the name to give the containr inside the dockerfile
    port : int
        port for apache to run on
    dockerfile_name : str
        a formatted string that defines the name of the docker file for apache

    Methods
    -------
    get_dockerfile_content()
        Returns the necessary content to the dockerfile for apache

    get_docker_compose_content()
        Returns to the docker compose file with the neccessary apache content

    get_config_content()
        Writes the necessary content to the config file with php-fpm support
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
            port for apache to run on
        dockerfile_name : str
            a formatted string that defines the name of the docker file for apache
        """
        self.prefix: str = prefix_for_containers
        self.container_name: str = prefix_for_containers + '_apache'
        self.port: int = config.ports['apache']
        self.dockerfile_name: str = 'apache.dockerfile'
        self.depends_on_string = ''

    def get_dockerfile_content(self):
        """
        Returns the necessary content to the dockerfile for apache

        """

        dockerfile_content: List[str] = [
            'FROM httpd:2.4',
            '',
            'RUN apt update -y',
            'COPY .docker/conf/apache.conf /usr/local/apache2/conf/demoapache.conf',
            'RUN echo "\\nInclude /usr/local/apache2/conf/demoapache.conf" >> /usr/local/apache2/conf/httpd.conf',
            'RUN cat /usr/local/apache2/conf/httpd.conf',
        ]
        return dockerfile_content

    def get_docker_compose_content(self):
        """
        Returns the neccessary content to the docker-compose.yml file for apache

        """

        docker_compose_content: List[str] = [
            "  apache:",
            "    container_name: {}".format(self.container_name),
            "    build:",
            "      context: .",
            "      dockerfile: .docker/{}".format(self.dockerfile_name),
            "    volumes:",
            "      - ./src:/var/www/src",
            "    working_dir: /var/www/src",
            "    ports:",
            "      - '{}:{}'".format(self.port, self.port),
            "    networks:",
            "      - {}-network".format(self.prefix)
        ]
        if self.depends_on_string != '':
            docker_compose_content.insert(2, self.depends_on_string)
        return docker_compose_content

    def get_config_content(self):
        """
        Returns the necessary content to the config file for apache with php-fpm support commented out
    
        """

        config_content: List[str] = [
            'LoadModule proxy_module /usr/local/apache2/modules/mod_proxy.so',
            'LoadModule proxy_http_module modules/mod_proxy_http.so',
            '',
            '<VirtualHost *:80>',
            '  ProxyPass / http://your_container_name:port/',
            '</VirtualHost>'
        ]
        return config_content

    def update_services_to_depend_on(self, depends_on_string: str):
        self.depends_on_string = depends_on_string