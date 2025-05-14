"""Implement a Stack data structure -- Last In, First Out (LIFO) -- with the following operations: 

push(val): put a value on the top of the stack
pop(val): remove the value from the top of a stack and return it."""

class Stack:
    def __init__(self):
        # Create an empty array to start
        self.myStack = []
    
    def push(self, val):
        """put a value on the top of the stack"""
        # Use the append method on the stack
        self.myStack.append(val)
        pass
    
    def pop(self):
        """remove the value from the top of a stack and return it"""
        # Get the length of the stack
        length = len(self.myStack)
        # remove the last element of the list
        poppedElement = self.myStack[length-1]
        self.myStack.pop()
        return poppedElement
    
    def __repr__(self):
        # Useful for testing
        return str(self.myStack)

newStack = Stack()
newStack.push(4)
newStack.push(5)
newStack.push(6)
# newStack.push(6)
ans = newStack.pop()
# print(ans)

# print(newStack)

"""Implement a Queue data structure -- First In, First Out (FIFO) -- with the following operations: 

enqueue(val): put a value at the end of the queue
dequeue( ): remove the value from the front of the queue and return it."""

class Queue:
    def __init__(self):
        # Define an empty array
        self.myQueue = []
    
    def enqueue(self, val):
        """put a value at the end of the queue"""
        self.myQueue.append(val)
    
    def dequeue(self):
        """remove the value from the front of the queue and return it"""
        
        poppedElement = self.myQueue[0]
        self.myQueue.remove(self.myQueue[0])
        return poppedElement
    
    def __repr__(self):
        return str(self.myQueue)

class PriorityQueue:
    def __init__(self):
        self.myPriorityQueue = []
    
    def enqueue(self, value):
        # Insert a value into the queue based on its cost 
        # If the list is empty, append the value 
        if self.myPriorityQueue == []:
            self.myPriorityQueue.append(value)
        else: 
            # Compare to all current values of the queue
            for qIndex in range( len(self.myPriorityQueue) ):
                # if this node is less than any value of the queue, insert it before that value
                if value.state[1] < self.myPriorityQueue[qIndex].state[1]: # some messy code to access the cost of each node
                    self.myPriorityQueue.insert(qIndex, value)
                    return
            self.myPriorityQueue.append(value)

    def dequeue(self):
        """remove the value from the front of the queue and return it"""
        
        poppedElement = self.myPriorityQueue[0]
        self.myPriorityQueue.remove(self.myPriorityQueue[0])
        return poppedElement
    
    def __repr__(self):
        return str(self.myPriorityQueue)

# myQueueObject = PriorityQueue()
# myQueueObject.enqueue(0)
# myQueueObject.enqueue(3)
# myQueueObject.enqueue(5)
# myQueueObject.enqueue(1)
# print(myQueueObject)