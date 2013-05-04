#1/usr/bin/python

from fileds import Filed

class MetaForm(type):

    def __new__(cls, classname, basecalss, classdict):
    
        self.__fileds__ = bassclass.__fileds__
        [ self.__fileds__.append(filed) if type(filed) is Filed for filed in classname.__dict__]
        


class Form(meataclass = MetaForm)
    
    def __init__(sefl)
