import json

class SmartContactConfiguration(object):
    
    def __init__(self, 
                 authorization_key_path: str = None) -> None:

        if _authorization_key_path:
            self._authorization_key = self._read_key_from_file(authorization_key_path)

    def _read_key_from_file(self, authorization_key_path: str = None) -> str:
        if not authorization_key_path:
            raise Exception('Key not passed as argument.')
        try:
            with open(authorization_key_path) as data:
                self.bot_key = json.load(data)
        except FileNotFoundError:
            print('Cannot read the key file.')