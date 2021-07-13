import unittest
from natural_language_elements import IntentionExample, Intention


class TestIntentExample(unittest.TestCase):
    def test_example_len(self):
        string_example = 'Doing a teste'
        intent_example = IntentionExample(string_example)
        self.assertEquals(len(string_example), len(intent_example))
        
    def test_intention_empty_creation(self):
        intention = Intention('IntentTest')
        intention.set_intention_examples(['this is an intention example'])
        self.assertEquals(len(intention), 1)
        
if __name__ == '__main__':
    unittest.main()
    