from project import Project
import unittest
from unittest.mock import patch
from unittest import mock
from unittest import TestCase
import os
from pprint import pprint
import shutil
from containers.nginx import Nginx
from containers.phpfpm import Phpfpm
from containers.node import Node
from containers.python import Python
from containers.sql import Sql
from containers.mongo import Mongo
from containers.mongoseeder import MongoSeeder
from containers.apache import Apache
from containers.deno import Deno
from containers.redis import Redis
os.environ['ENV'] = 'testing'

class ProjectTest(unittest.TestCase):

    containers = 'NGINX phpfpm'

    all_ok = 'y'

    @patch('builtins.input', lambda *args: 'test-name')
    def test_set_path(self):
        project = Project()
        project.set_path()
        self.assertEqual(project.name, 'test-name')
        self.assertEqual(project.path, os.getcwd() + '/' + 'test-name')

    # Correct input for containers and all is ok
    @patch('builtins.input', side_effect=[containers, all_ok])
    def test_get_list_of_containers_1(self, mock_input):
        project = Project()
        project.get_list_of_containers()
        self.assertEqual(['nginx', 'phpfpm'], project.containers)

    # Correct input for containers but all not ok
    @patch('builtins.input', side_effect=[containers, 'n'])
    def test_get_list_of_containers_2(self, mock_input):
        project = Project()
        try:
            project.get_list_of_containers()
        except:
            self.assertRaises(SystemExit)

    @patch('builtins.input', lambda *args: 'my-project')
    def test_get_prefix_for_containers(self):
        project = Project()
        project.get_prefix_for_containers()
        self.assertEqual(project.container_prefix, 'my-project')

    def test_add_network_block_to_compose_file(self):
        project = Project()
        # mock the property needed in this method
        project.container_prefix = "hello"
        project.add_network_block_to_compose_file()
        # TODO :: Once implemented then assert this content is inside the file
        text_block: List[str] = [
            'network:',
            '  {}-network:'.format(self.container_prefix),
            '    driver: bridge'
        ]

    def test_init_git_repo(self):
        project = Project()
        project.init_git_repo()
        # TODO :: Assert the project is using git (check for .git folder?)

    def test_create_containers_from_container_list(self):
        # setup
        project = Project()
        project.container_prefix = "my_project"
        project.path = "./my-project"

        # nginx
        project.containers = ["nginx"]
        os.mkdir('my-project')
        os.mkdir('./my-project/.docker')
        os.mkdir('./my-project/.docker/config')
        project.create_containers_from_container_list()
        nginx = Nginx('my_project')
        # start of asserting dockerfile content
        nginx_dockerfile_content = nginx.get_dockerfile_content()
        # add nl char to list to match what is read in file
        new_dockerfile_content = []
        for x in nginx_dockerfile_content:
            new_dockerfile_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/.docker/nginx.dockerfile', 'r')
        for x in f:
          file_contents.append(x)
        self.assertEqual(new_dockerfile_content, file_contents)
        f.close()
        # start of asserting docker compose content
        nginx.depends_on_string = ''
        nginx_docker_compose_content = nginx.get_docker_compose_content()
        new_docker_compose_content = []
        for x in nginx_docker_compose_content:
            new_docker_compose_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/docker-compose.yml', 'r')
        for x in f:
          file_contents.append(x)
        self.assertEqual(new_docker_compose_content, file_contents)
        f.close()
        # start of asserting config file content
        nginx_config_file_content = nginx.get_config_file_content()
        new_config_file_content = []
        for x in nginx_config_file_content:
            new_config_file_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/.docker/config/nginx.conf', 'r')
        for x in f:
          file_contents.append(x)
        self.assertEqual(new_config_file_content, file_contents)
        f.close()
        shutil.rmtree('./my-project')

        # phpfpm
        phpfpm = Phpfpm('my_project')
        project.containers = ["phpfpm"]
        os.mkdir('my-project')
        os.mkdir('./my-project/.docker')
        os.mkdir('./my-project/.docker/config')
        project.create_containers_from_container_list()
        # start of dockerfile content
        phpfpm_dockerfile_content = phpfpm.get_dockerfile_content()
        new_dockerfile_content = []
        for x in phpfpm_dockerfile_content:
            new_dockerfile_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/.docker/phpfpm.dockerfile', 'r')
        for x in f:
          file_contents.append(x)
        self.assertEqual(new_dockerfile_content, file_contents)
        f.close()
        # start of docker compose content
        phpfpm_docker_compose_content = phpfpm.get_docker_compose_content()
        new_docker_compose_content = []
        for x in phpfpm_docker_compose_content:
            new_docker_compose_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/docker-compose.yml', 'r')
        for x in f:
          file_contents.append(x)
        self.assertEqual(new_docker_compose_content, file_contents)
        f.close()
        #start of php ini copy
        phpfpm.create_php_ini_file(project.path)
        self.assertEqual(True, os.path.isfile("./my-project/.docker/config/php.ini"))
        shutil.rmtree('./my-project')

        # node
        node = Node('my_project')
        project.containers = ["node"]
        os.mkdir('my-project')
        os.mkdir('./my-project/.docker')
        os.mkdir('./my-project/.docker/config')
        project.create_containers_from_container_list()
        # start of dockerfile content
        dockerfile_content = node.get_dockerfile_content()
        new_dockerfile_content = []
        for x in dockerfile_content:
            new_dockerfile_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/.docker/node.dockerfile', 'r')
        for x in f:
          file_contents.append(x)
        self.assertEqual(new_dockerfile_content, file_contents)
        f.close()
        # start of docker compose content
        docker_compose_content = node.get_docker_compose_content()
        new_docker_compose_content = []
        for x in docker_compose_content:
            new_docker_compose_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/docker-compose.yml', 'r')
        for x in f:
            file_contents.append(x)
        self.assertEqual(new_docker_compose_content, file_contents)
        f.close()
        shutil.rmtree('./my-project')

        # python
        python = Python('my_project')
        project.containers = ["python"]
        os.mkdir('my-project')
        os.mkdir('./my-project/.docker')
        os.mkdir('./my-project/.docker/config')
        project.create_containers_from_container_list()
        # start of dockerfile content
        dockerfile_content = python.get_dockerfile_content()
        new_dockerfile_content = []
        for x in dockerfile_content:
            new_dockerfile_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/.docker/python.dockerfile', 'r')
        for x in f:
          file_contents.append(x)
        self.assertEqual(new_dockerfile_content, file_contents)
        f.close()
        # start of docker compose content
        docker_compose_content = python.get_docker_compose_content()
        new_docker_compose_content = []
        for x in docker_compose_content:
            new_docker_compose_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/docker-compose.yml', 'r')
        for x in f:
            file_contents.append(x)
        self.assertEqual(new_docker_compose_content, file_contents)
        f.close()
        shutil.rmtree('./my-project')

        # sql
        sql = Sql('my_project')
        project.containers = ["sql"]
        os.mkdir('my-project')
        os.mkdir('./my-project/.docker')
        os.mkdir('./my-project/.docker/config')
        os.mkdir('./my-project/.docker/data')
        os.mkdir('./my-project/.docker/env')
        project.create_containers_from_container_list()
        # start of dockerfile content
        dockerfile_content = sql.get_dockerfile_content()
        new_dockerfile_content = []
        for x in dockerfile_content:
            new_dockerfile_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/.docker/sql.dockerfile', 'r')
        for x in f:
          file_contents.append(x)
        self.assertEqual(new_dockerfile_content, file_contents)
        f.close()
        # start of docker compose content
        docker_compose_content = sql.get_docker_compose_content()
        new_docker_compose_content = []
        for x in docker_compose_content:
            new_docker_compose_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/docker-compose.yml', 'r')
        for x in f:
            file_contents.append(x)
        self.assertEqual(new_docker_compose_content, file_contents)
        # created both env and dump file
        self.assertTrue(os.path.exists('./my-project/.docker/data/sql-data-dump.sql'))
        self.assertTrue(os.path.exists('./my-project/.docker/env/sql.env'))
        f.close()
        shutil.rmtree('./my-project')

        # mongo
        mongo = Mongo('my_project')
        project.containers = ["mongo"]
        os.mkdir('my-project')
        os.mkdir('./my-project/.docker')
        os.mkdir('./my-project/.docker/config')
        os.mkdir('./my-project/.docker/data')
        os.mkdir('./my-project/.docker/env')
        project.create_containers_from_container_list()
        # start of env content
        env_content = mongo.get_env_content()
        new_env_content = []
        for x in env_content:
            new_env_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/.docker/env/mongo.env', 'r')
        for x in f:
          file_contents.append(x)
        self.assertEqual(new_env_content, file_contents)
        f.close()
        # start of docker compose content
        docker_compose_content = mongo.get_docker_compose_content()
        new_docker_compose_content = []
        for x in docker_compose_content:
            new_docker_compose_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/docker-compose.yml', 'r')
        for x in f:
            file_contents.append(x)
        self.assertEqual(new_docker_compose_content, file_contents)
        shutil.rmtree('./my-project')

        # mongoseeder
        mongo_seeder = MongoSeeder('my_project')
        project.containers = ["mongoseeder"]
        os.mkdir('my-project')
        os.mkdir('./my-project/.docker')
        os.mkdir('./my-project/.docker/config')
        os.mkdir('./my-project/.docker/data')
        os.mkdir('./my-project/.docker/env')
        project.create_containers_from_container_list()
        # start of dockerfile content
        dockerfile_content = mongo_seeder.get_dockerfile_content()
        new_dockerfile_content = []
        for x in dockerfile_content:
            new_dockerfile_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/.docker/mongoseeder.dockerfile', 'r')
        for x in f:
          file_contents.append(x)
        self.assertEqual(new_dockerfile_content, file_contents)
        f.close()
        # start of docker compose content
        docker_compose_content = mongo_seeder.get_docker_compose_content()
        new_docker_compose_content = []
        for x in docker_compose_content:
            new_docker_compose_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/docker-compose.yml', 'r')
        for x in f:
            file_contents.append(x)
        self.assertEqual(new_docker_compose_content, file_contents)
        self.assertTrue(os.path.exists('./my-project/.docker/data/mongo-data-dump'))
        shutil.rmtree('./my-project')

        # apache
        apache = Apache('my_project')
        project.containers = ["apache"]
        os.mkdir('my-project')
        os.mkdir('./my-project/.docker')
        os.mkdir('./my-project/.docker/config')
        project.create_containers_from_container_list()
        # start of asserting dockerfile content
        dockerfile_content = apache.get_dockerfile_content()
        # add nl char to list to match what is read in file
        new_dockerfile_content = []
        for x in dockerfile_content:
            new_dockerfile_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/.docker/apache.dockerfile', 'r')
        for x in f:
          file_contents.append(x)
        self.assertEqual(new_dockerfile_content, file_contents)
        f.close()
        # start of asserting docker compose content
        docker_compose_content = apache.get_docker_compose_content()
        new_docker_compose_content = []
        for x in docker_compose_content:
            new_docker_compose_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/docker-compose.yml', 'r')
        for x in f:
          file_contents.append(x)
        self.assertEqual(new_docker_compose_content, file_contents)
        f.close()
        # start of asserting config file content
        config_content = apache.get_config_content()
        new_config_content = []
        for x in config_content:
            new_config_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/.docker/config/demoapache.conf', 'r')
        for x in f:
          file_contents.append(x)
        self.assertEqual(new_config_content, file_contents)
        f.close()
        shutil.rmtree('./my-project')

        # deno
        deno = Deno('my_project')
        project.containers = ["deno"]
        os.mkdir('my-project')
        os.mkdir('./my-project/.docker')
        os.mkdir('./my-project/.docker/config')
        project.create_containers_from_container_list()
        # start of dockerfile content
        dockerfile_content = deno.get_dockerfile_content()
        new_dockerfile_content = []
        for x in dockerfile_content:
            new_dockerfile_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/.docker/deno.dockerfile', 'r')
        for x in f:
          file_contents.append(x)
        self.assertEqual(new_dockerfile_content, file_contents)
        f.close()
        # start of docker compose content
        docker_compose_content = deno.get_docker_compose_content()
        new_docker_compose_content = []
        for x in docker_compose_content:
            new_docker_compose_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/docker-compose.yml', 'r')
        for x in f:
            file_contents.append(x)
        self.assertEqual(new_docker_compose_content, file_contents)
        f.close()
        shutil.rmtree('./my-project')

        # redis
        redis = Redis('my_project')
        project.containers = ["redis"]
        os.mkdir('my-project')
        os.mkdir('./my-project/.docker')
        os.mkdir('./my-project/.docker/config')
        project.create_containers_from_container_list()
        # start of dockerfile content
        dockerfile_content = redis.get_dockerfile_content()
        new_dockerfile_content = []
        for x in dockerfile_content:
            new_dockerfile_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/.docker/redis.dockerfile', 'r')
        for x in f:
          file_contents.append(x)
        self.assertEqual(new_dockerfile_content, file_contents)
        f.close()
        # start of docker compose content
        docker_compose_content = redis.get_docker_compose_content()
        new_docker_compose_content = []
        for x in docker_compose_content:
            new_docker_compose_content.append(x + '\n')
        file_contents = []
        f = open('./my-project/docker-compose.yml', 'r')
        for x in f:
            file_contents.append(x)
        self.assertEqual(new_docker_compose_content, file_contents)
        f.close()
        shutil.rmtree('./my-project')


    def test_init_docker_compose_file(self):
        project = Project()
        # TODO :: assert the below is inside the file when the method is implemented
        text: List[str] = [
            'version: "3"',
            '  services:'
        ]
        project.init_docker_compose_file()

    def test_create_base_files(self):
        project = Project()
        project.path = "./my-project"
        project.create_base_files()
        self.assertEqual(True, os.path.exists("./my-project"))
        self.assertEqual(True, os.path.exists("./my-project/LICENSE.TXT"))
        self.assertEqual(True, os.path.exists("./my-project/.gitignore"))
        self.assertEqual(True, os.path.exists("./my-project/docker-compose.yml"))
        self.assertEqual(True, os.path.exists("./my-project/src"))
        self.assertEqual(True, os.path.exists("./my-project/.docker"))
        self.assertEqual(True, os.path.exists("./my-project/.docker/config"))
        self.assertEqual(True, os.path.exists("./my-project/.docker/data"))
        self.assertEqual(True, os.path.exists("./my-project/.docker/env"))
        shutil.rmtree("./my-project")


if __name__ == '__main__':
    print('[Testing] Project: Started...')
    unittest.main()