"""
Singly  
                   Elemento   Próximo
HEAD[4800] -> Node   [10]     [4900]  -> Node [20][5000] -> Node [7][null]


Doubly

HEAD -> Node <-> Node <-> Node
   null <-


Operação                                    Singly  Doubly
Acesso a um elemento                        O(n)    O(n)
Adicionar/remover posição do iterador       O(1)    O(1)
Adicionar/remover primeiro elemento         O(1)    O(1)
Adicionar último elemento                   O(1)    O(1)
Remover último elemento                     O(n)    O(1)
"""

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
        if self.head == Node:
            return 0

        current_node = self.head

        total = 0

        while current_node:
            current_node = current_node.next
            total += 1

        return total

    def to_list(self):
        node_data = []
        current_node = self.head

        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next

        return node_data
    
    def display(self):

        node = self.head

        if node is None:
            print("Linked List empty.")
        
        while node:
           print(node.data)
           node = node.next
        print("-" * 8)
    
    def get(self, index):

        if index >= self.length() or index < 0:
            print("Error: Index out of range")
            return None

        current_idx = 0
        current_node = self.head

        while current_node != None:
            if current_idx == index:
                return current_node.data
            current_node = current_node.next
            current_idx += 1

    def reverse(self):
        
        previous_node = None
        current_node = self.head

        while current_node != None:
            current_node.next, previous_node, current_node = previous_node, current_node, current_node.next
        self.head = previous_node
    
    def search(self, data):
        
        if self.head == None:
            print("Error: Empty list")
            return None

        current_node = self.head

        while current_node != None:
            if current_node.data == data:
                print("Item found.")
                return 
            current_node = current_node.next
        else:
            print("Item not found.")
        
    
    def remove_first_item(self):
        
        if self.head == None:
            print("Error: Empty list")
            return None

        self.head = self.head.next
    
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
            print("Error: Empty list")
            return None

        if data == self.head.data:
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
            print("Item not found.")
         
    def insert_by_index(self, index, data):

        if index >= self.length() or index < 0:
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