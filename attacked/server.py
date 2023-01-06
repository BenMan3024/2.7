import socket
import non_update_functions
import logging
import functions
from colorama import Fore
from common.const import *
from common import protocol


logging.basicConfig(level=logging.DEBUG)


def run_server() -> socket.socket:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(SERVER_ADDRESS)
    logging.info(f"[RUNNING] SERVER IS UP AND RUNNING AT {SERVER_ADDRESS}." + Fore.MAGENTA)
    server_socket.listen()
    return server_socket


def connect_client(server_socket: socket.socket):
    logging.info("[LISTENING] WAITING FOR CLIENTS...")
    client_socket, client_address = server_socket.accept()
    logging.critical("[NEW CONNECTION] {client_address} CONNECT TO SERVER")
    return client_socket, client_address


def handle_request(request_cmd: str, request_params: str, client_address: ADDR):
    logging.info(f"{client_address} sent the command "
            f"{request_cmd} and add the params {request_params}")
    try:
        func = getattr(functions, request_cmd)
        keep_running, response_cmd, response_params = func(request_params)
    except AttributeError:
        try:
            keep_running, response_cmd, response_params = getattr(non_update_functions, request_cmd)(request_params)
        except AttributeError:
            keep_running, response_cmd, response_params = True, "string_handler", [f"THERE IS NO FUNCTION NAMED {request_cmd}"]
    return keep_running, response_cmd, response_params


def main():
    server_socket = run_server()
    while True:
        is_connect = True
        client_socket, client_address = connect_client(server_socket)
        while is_connect:
            request_cmd, request_params = protocol.recv(client_socket)
            is_connect, response_cmd, response_params = handle_request(request_cmd, request_params, client_address)
            protocol.send(client_socket, response_cmd, response_params)
        logging.critical(f"{client_address} disconnect from the server")
        client_socket.close()


if __name__ == '__main__':
    main()
