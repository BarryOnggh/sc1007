class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def findNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
        if self.head is None:
            raise ValueError("List is empty")
            
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur
        
    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid position")
            
        new_node = Node(data)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True
        
        prev_node = self.findNode(index - 1)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1
        return True
    
    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

def moveMinNode(head):
    #create list of even
    #scan through list to find even
    #if even, push to back of the list

    list_of_even = []

    current = head

    while current:
        if current.data%2==0:
            list_of_even.append(current.data)
    
    #if element in list
    #move to back
    #

    current = head
    prev = None
    node_back = head

    for i in list_of_even:
        while current:
            node_back = head
            node_to_continue = current.next
            if i == current.data:
                prev.next = current.next
                while node_back:
                    node_back = node_back.next
                node_back.next = current
            else:
                prev = current
            current = node_to_continue
    
    return head




if __name__ == "__main__":
    linked_list = LinkedList()
    
    # A simpler way to get input for testing
    input_string = input("Enter a list of numbers separated by spaces: ")
    numbers = input_string.split()
    
    for num_str in numbers:
        try:
            num = int(num_str)
            # Always insert at the end to maintain order
            linked_list.insertNode(num, linked_list.size)
        except ValueError:
            print(f"'{num_str}' is not a valid integer. Skipping.")
    
    print("\nBefore:", end=" ")
    linked_list.printList()
    
    # Call the function and update the list's head with the returned new head
    linked_list.head = moveMinNode(linked_list.head)
    
    print("After: ", end=" ")
    linked_list.printList()