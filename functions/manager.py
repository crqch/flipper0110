from functions.hostname_to_ip import hostname_to_ip
from functions.port_scanner import port_scanner
from menu_handler import add_to_menu


def main():
    add_to_menu("Port Scanner", port_scanner)
    add_to_menu("Hostname > IP", hostname_to_ip)
