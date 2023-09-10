#Goal of this file is to take M3L and GSS and turn it to byte code
import tomllib

def M3L_parser(M3L_file: str):
    '''This fucntion parses through the M3L file that was passed in and creates 
    bytecode that is meant for a renderer.'''
    pass

def GSS_parser(GSS_file: str):
    '''This fucntion parses through the GSS file that was passed in and creates 
    bytecode that is meant for a renderer. Ideally this would happen once per 
    session, but if the user is trying out a new GSS file. I would like for it 
    to happen in the application rather than closing the program and reloading the 
    program'''
    pass