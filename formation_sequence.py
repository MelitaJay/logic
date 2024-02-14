
from classes.connective import ConnectiveNegation
from classes.proposition import PropositionAtomic, PropositionNegated, PropositionConnected
from classes.element import Element

class FormationSequence:

    def __init__(self, element: Element):

        self.element = element

        self.store = {
            "foo": []
        }
        self.include_negation = False

    def get(self):

        self.handle_element(self.element)
        self._print_store()

    def handle_element(self, element: Element):
        
        if type(element) == PropositionAtomic:
            self._add_element(element)

        if type(element) == PropositionNegated:
            self.handle_element(element.connective)
            self.handle_element(element.prop_a)

        if type(element) == PropositionConnected:
            self.handle_element(element.prop_a)
            self.handle_element(element.prop_b)
            self._add_element(element)

    def _add_element(self, element: Element):

        if type(element) == PropositionAtomic:
            name = element.name
            number = element.number
            
            if name not in self.store:
                self.store[name] = []

            if number not in self.store[name]:
                # if number > 1:
                #     self._add_element(PropositionAtomic(name, number-1))

                self.store[name].append(number)

        else:
            self.store["foo"].append(element)

    def _print_store(self):

        foo = self.store.pop("foo")

        ret = []

        for key, values in self.store.items():
            values.sort()
            [ret.append(f"{key}{value}") for value in values]

        ret.extend(x.display() for x in foo)

        print(", ".join(ret))


