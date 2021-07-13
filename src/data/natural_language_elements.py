class Intention(object):
    def __init__(self, name:str):
        self.name = name
        self.id = None
        self.count_questions = None
        self.health_score = None
        self.storage_date = None
        self.examples = []
    
    def set_intention_examples(self, examples):
        if isinstance(examples, list):
            if examples:
                self.__validate_if_examples_list_is_not_empty(examples)
            else:
                raise Exception('Examples list is empty!')

    def __validate_if_examples_list_is_not_empty(self, examples):
        if isinstance(examples[0], IntentionExample):
            self.examples = examples
        elif isinstance(examples[0], str):
            self.examples = [IntentionExample(i) for i in examples]
    
    def generate_json(self):
        pass
            
    def __len__(self):
        return len(self.examples)
        
class IntentionExample(object):
    def __init__(self, text:str):
        self.text = text
        
    def __len__(self):
        return len(self.text)