import socket
import response_handlers
from create_update_request import update_request
from common.const import *
from common import protocol


def connect_to_server(address: ADDR) -> socket.socket:
    my_socket = socket.socket()
    my_socket.connect(address)
    return my_socket


def create_request() -> FULL_REQUEST:
    cmd = input(CMD_INPUT).lower()
    if cmd == "update":
        params = update_request()
    else:
        params = [input(PARAMS_INPUT).lower()]
    return cmd, params


def handle_response(response_cmd: str, response_params: str):
    handler_function = getattr(response_handlers, response_cmd)
    handler_function(response_params)
    print("-" * 146)


def is_client_disconnect(cmd: str) -> bool:
    return cmd != "disconnect"


def main():
    my_socket, is_connect = connect_to_server(SERVER_ADDRESS), True
    print(INITIAL_CLIENT_PRINT)
    while is_connect:
        try:
            request_cmd, request_params = create_request()
            protocol.send(my_socket, request_cmd, request_params)
            response_cmd, response_params = protocol.recv(my_socket)
            handle_response(response_cmd, response_params)
            is_connect = is_client_disconnect(request_cmd)
        except KeyboardInterrupt:
            protocol.send(my_socket, "disconnect", "")
            is_connect = False
    my_socket.close()


if __name__ == '__main__':
    main()
