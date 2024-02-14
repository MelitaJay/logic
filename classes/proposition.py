import abc
from classes.connective import ConnectiveNegation, Connective
from classes.element import Element

class Proposition(Element):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name:str=None):
        self.name = name

    def display(self):
        return f"{self.name}"
    
    @abc.abstractproperty
    def brackets_count(self):
        pass

class PropositionAtomic(Proposition):

    def __init__(self, name:str, number:int=None):
        super().__init__(name)
        self.number = number

    def display(self):
        return f"{self.name}{self.number}"
    
    @property
    def brackets_count(self):
        return 0
    

class PropositionConnected(Proposition):

    def __init__(self, prop_a:Proposition, prop_b:Proposition, connective:Connective):

        super().__init__("")
        self.prop_a = prop_a
        self.prop_b = prop_b
        self.connective = connective

    def display(self):
        return f"({self.prop_a.display()} {self.connective.symbol} {self.prop_b.display()})"
    
    @property
    def brackets_count(self):
        return (
            self.prop_a.brackets_count
            + self.prop_b.brackets_count
            + 2
        )

class PropositionNegated(Proposition):

    def __init__(self, prop_a:Proposition):

        super().__init__("")
        self.prop_a = prop_a
        self.connective = ConnectiveNegation()

    def display(self):
        return f"({self.prop_a.display()} {self.connective.symbol} {self.prop_b.display()})"
    
    @property
    def brackets_count(self):
        return (
            self.prop_a.brackets_count
            + 2
        )
