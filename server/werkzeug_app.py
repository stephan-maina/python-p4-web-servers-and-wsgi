#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

# Define a route handling function
def application(environ, start_response):
    # This is the request handling component.
    # It receives incoming HTTP requests.
    request = Request(environ)

    # Log the remote address of the client making the request.
    print(f'This web server is running at {request.remote_addr}')

    # This is where you might perform application-specific logic.
    # For now, it just generates a simple response.
    response = Response('A WSGI generated this response!')

    # This is the response handling component.
    # It generates and sends HTTP responses back to the client.
    return response(environ, start_response)

if __name__ == '__main__':
    # This part configures and runs the web server.
    
    # The 'run_simple' function is part of Werkzeug and serves as the web server component.
    run_simple(
        hostname='localhost',  # This specifies the server's hostname.
        port=5555,             # This specifies the port number to listen on.
        application=application  # This specifies the WSGI application to run.
    )
