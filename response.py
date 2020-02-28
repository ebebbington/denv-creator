class Response:
    """
    A class used to sent responses to the console such as info, or getting input

    ...

    Methods
    -------
    ask_for_input(message)
        Gets input from the console, passing in a param as the message and returns

    show_info(message)
        Shows information in the console which is coloured green

    show_error(message)
        Outputs an error message to the console in red

    show_log(message)
        Outputs general logging messages to the kernal
    """

    def ask_for_input(message: str):
        """
        Gets input from the console, passing in a param as the message and returns

        """

        return str(input('\n{}'.format(message)))

    def show_info(message: str):
        """
        Shows information in the console which is coloured green

        """

        print('\n\033[92m{}\x1b[0m'.format(message))

    def show_error(message: str):
        """
        Outputs an error message to the console in red

        """

        print('\n\033[91m{}\x1b[0m\n'.format(message))
        exit()
    
    def show_log(message: str):
        """
        Outputs general logging messages to the kernal

        """

        print(message)