#1/usr/bin/python

from fileds import Filed

class MetaForm(type):

    def __new__(cls, classname, basecalss, classdict):
    
        self.__fileds__ = bassclass.__fileds
        [ self.__fileds__.append(filed) if type(filed) is Filed for filed in classname.__dict__]
        


class Form(meataclass = MetaForm)
    self.__name__ = Form.__class__.name
    def __init__(sefl)
