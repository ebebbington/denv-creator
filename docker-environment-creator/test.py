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
    dockerfile_content = [
        'FROM nginx:latest',
        '# Update and install required packages',
        'RUN apt-get update',
        'RUN apt-get install vim -y',
        'COPY ./.docker/config/copytube.conf /etc/nginx/conf.d/copytube.conf',
        'ENTRYPOINT ["nginx"]',
        'CMD ["-g","daemon off;"]'
    ]
    file = open('test.txt', 'w')
    for i in dockerfile_content:
        file.write(i + '\n')
#write_array_to_file()

tabs = 'some text:' + '\tsome text part of the above text'
#print(tabs)

# Get directory of where the user was when they executed the script
#print(os.getcwd() + '/../')

f = open('test.deleteme', 'w')
f.remove()