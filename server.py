#!/usr/bin/env python
import socket

def main():

    ipAddr = "192.168.0.101"
    portNum = 80
    bufferSize = 2048
    message = "Can I give you an html file?"
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ipAddr, portNum))
    s.listen(0)

    sc, address = s.accept()
    print address
    sc.send(message)
    sc.close()
    s.close()

if __name__ == "__main__":
    main()
