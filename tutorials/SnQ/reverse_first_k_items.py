# Provided base classes: Node, LinkedList, Stack, Queue
# (Same classes as Question 1 - include them here)
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

class Queue:
    def __init__(self):
        self.ll = LinkedList()
        
    def enqueue(self, data):    
        self.ll.insertNode(data, self.ll.size)
        
    def dequeue(self):
        if self.isEmpty():
            return None
        data = self.ll.head.data    
        self.ll.removeNode(0)
        return data
        
    def getFront(self):
        if self.isEmpty():
            raise IndexError("Peek from empty queue")
        return self.ll.head.data    
        
    def getSize(self):          
        return self.ll.size
        
    def isEmpty(self):
        return self.ll.size == 0
    
    def printQueue(self):
        self.ll.printList()


def reverse_first_k_items(queue, k):
    #reverse first k elements of queue using a stack
    #dequeue and enqueue first length-k
    #dequeue k
    #push into stack
    #pop stack
    #enqueue back into queue

    helper_stack = Stack()

    length = queue.getSize()
    for i in range(k):
        helper_stack.push(queue.dequeue())
    for i in range(k):
        queue.enqueue(helper_stack.pop())
    for i in range(length-k):
        queue.enqueue(queue.dequeue())
    return queue



if __name__ == "__main__":
    q = Queue()
    
    while True:
        print("Please input your choice (1/2/0): ", end="")
        choice = input()
        
        if choice == '1':
            print("Input an integer that you want to insert into the queue: ", end="")
            num = int(input())
            q.enqueue(num)
            print("The resulting queue is:", end=" ")
            q.printQueue()
        elif choice == '2':
            if q.isEmpty():
                print("Queue is empty. Cannot reverse.")
                continue
            print("Enter an integer to reverse the queue until that number: ", end="")
            k = int(input())
            if k > q.getSize() or k < 0:
                print(f"Invalid k value. k must be between 0 and {q.getSize()}.")
                continue
            reverse_first_k_items(q, k)
            print(f"The resulting queue after reversing first {k} elements is:", end=" ")
            q.printQueue()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")