class LinkedList:
    class Node:
        def __init__(self, value):
            self.next = None
            self.value = value
            
        def setNext(self, node):
            self.next = node            
    
    def __init__(self):
        self.head = None
        
    def add(self, value):
        if not self.head:
            self.head = LinkedList.Node(value)
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
            
        last_node.next = LinkedList.Node(value)
        
    # Added for Q1.
    def delete(self, value_to_delete):
        if not self.head:
            return False

        # deletion at head
        if self.head.value == value_to_delete:
            self.head = self.head.next
            return True
                
        # deletion for a non-head node
        prev_node = None
        next_node = self.head

        while next_node: # there is more than one node
            if next_node.value == value_to_delete:
                prev_node.next = next_node.next
                return True
            prev_node = next_node
            next_node = next_node.next
        return False
    
    def to_string(self):
        return ", ".join([str(i) for i in self.to_list()])
    
    def to_list(self):
        if not self.head:
            return None
        
        values = []
        next_node = self.head
        while next_node:
            values.append(next_node.value)
            next_node = next_node.next
        return values
