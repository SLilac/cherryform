
class ValidationError(Exception):
    pass

class Email:
    pass

class Password:
    pass

class Require:
    pass

class Url:
    pass

def max(length = 15):
    
    def _max(form, filed):
        if length > len(filed.data):
            raise ValidationError(message)
    return _max
