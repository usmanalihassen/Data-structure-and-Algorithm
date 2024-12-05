# Node class to represent each element
class Node:
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.next = None  # Pointer to the next node

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # Head of the linked list

    # Method to add a node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node

    # Method to display the linked list
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.display()
#leet code
def two_sum(nums, target):
    # Dictionary to store the index of numbers we have seen
    seen = {}
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        # Check if the complement exists in the dictionary
        if complement in seen:
            return [seen[complement], i]
        # Store the current number and its index in the dictionary
        seen[num] = i

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Indices:", result)

