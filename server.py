#!/usr/bin/env python
import BaseHTTPServer, cgi
import signal
import sys
from time import gmtime, strftime
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

        #Uses the static IP 192.168.0.101 because my RaspPi has a DCHP reservation for that address on our router
        html = """
            <html>
                <head>
                    <title>Ryan's Doorbell</title>
                </head>
                <body>
                    <p>Press this button to alert Ryan that his presence is requested in the living room.</p>
                    <button id='but1'>This is the button</button><br><br>
                    <textarea id="message" style="min-width: 400px; min-height: 100px;" placeholder="Leave blank or enter a message for Ryan here ..."></textarea>

                    <script src='http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js'></script>
                    <script type='text/javascript'>
                        $('#but1').click(function(){
                            $.ajax({
                                url:'http://192.168.0.101:8000/server.py',
                                type:'POST',
                                data: {
                                    message: $("#message").val().trim() || "Get thineself into the living area quarters"
                                }
                            });
                            alert('Ryan has been notified');
                        });
                    </script>
                </body>
            </html>
        """
        s.wfile.write(html)

    def do_POST(s):
        # Retrieve the POST parameters
        ctype, pdict = cgi.parse_header(s.headers.getheader('content-type'))
        length = int(s.headers.getheader('content-length'))
        postVars = cgi.parse_qs(s.rfile.read(length), keep_blank_values=1)

        message = postVars["message"][0]
        print "[" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "] " + message

        blink()


def startServer():
    server_address = ('', 8000)
    server = BaseHTTPServer.HTTPServer(server_address, DoorBellHandler)
    server.serve_forever()


def signal_handler(signal, frame):
    shutDown()
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    setup()
    startServer()

if __name__ == "__main__":
    main()
