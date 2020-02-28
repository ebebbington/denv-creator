import os

def get_current_directory():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    print(current_dir)

def add_white_spaces_at_start_of_string(text, numberOfSpaces) -> str:
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

def val_is_set(val):
        if len(val) < 1:
            Response.show_error('You did not specify a value')

def check_is_array(vals):
        if not isinstance(vals, list):
            Response.show_error('The given containers is not a list')

def contains_only_one_web_server(container_list):
    possible_web_servers = [
        'nginx',
        'apache'
    ]
    count = 0
    for container in container_list:
        for possible_web_server in possible_web_servers:
            # Create the count
            if possible_web_server == container:
                count = count + 1
            # Check if more thn 2 servers are defined
            if count > 1:
                Response.show_error('You have defined more than one web server')

tabs = 'some text:' + '\tsome text part of the above text'
#print(tabs)

# Get directory of where the user was when they executed the script
#print(os.getcwd() + '/../')