CMD_LEN = 2
PARAMS_LEN = 12
SERVER_FUNCTIONS_LEN = 8
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000
SERVER_ADDRESS = (SERVER_IP, SERVER_PORT)
CMD_INPUT = f'Type one of the server commands:\n\t'
INITIAL_CLIENT_PRINT = f'If you want to see what the names of the server functions are type "commands_names".\n' \
                       'If you want update the server type "update" and add path to work python file as a parameter.\n' \
                       + '-'*146 +"\n"
PARAMS_INPUT = "Add the necessary parameters. If you add parameters that are not necessary, nothing will happen.\n\t"
ADDR = tuple[str, int]
FULL_REQUEST = tuple[str, str]
