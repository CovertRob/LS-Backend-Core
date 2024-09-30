class CustomSet:

    def __init__(self, list_of_elements=None) -> None:
        if list_of_elements is None:
            self.elements = []
        else:
            self.elements = []
            for item in list_of_elements:
                if not item in self.elements:
                    self.elements.append(item)
                

    def is_empty(self):
        return (len(self.elements) == 0)

    def contains(self, element):
        return element in self.elements

    def is_subset(self, other_set):
        return all([other_set.contains(element) for element in self.elements])

    def is_disjoint(self, other_set):
        return self.intersection(other_set).is_empty()

    def is_same(self, other_set):
        if self.is_empty() and not other_set.is_empty():
            return False
        return self.is_subset(other_set)

    def __eq__(self, other_set) -> bool:
        return self.is_same(other_set)

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def intersection(self, other_set):
        return CustomSet([element for element in self.elements if other_set.contains(element)])

    def difference(self, other_set):
        return CustomSet([element for element in self.elements if not other_set.contains(element)])

    def union(self, other_set):
        return CustomSet(self.elements + other_set.elements)

    def __str__(self) -> str:
        return str(self.elements)
    
