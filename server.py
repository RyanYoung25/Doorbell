#!/usr/bin/env python
import BaseHTTPServer
from blinkLights import *


class DoorBellHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Ryan's Doorbell</title></head><body>")
        s.wfile.write("<p>Press this button to alert Ryan that his presence is requested in the living room.</p><button id='but1'>This is the button</button>")
        #Adding jquery
        s.wfile.write("<script src='http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js'></script>")
        #Adding java scirpt for button press
        #Uses the static IP 192.168.0.101 because my RaspPi has a DCHP reservation for that address on our router
        s.wfile.write("<script type='text/javascript'>$('#but1').click(function(){ $.ajax({url:'http://192.168.0.101:8000/server.py', type:'POST'}); alert('Ryan Has been notified');}); </script>")
        s.wfile.write("</body></html>")

    def do_POST(s):
        blink()


def startServer():
    server_address = ('', 8000)
    server = BaseHTTPServer.HTTPServer(server_address, DoorBellHandler)
    server.serve_forever()


def main():
    setup()
    startServer()

if __name__ == "__main__":
    main()
