#!/usr/bin/env python


import socket
import os
import subprocess

cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect(("192.168.56.1",7777 ))

cliente.close()
