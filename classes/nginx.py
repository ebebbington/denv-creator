class Nginx:

    def __init__(self, container_name, port):
        self.service_name = 'nginx'
        self.container_name = container_name
        self.dockerfile = self.service_name + '.dockerfile'
        self.port = port

    def setup_dockerfile_content:
        self.dockerfile_content = [
            'FROM nginx:latest',
            '# Update and install required packages',
            'RUN apt-get update',
            'RUN apt-get install vim -y',
            '\n',
            'COPY ./.docker/config/copytube.conf /etc/nginx/conf.d/copytube.conf',
            '\n',
            'ENTRYPOINT ["nginx"]',
            'CMD ["-g","daemon off;"]'
        ]

    def create_dockerfile: 
