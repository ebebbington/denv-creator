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
    write_to_dockerfile()
        Writes the neccessary content to the dockerfile for nginx

    write_to_docker_compose_file()
        Appends to the docker compose file with the neccessary nginx content

    write_to_config_file_with_php_fpm()
        Writes the neccessary content to the config file with php-fpm support

    write_to_config_file_without_php_fpm()
        Writes the neccessary content to the config file where the php-fpm support is commented out
    """

    def __init__(self, prefix_for_containers):
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
        self.prefix = prefix_for_containers
        self.container_name = prefix_for_containers + '_nginx'
        self.port = 3001
        self.dockerfile_name = 'nginx.dockerfile'

    def write_to_dockerfile(self):
        """
        Writes the neccessary content to the dockerfile for nginx

        """

        dockerfile_content = [
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
        file = open('./.docker/{}'.format(self.dockerfile_name), 'w')
        for text in dockerfile_content:
            file.write(text + '\n')

    def write_to_docker_compose_file(self):
        """
        Writes the neccessary content to the docker-compose.yml file for nginx

        """

        docker_compose_content = [
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
        file = open('./docker-compose.yml', 'a')
        for text in docker_compose_content:
            file.write(text + '\n')

    def write_to_config_file_with_php_fpm(self):
        """
        Writes the neccessary content to the config file for nginx with php-fpm support

        """

        config_content = [
            'server {',
	        '  listen {};'.format(self.port),
            '',
            '  ##',
            '  # PHP-FPM',
            '  ##',
            '  location ~ \.php$ {',
  	        '    include /etc/nginx/fastcgi_params;',
		    '    root /var/www/src;',
            '    fastcgi_split_path_info ^(.+?\.php)(/.*)$;',
            '    fastcgi_pass	phpfpm:3002;',
		    '    fastcgi_param SCRIPT_FILENAME $document_root/$fastcgi_script_name;',
            '  }',
            '',
            '  location / {',
		    '    root /var/www/src;',
		    '    index index.php;',
		    '    rewrite ^ /index.php?$args last; break;',
	        '  }',
            '}'
        ]
        file = open('./.docker/config/nginx.conf', 'w')
        for text in config_content:
            file.write(text + '\n')

    def write_to_config_file_without_php_fpm(self):
        """
        Writes the neccessary content to the config file for nginx with php-fpm support commented out
    
        """

        self.config_content = [
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
        file = open('./.docker/config/nginx.conf', 'w')
        for text in config_content:
            file.write(text + '\n')