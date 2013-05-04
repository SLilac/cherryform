#!/usr/bin/python

class FiledError(Exception):
    def __init__(self):
        pass


class Filed:
    
    def __init__(self,label, validators , id = None, description = "",
            name = "", required = True, default = None, from = None, errors ):
        
        self.label = label
        self.validators = validators if type(validators) is list else [validators]
        self.data = None
        self.type = None
        self.errors = errors if type(errors) is list else [error]
        self.default = default

    def validate(self):
        pass_ed = True
        for validator in validators:
            pass_ed = validator(self.data)
            if pass_ed == False:
                raise FiledError(' %s validator failed : %s' % (self.__class__.__name__, self._data))
    
    
    def __call__(self):
        return "<input name='%s' id ='%s' type=''> %s</input>"
    
        
        
