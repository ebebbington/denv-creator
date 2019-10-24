import os

def get_current_directory():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    print(current_dir)

def add_white_spaces_at_start_of_string(text, numberOfSpaces):
    spacey_string = text.rjust(len(text)+numberOfSpaces)
    return spacey_string
spaces = add_white_spaces_at_start_of_string('hello world', 5)
print(spaces)

def get_current_file_name():
    print(__file__)

def write_array_to_file():
    docker_compose_content = [
            "  nginx:",
            "    container_name: {}".format('nginx'),
            "    build:",
            "      context: .",
            "      dockerfile: .docker/{}".format('nginx.dockerfile'),
            "    volumes:",
            "      - ./src:/var/www/src",
            "    working_dir: /var/www/src",
            "    ports:",
            "      - '{}:{}'".format(3001, 3001),
            "    networks:",
            "      - {}-network".format('test')
    ]
    file = open('./test.txtttt', 'w')
    for i in docker_compose_content:
        file.write(i + '\n')
write_array_to_file()

tabs = 'some text:' + '\tsome text part of the above text'
#print(tabs)

# Get directory of where the user was when they executed the script
#print(os.getcwd() + '/../')