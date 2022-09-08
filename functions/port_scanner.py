import socket
import os
import sys
import time
from datetime import datetime
from time import sleep
import threading
import concurrent.futures
from colorama import Fore

print_lock = threading.Lock()


def scan_thread(port, remoteServerIP):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((remoteServerIP, port))
        sock.close()
        with print_lock:
            print(f"{Fore.LIGHTGREEN_EX}[+] Port {port}: 	Open")
    except socket.timeout:
        pass


def port_scanner():
    os.system('cls')

    remoteServer = input(f"{Fore.GREEN}Enter a remote host to scan: ")
    try:
        remoteServerIP = socket.gethostbyname(remoteServer)
    except socket.gaierror:
        print(f"{Fore.RED}[!] Hostname could not be resolved. Exiting")
        sys.exit()
    try:
        fromPort = int(input(f"{Fore.GREEN}Enter from which port to scan: "))
        toPort = int(input(f"{Fore.GREEN}Enter to which port to scan: "))
        threads = input(f"{Fore.GREEN}How much threads should be used (enter for 10000): ")
        if threads == "":
            threads = 10000
        else:
            threads = int(threads)
    except ValueError:
        print(f"{Fore.RED}[!] Invalid number")
        sleep(1)
        sys.exit()

    print(f"{Fore.GREEN}Scanning remote host {remoteServerIP}")

    t1 = datetime.now()
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            for port in range(fromPort, toPort):
                executor.submit(scan_thread, port, remoteServerIP)

    except socket.gaierror:
        print(f'{Fore.RED}[!] Hostname could not be resolved. Exiting')
        time.sleep(3)
        sys.exit()

    except socket.error:
        print(f'{Fore.RED}[!] Couldn\'t connect to server')
        time.sleep(3)
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1

    # Printing the information to screen
    print(f'{Fore.LIGHTGREEN_EX}Scanning lasted for {Fore.GREEN}' + total.__str__() + f' {Fore.LIGHTGREEN_EX}!\n\n')
    input(f'{Fore.LIGHTYELLOW_EX}Press any key to return to the menu...')
