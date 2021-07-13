import os
import json


class SmartContactConfiguration(object):
    
    def __init__(self, 
                 authorization_key_path: str = None, 
                 authorization_key_file: str = None) -> None:
        """
        """
        self._read_key_from_json_file(os.path.join(authorization_key_path, authorization_key_file))

    def _read_key_from_json_file(self, authorization_key_file: str = None) -> str:
        """
        Reads bot key from json file
        
        Parameter:
        - authorization_key_file (str): path of authorization file
        """
        
        if not authorization_key_file:
            raise Exception('Key not passed as argument.')
        try:
            with open(authorization_key_file) as data:
                self._authorization_key = json.load(data)['authorization_key']
        except FileNotFoundError:
            print('Cannot read the key file.')
            
    def get_authorization_key(self) -> str:
        """
        Returns authorization key
        """
        
        return self._authorization_key
    