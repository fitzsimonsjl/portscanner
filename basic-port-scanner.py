# TODO:
# 1. Take specificed host
# 2. Create new connection and go through ports ranged 1 - 1025, testing response
# 3. Append response to an array, saving to CSV to be analysed later

import socket
import csv

host = "scanme.nmap.com"

open_ports = []
closed_ports = []


def scan_ports():
    for port in range(1, 501):
        conn_sock = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        )  # Specifies default as TCP, we can choose
        conn_sock.settimeout(2)
        response = conn_sock.connect_ex((host, port))
        if response == 0:
            print(f"{port} is open")
            open_ports.append(port)
        else:
            print(f"{port} is closed")
            closed_ports.append(port)


scan_ports()


def write_response_to_csv():
    open_ports_data = open_ports
    with open("open-ports.csv", "w") as opf:
        writer = csv.writer(opf)
        writer.writerow(open_ports_data)
    closed_ports_data = closed_ports
    with open("closed-ports.csv", "w") as cpf:
        writer = csv.writer(cpf)
        writer.writerow(closed_ports_data)


write_response_to_csv()
