# TODO:
# 1. Take specificed host
# 2. Create new connection and go through ports ranged 1 - 1025, testing response
# 3. Append response to a list, saving to CSV to be analysed later
# 4. Try-catch error handling

import socket
import csv
import sys

host = "scanme.nmap.com"

open_ports = []
closed_ports = []

red = "\033[0;91m"
green = "\033[0;92m"


def scan_ports():
    for port in range(1, 500):
        conn_sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,  # AF_INET specifies "Address Family" - in this case IPv4
        )  # Specifies default as TCP, we can choose SOCK_DGRAM if we wanted to use UDP
        conn_sock.settimeout(10)
        response = conn_sock.connect_ex((host, port))
        if response == 0:
            print(green + f"{port} is open")
            open_ports.append(port)
        else:
            print(red + f"{port} is closed")
            closed_ports.append(port)


scan_ports()


def write_response_to_csv():
    open_ports_data = open_ports
    with open("open-ports.csv", "w") as opf:  # 'open ports file'
        writer = csv.writer(opf)
        writer.writerows(zip(open_ports_data))
    closed_ports_data = closed_ports
    with open("closed-ports.csv", "w") as cpf:  # 'closed ports file'
        writer = csv.writer(cpf)
        writer.writerows(zip(closed_ports_data))


write_response_to_csv()
