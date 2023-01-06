import base64
from common.const import *


def _read_param(sock, length):
    param = sock.recv(length)
    while len(param) < length:
        param += sock.recv(length - len(param))
    return param


def recv(sock):
    len_cmd = _read_param(sock, CMD_LEN)
    len_cmd = int(len_cmd)

    cmd = _read_param(sock, len_cmd)
    cmd = cmd.decode()

    len_params = _read_param(sock, PARAMS_LEN)
    len_params = int(len_params)

    params = _read_param(sock, len_params)

    try:
        params = [base64.b64decode(i).decode() for i in params.split(b",")]
    except UnicodeDecodeError:
        params = base64.b64decode(params)

    return cmd, params


def send(sock, cmd, params):
    len_cmd = str(len(cmd)).zfill(CMD_LEN)
    try:
        params = ",".join([base64.b64encode(i.encode()).decode() for i in params])
    except (TypeError, AttributeError):
        params = base64.b64encode(params).decode()
    len_params = str(len(params)).zfill(PARAMS_LEN)

    sock.send(f"{len_cmd}{cmd}{len_params}{params}".encode())
