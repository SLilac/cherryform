#!/usr/bin/python

class FiledError(Exception):
    def __init__(self):
        pass


class Filed:
    
    def __init__(self,label, validators , id = None, description = ""):
        
        self.label = label
        self.validators = validators
        self._data = None

    def validation(self):
        pass = True
        for validator in validators:
            pass = validator(self._data)
            if pass == False:
                rasie raise FiledError(' %s validator failed : %s' % (self.__class__.__name__, self._data))
        
        
        
