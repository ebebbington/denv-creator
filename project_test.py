from project import Project
import unittest
from unittest.mock import patch
from unittest import mock
from unittest import TestCase
import os
from pprint import pprint
import shutil

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
        print(1)
        # TODO
        #    nginx, phpfpm, node, python, sql, mongo, mongoseeder, apache, redis

    def test_init_docker_compose_file(self):
        project = Project()
        # TODO :: assert the below is inside the file when the mehthod is implemented
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