import socket
from typing import Dict

# The goal with this module is to allow inter communication between the UI render and 
# the application that called on it. This is all local to the machine...

def connect_application():
    '''This is called whenever a new application is attempting to connect. This is 
    being done in order to prevent an unknown application from attempting to override 
    the render'''

    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the IP and port
    server_socket.bind(('127.0.0.1', 12345))

    print("Listening for UI request(s)")

    while True:
        data, sender_address = server_socket.recvfrom(1024)
        message = data.decode()
        print(f"Received message from {sender_address}: {message}")

        if message.lower() == "@quit":
            break

    server_socket.close()
    pass

def interpret_message(message: str):
    '''This function should take in the message that is being received by the external 
    application and interpret what handler to send that message to'''
    pass

def is_approved_app(app_name: str) -> bool:
    '''This searches through the approved application list and returns if the app that
    is attempting to connect has been approved previously'''
    return True

def show_state() -> Dict[str, str]:
    '''This returns the current state of the UI in a dictionary format.  This is done
    so that a controlling application can keep in sync with what the current environment 
    is showing'''
    pass