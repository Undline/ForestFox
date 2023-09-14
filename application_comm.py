import socket
from typing import Dict

# The goal with this module is to allow inter communication between the UI render and 
# the application that callled on it. This is all local to the machine...

def connect_application():
    '''This is called whenever a new application is attempting to connect. This is 
    being done in order to prevent an unknown application from attempting to overide 
    the render'''
    pass

def is_approved_app(app_name: str) -> bool:
    '''This searches through the approved application list and returns if the app that
    is attempting to connect has been approved previously'''
    return True

def show_state() -> Dict[str, str]:
    '''This returns the current state of the UI in a dictionary format.  This is done
    so that a controlling application can keep in sync with what the current enviroment 
    is showing'''
    pass