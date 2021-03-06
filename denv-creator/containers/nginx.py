import config

"""
...
Usage
---------
Nginx = Nginx('prefix name e.g. myprojectname')
Nginx.write_to_*()

"""

class Nginx:
    """
    A class used to represent the Nginx container

    ...

    Attributes
    ----------
    prefix : str
        The prefix applied for all container names
    container_name : str
        the name to give the containr inside the dockerfile
    port : int
        port for nginx to run on
    dockerfile_name : str
        a formatted string that defines the name of the docker file for nginx

    Methods
    -------
    get_dockerfile_content()
        Returns the neccessary content for the dockerfile for nginx

    get_docker_compose_content()
        Returns the docker compose content neccessary necessary for nginx

    write_to_config_file()
        returns the neccessary content for the config file with php-fpm support
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
            port for nginx to run on
        dockerfile_name : str
            a formatted string that defines the name of the docker file for nginx
        """
        self.prefix: str = prefix_for_containers
        self.container_name: str = prefix_for_containers + '_nginx'
        self.port: int = config.ports['nginx']
        self.dockerfile_name: str = 'nginx.dockerfile'

    def get_dockerfile_content(self):
        """
        Holds the neccessary content for the dockerfile for nginx

        """

        dockerfile_content: List[str] = [
            'FROM nginx:latest',
            '# Update and install required packages',
            'RUN apt-get update',
            'RUN apt-get install vim -y',
            '',
            'COPY ./.docker/config/nginx.conf /etc/nginx/conf.d/nginx.conf',
            '',
            'ENTRYPOINT ["nginx"]',
            'CMD ["-g","daemon off;"]'
        ]
        return dockerfile_content

    def get_docker_compose_content(self):
        """
        Holds the neccessary content for the docker-compose.yml file for nginx

        """

        docker_compose_content: List[str] = [
            "  nginx:",
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

    def get_config_file_content(self):
        """
        Holds the neccessary content for the config file for nginx with php-fpm support commented out
    
        """

        config_content: List[str] = [
            'server {',
	        '  listen {};'.format(self.port),
            '',
            '  ##',
            '  # PHP-FPM',
            '  ##',
            '  #location ~ \.php$ {',
  	        '    #include /etc/nginx/fastcgi_params;',
		    '    #root /var/www/src;',
            '    #fastcgi_split_path_info ^(.+?\.php)(/.*)$;',
            '    #fastcgi_pass	phpfpm:3002;',
		    '    #fastcgi_param SCRIPT_FILENAME $document_root/$fastcgi_script_name;',
            '  #}',
            '',
            '  location / {',
		    '    root /var/www/src;',
            '    index index.html;'
		    '    #index index.php;',
		    '    #rewrite ^ /index.php?$args last; break;',
	        '  }',
            '}'
        ]
        return config_content

    def update_services_to_depend_on(self, depends_on_string: str):
        self.depends_on_string = depends_on_string