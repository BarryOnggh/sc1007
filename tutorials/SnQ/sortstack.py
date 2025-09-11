# Provided base classes: Node, LinkedList, Stack
# (Same Node, LinkedList, Stack classes as Question 1 - include them here)
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

    def removeNode(self, index):
        if self.head is None:
            raise ValueError("List is empty")
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
            
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
            
        pre = self.findNode(index - 1)
        if pre.next is not None:
            pre.next = pre.next.next
            self.size -= 1
            return True
        return False
        
    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print("")

class Stack:
    def __init__(self):
        self.ll = LinkedList()
        
    def push(self, data):    
        self.ll.insertNode(data, 0)
        
    def pop(self):
        if self.isEmpty():
            return None
        data = self.ll.head.data    
        self.ll.removeNode(0)
        return data
        
    def peek(self):
        if self.isEmpty():
            return None
        return self.ll.head.data    
        
    def isEmpty(self):
        return self.ll.size == 0
        
    def getSize(self):
        return self.ll.size
        
    def printStack(self):
        self.ll.printList()

# Function to sort a stack in ascending order [cite: 47]
def sort_stack(stack):
    # TODO: Write your code here
    # 1. Create a temporary stack.
    # 2. While the input stack is not empty, pop an element `tmp`.
    # 3. While the temporary stack is not empty and its top element is greater than `tmp`,
    #    pop from the temporary stack and push it back to the input stack.
    # 4. Push `tmp` to the temporary stack.
    # 5. After the main loop, the temporary stack is sorted. Move all elements back to the original stack.
    pass

# Main program execution
if __name__ == "__main__":
    s = Stack()
    
    while True:
        print("Please input your choice (1/2/0): ", end="")
        choice = input()
        
        if choice == '1':
            print("Input an integer that you want to insert into the stack: ", end="")
            num = int(input())
            s.push(num)
            print("The resulting stack is:", end=" ")
            s.printStack()
        elif choice == '2':
            sort_stack(s)
            print("The resulting stack after sorting it in ascending order is:", end=" ")
            s.printStack()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")