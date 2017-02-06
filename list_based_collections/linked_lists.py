class Element(object):
    def __init__(self, data):
        self.data = data

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """Adds element to the end of the list"""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element


    def get_position(self, position):
        """Get an element from a particular position.
        Return "None" if position is not in the list."""
        counter = 0
        current = self.head
        if position < 0:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None


    def insert(self, new_element, position):
        """Insert a new node at the given position."""
        counter = 0
        current = self.head
        if position == 0:
            new_element.next = self.head
            self.head = new_element
        elif position > 0:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1


    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
