#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        """The value must be a string."""
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")
      
    def is_sentence(self):
        return self.value.endswith('.')
        
    def is_question(self):
        return self.value.endswith('?')
        
    def is_exclamation(self):
        return self.value.endswith('!')
        
    def count_sentences(self):
        standardized_value = self.value.replace('!', '.').replace('?', '.').split('.')
        sentences = [sentence.strip() for sentence in standardized_value if sentence]
        return len(sentences)  
    

