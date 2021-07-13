from .configurations import SmartContactConfiguration

class NlpControler(object):
    def __init__(self, 
                 authorization_key_path:str = None,
                 authorization_key_file:str = None) -> None:
        
        configuration = SmartContactConfiguration(authorization_key_path,authorization_key_file)
        self._authorization_key = configuration.get_authorization_key()
    
    def get_intentions(self) -> None:
        pass
    
    def send_intentions(self) -> None:
        pass
    