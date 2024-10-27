# Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Initialize next as null (no next node)

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head of list

    # Adding node to end
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty, new node is head
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse to end of list
            last = last.next
        last.next = new_node  # Point last node to new node

    # Printing list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of list

# Using LinkedList
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

ll.display()  # Output: 10 -> 20 -> 30 -> None
