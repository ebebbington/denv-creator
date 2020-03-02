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
    write_to_dockerfile()
        Writes the neccessary content to the dockerfile for apache

    write_to_docker_compose_file()
        Appends to the docker compose file with the neccessary apache content

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
            port for apache to run on
        dockerfile_name : str
            a formatted string that defines the name of the docker file for apache
        """
        self.prefix: str = prefix_for_containers
        self.container_name: str = prefix_for_containers + '_apache'
        self.port: int = config.ports['apache']
        self.dockerfile_name: str = 'apache.dockerfile'

    def write_to_dockerfile(self, root_path: str):
        """
        Writes the neccessary content to the dockerfile for apache

        """

        dockerfile_content: List[str] = [
            'FROM httpd:2.4.33-alpine',
            'RUN apk update; \\',
            '  && apk upgrade;',
            'COPY apache.conf /usr/local/apache2/conf/demo.apache.conf',
            'RUN echo "Include /usr/local/apache2/conf/apache.conf" \\',
            '  >> /usr/local/apache2/conf/httpd.conf',
        ]
        file = open('{}/.docker/{}'.format(root_path, self.dockerfile_name), 'w')
        for text in dockerfile_content:
            file.write(text + '\n')

    def write_to_docker_compose_file(self, root_path: str):
        """
        Writes the neccessary content to the docker-compose.yml file for apache

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
        file = open('{}/docker-compose.yml'.format(root_path), 'a')
        for text in docker_compose_content:
            file.write(text + '\n')

    def write_to_config_file(self, root_path: str):
        """
        Writes the neccessary content to the config file for apache with php-fpm support commented out
    
        """

        config_content: List[str] = [
            'ServerName localhost',
            '',
            'LoadModule deflate_module /usr/local/apache2/modules/mod_deflate.so',
            'LoadModule proxy_module /usr/local/apache2/modules/mod_proxy.so',
            'LoadModule proxy_fcgi_module /usr/local/apache2/modules/mod_proxy_fcgi.so',

            '<VirtualHost *:{}>'.format(self.port),
            '  #ProxyPassMatch ^/(.*\.php(/.*)?)$ fcgi://php:9000/var/www/html/$1',
            '  DocumentRoot /var/www/asrc/',
            '  <Directory /var/www/src/>',
            '    #DirectoryIndex index.php',
            '    Options Indexes FollowSymLinks',
            '    AllowOverride All',
            '    Require all granted',
            '  </Directory>',
            '  CustomLog /proc/self/fd/1 common',
            '  ErrorLog /proc/self/fd/2',
            '</VirtualHost>'
        ]
        file = open('{}/.docker/config/apache.conf'.format(root_path), 'w')
        for text in config_content:
            file.write(text + '\n')

    def update_services_to_depend_on(self, depends_on_string: str):
        self.depends_on_string = depends_on_string