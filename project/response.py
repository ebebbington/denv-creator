#
# Handles the responding side to the user
#
class Response:

    def ask_for_input(message):
        return str(input('\n{}'.format(message)))

    def show_info(message):
        print('\n\033[92m{}\x1b[0m'.format(message))

    def show_error(message):
        print('\n\033[91m{}\x1b[0m'.format(message))
        exit()