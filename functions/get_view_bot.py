import socket
import os
import sys
import time
from datetime import datetime
from time import sleep
import threading
import concurrent.futures

import requests
from colorama import Fore

print_lock = threading.Lock()
count = 0


def get_view(hostname):
    global count
    requests.get(hostname)
    with print_lock:
        count += 1
        print(f"{Fore.LIGHTYELLOW_EX}[-] {count}", end='\r')


def get_view_bot():
    os.system('cls')

    hostname = input(f"{Fore.GREEN}Enter hostname to send GET requests: ")
    try:
        requests.get(hostname)
    except requests.exceptions.ConnectionError:
        print(f"{Fore.RED}[!] Hostname could not be resolved. Exiting")
        sys.exit()
    try:
        viewCount = int(input(f"{Fore.GREEN}Enter the number of requests: "))
        threads = input(f"{Fore.GREEN}How much threads should be used (enter for 2000): ")
        if threads == "":
            threads = 2000
        else:
            threads = int(threads)
        if threads > viewCount:
            threads = viewCount
    except ValueError:
        print(f"{Fore.RED}[!] Invalid number")
        sleep(1)
        sys.exit()

    print(f"{Fore.GREEN}Generating {viewCount} requests to {hostname}\n\n")
    t1 = datetime.now()
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            for i in range(viewCount):
                executor.submit(get_view, hostname)
    except requests.exceptions.ConnectionError:
        print(f'{Fore.RED}[!] Hostname could not be resolved. Exiting')
        time.sleep(3)
        sys.exit()

    print(f"{Fore.LIGHTGREEN_EX}[+] {viewCount}")

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1

    # Printing the information to screen
    print(
        f'{Fore.LIGHTGREEN_EX}Generating views lasted for {Fore.GREEN}' + total.__str__() + f' {Fore.LIGHTGREEN_EX}!\n\n')
    input(f'{Fore.LIGHTYELLOW_EX}Press any key to return to the menu...')
