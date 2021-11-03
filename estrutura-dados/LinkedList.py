class Node:

    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def append(self, data):

        node = Node(data)

        if self.head == None:
            self.head = node
            return
        
        current_node = self.head

        while current_node.next:
             current_node = current_node.next

        current_node.next = node
        return
    
    def length(self):

        if self.head == None:
            return 0

        total = 0
        current_node = self.head

        while current_node != None:
            current_node = current_node.next
            total += 1

        return total

    def to_list(self):
    
        lista = []
        current_node = self.head

        while current_node != None:
            lista.append(current_node.data)
            current_node = current_node.next
            
        
        return lista
    
    def display(self):

        current_node = self.head

        if current_node is None:
            print("Error: Empty Linked List.")

        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

    def get_value(self, index):

        if index > self.length() or index < 0:
            print("Error: Index out of range.")

        current_node = self.head
        current_idx = 0

        while current_node != None:
            if current_idx == index:
                    return current_node.data
            
            current_node = current_node.next
            current_idx += 1
    
    def get_index(self, data):

        if data == self.head.data:
            return 0

        current_node = self.head
        current_idx = 0

        while current_node != None:
            if data == current_node.data:
                return current_idx
            
            current_node = current_node.next
            current_idx += 1
        
        else:
            print("Error: Item not found.")

    def reverse(self):

        previous_node = None
        current_node = self.head

        while current_node != None:
            previous_node, current_node, current_node.next = current_node, current_node.next, previous_node
        
        self.head = previous_node
    
    def search(self, data):

        if self.length() == 0:
            print("Error: Empty Linked List.")
            return None
        
        current_node = self.head

        while current_node != None:
            if current_node.data == data:
                print("Item found.")
                return 
        else:
            print("Error: Item not found.")

    def remove_first_item(self):

        if self.head == None:
            print("Error: Empty Linked List.")

        current_node = self.head
        self.head = current_node.next

    def remove_last_item(self):

        self.reverse()
        self.remove_first_item()
        self.reverse()

    def add_first_item(self, data):

        node = Node(data)

        node.next = self.head
        self.head = node
    
    def add_last_item(self, data):

        self.reverse()
        self.add_first_item(data)
        self.reverse()

    def remove_by_value(self, data):

        if self.head == None:
            print("Error: Empty Linked List.")
            return None

        if self.data == data:
            self.remove_first_item()
            return

        current_node = self.head

        while current_node != None:
            previous_node = current_node
            current_node = current_node.next

            if current_node.data == data:
                previous_node.next = current_node.next
                return 
        else:
            print("Error: Item not found.")

    def insert_by_index(self, index, data):
        
        if index > self.length() or index < 0:
            print("Error: Index out of range")
            return None
        
        if index == 0:
            self.add_first_item(data)
            return

        current_node = self.head
        current_idx = 0
        node = Node(data)

        while current_node != None:
            previous_node = current_node
            current_node = current_node.next

            if current_idx == (index - 1):
                previous_node.next = node
                node.next = current_node
                return

            current_idx += 1

    def remove_by_index(self, index):

        if index > self.length() or index < 0:
            print("Error: Index out of range")
        
        if index == 0:
            self.remove_first_item()
            return
        
        current_node = self.head
        current_idx = 0

        while current_node != None:
            previous_node = current_node
            current_node = current_node.next

            if current_idx == index:
                previous_node.next = current_node.next
                return

            current_idx += 1

        else:
            print("Error: Item not found.")