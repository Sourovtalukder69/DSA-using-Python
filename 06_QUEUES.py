# What is Queues ?
# Queues is a linear data structure. Its follow the principal of FIFO(first in first out). insertion(enqueue) always occur from tail(rear) and deletion(dequeue) always ocuur from head(front).
# 
#   example : ticket cut for bus line by line

# implementation use a linked list

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queues:
    def __init__(self):
        self.front = None
        self.rear = None
        self.n = 0
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.n = self.n + 1

    def dqueue(self):
        if self.front == None:
            return "Empty queues"
        else:
            self.front = self.front.next

    def isempty(self):
        return self.front == None
    
    def size(self):
        curr = self.front
        count = 0
        while curr != None:
            count = count + 1
            curr = curr.next
        return count
    
    def front_item(self):
        if self.front == None:
            return "Empy"
        else:
            return self.front.data
        
    def rare_item(self):
        if self.rear == None:
            return "Empy"
        else:
            return self.rear.data
        




    def traverse(self):
        temp = self.front
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next

q = Queues()
q.enqueue(4)
q.enqueue(5)

q.traverse()

                              


#######  Creating a queues by using two stack  #######




# problem
def fun(num):
    if (num == 0):
        return 0
    else:
        Queues.enqueue(num%10)
        res = fun[num//10]
        res = res*10 + Queues.dqueue()
        return res
print(fun[123])
