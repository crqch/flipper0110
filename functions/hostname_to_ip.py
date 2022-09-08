import socket
import os
import sys
import time
from datetime import datetime
from time import sleep
import threading
import concurrent.futures
from colorama import Fore


def hostname_to_ip():
    os.system('cls')

    remoteServer = input(f"{Fore.GREEN}Enter a remote host to resolve IP: ")
    try:
        remoteServerIP = socket.gethostbyname(remoteServer)
    except socket.gaierror:
        print(f"{Fore.RED}[!] Hostname could not be resolved. Exiting")
        sys.exit()
    print(f'{Fore.LIGHTGREEN_EX}[+] IP of {remoteServer} is: {Fore.GREEN}{remoteServerIP}\n\n')
    input(f'{Fore.LIGHTYELLOW_EX}Press any key to return to the menu...')
