# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 15:49:19 2017

@author: TahsinVT
"""

import socket

def Main():
    host = '127.0.0.1'
    port = 5000
    
    mysocket = socket.socket()
    mysocket.connect((host,port))
    
    message = input(" -> ")
    
    while message !='q'