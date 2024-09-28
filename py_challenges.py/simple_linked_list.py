'''
1. Two classes: SimpleLinkedList and Element
    - Element: constructor takes one argument and optional next argument
2. Element methods
  - datum property
  - is_tail method
  - next property
3. SimpleLinkedList methods
    - size property
    - is_empty method
    - push method
    - peek method
    - head property
    - pop method
    - from_list class method
    - to_list method
    - reverse method
'''
class Element:

    def __init__(self, data, next=None) -> None:
        self.datum = data
        self.next = next

    #returns the elements data
    @property
    def datum(self):
        return self._datum

    @datum.setter
    def datum(self, value):
        self._datum = value

    def is_tail(self):
        return not bool(self.next)
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, element):
        self._next = element

class SimpleLinkedList:

    def __init__(self) -> None:
        self.head = None # will reset this at first push

    @property
    def size(self):
        counter = 0
        next_element = self.head
        while next_element:
            counter += 1
            next_element = next_element.next
        return counter

    @property
    def head(self) -> Element:
        return self._head

    @head.setter
    def head(self, element):
        self._head = element

    @classmethod
    def from_list(cls, lst=None):
        if lst is None:
            lst = []
        linked_list = cls()
        for datum in reversed(lst):
            linked_list.push(datum)
        return linked_list
    
    def to_list(self):
        lst = []
        current_elem = self.head
        while current_elem:
            lst.append(current_elem.datum)
            current_elem = current_elem.next
        return lst

    def is_empty(self):
        return not bool(self.size)

    def push(self, data):
        new_element = Element(data, self.head)
        self.head = new_element

    def pop(self):
        pop_item = self.head
        if pop_item:
            self.head = pop_item.next
        return pop_item.datum

    def peek(self):
        return self.head.datum if self.head else None

    def reverse(self):
        reversed_list = SimpleLinkedList()
        current_elem = self.head
        while current_elem:
            reversed_list.push(current_elem.datum)
            current_elem = current_elem.next
        return reversed_list

        



