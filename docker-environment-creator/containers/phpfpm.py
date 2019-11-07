class Phpfpm:

    """
    A class used to represent the Php-fpm container

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
            the name to give the container inside the dockerfile
        port : int
            port for phpfpm to run on
        dockerfile_name : str
            a formatted string that defines the name of the docker file for phpfpm
        """
        self.prefix = prefix_for_containers
        self.container_name = prefix_for_containers + '_phpfpm'
        self.port = 3002
        self.dockerfile_name = 'phpfpm.dockerfile'

    def write_to_dockerfile(self):
        """
        Writes the neccessary content to the dockerfile for nginx

        """

        dockerfile_content = [
            'FROM php:7.3-fpm',
            '',
            '# Update and install required packages and dependencies',
            'RUN apt-get update -y && apt-get install apt-transport-https -y',
            'RUN apt-get install vim -y',
            'RUN apt-get install apt-utils -y',
            'RUN apt-get install libc-client-dev -y',
            'RUN apt-get install libzip-dev -y',
            'RUN apt-get install -y libxml2-dev libxslt-dev python-dev --no-install-recommends',
            'RUN apt-get install -y libldb-dev libldap2-dev',
            'RUN apt-get install -y libpng-dev',
            '',
            '# Avilable extensions by default when using docker-php-ext-install',
            '# bcmath bz2 calendar ctype curl dba dom mysqli enchant exif fileinfo filter ftp gd gettext gmp hash iconv imap interbase intl json ldap mbstring mysqli oci8 odbc opcache pcntl pdo pdo_dblib pdo_firebird pdo_mysql pdo_oci pdo_odbc pdo_pgsql pdo_sqlite pgsql phar posix pspell readline recode reflection session shmop simplexml snmp soap sockets sodium spl standard sysvmsg sysvsem sysvshm tidy tokenizer wddx xml xmlreader xmlrpc xmlwriter xsl zend_test zip',
            'RUN docker-php-ext-install pdo pdo_mysql mysqli xml json ldap mbstring soap gd xsl zip sockets',
            '',
            '# Configure php.ini',
            'COPY ./.docker/config/phpfpm/php.ini /etc/php.ini',
            '',
            '# Install composer',
            'RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer'
        ]

        file = open('./.docker/{}'.format(self.dockerfile_name), 'w')
        for text in dockerfile_content:
            file.write(text + '\n')

    def write_to_docker_compose_file(self):
        """
        Writes the neccessary content to the docker-compose.yml file for nginx

        """

        docker_compose_content = [
            'phpfpm:',
            '  container_name: {}_phpfpm'.format(self.prefix),
            '  build:',
            '    context: .',
            '    dockerfile: .docker/{}'.format(self.dockerfile_name),
            '  depends_on:',
            '    - sql',
            '  ports:',
            '    - {}:{}'.format(self.port),
            '  volumes:',
            '    - ./src:/var/www/src',
            '  command: bash -c "composer install && php-fpm -F"',
            '  working_dir: /var/www/src',
            '  networks:',
            '    - {}-network'.format(self.prefix)
        ]
        
        file = open('./docker-compose.yml', 'a')
        for text in docker_compose_content:
            file.write(text + '\n')

    def create_php_ini_file:
        from shutil import copyfile
        copyfile('data/php.ini', '.docker/config/php.ini')