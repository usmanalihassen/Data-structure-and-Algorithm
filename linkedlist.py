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
#example
class Node:
    def __init__(self, data):
        self.data = data  # Initialize the data of the node
        self.next = None  # Set the next node to None initially

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list

    def append(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:      # If the list is empty, set the head to the new node
            self.head = new_node
            return
        last = self.head       # Start from the head node
        while last.next:       # Traverse to the end of the list
            last = last.next
        last.next = new_node   # Link the last node to the new node

    def display(self):
        current = self.head  # Start from the head node
        while current:
            print(current.data, end=" -> ")  # Print the data in the current node
            current = current.next           # Move to the next node
        print("None")  # End of the list

    def delete(self, key):
        current = self.head

        # If the node to be deleted is the head
        if current and current.data == key:
            self.head = current.next  # Change the head
            current = None  # Remove the old head
            return

        # Find the node to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not found in the list
        if current is None:
            print("Node with data", key, "not found.")
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None  # Free memory

# Example usage:
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()  # Output: 10 -> 20 -> 30 -> None

ll.delete(20)
ll.display()  # Output: 10 -> 30 -> None
