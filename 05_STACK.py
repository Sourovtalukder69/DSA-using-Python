# What is stack ?
# Stack is a simple data structure.
#    Example : In mess plate put on down to up. 1st put place is down last put place is up.
#              and any body will take last place as fisrt plate

# Its use a pricipal call (LIFO)
# stack can created by Array. or by Linked List
# Main functionality push and pop



#          |-----------------|      <----- Top | Push (insertign item) 
#          |        4        |                 | Pop  (removing item)
#          |-----------------|                 | peak (top item)
#          |        3        |                 | is empty (check empty or not)
#          |-----------------|                 | size (how much item )     
#          |        2        | 
#          |-----------------|                 
#          |________1________|   
#                Stack            

# That means stack is basically linked list in where all operation will occur in head. dont touch tail


########## Stack implementation using Linked list ########

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):  # creating an empty linked list
        self.top = None
        self.n = 0

    def isempty(self):
        return self.top == None
        

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def peak(self):
        if (self.isempty()):
            return print("stack Empty")
        else:
            return self.top.data
    # def pop(self):
    #     if self.top is None:
    #         return "stack is empty"
    #     else:
    #         data = self.top.data
    #         self.top = self.top.next
    #         return data
    # Created by me  
    def pop(self):
        if self.top == None:
            return 'Empty Stack'
        else:
            pop_item = self.top.data
            self.top = self.top.next
            self.n = self.n-1
        return pop_item
        

    def traverse(self):
        curr = self.top
        while curr != None:
            print(curr.data, end=' ')
            curr = curr.next
    def size(self):
        curr = self.top
        count = 0
        while curr != None:
            curr = curr.next
            count = count + 1
        return print(count)
    ############### Problem 1 ###########  
    def reverse_string(self,string):
        s = Stack()
        for i in string:
            s.push(i)

        res = ""
        while (not s.isempty()):
            res = res + s.pop()
        print(res)


    ############## Problem 2 ########### 
    # text editor undo redo

    def text_editor(self, text, pattern):
        u = Stack()
        r = Stack()
        for i in text:
            u.push(i)
        for i in pattern:
            if i=='u':
                data = u.pop()
                r.push(data)
            else:
                data = r.pop()
                u.push(data)
        res = ''
        while (not u.isempty()):
            res = u.pop() + res
        print(res)

    # I created undo redo
        # Undo redo in stack operation

    def undo_redo(self, string, ur):
        s1 = Stack()
        s2 = Stack()
        for i in  string:
            s1.push(i)
        for j in ur:
            if j == 'u':
                s2.push(s1.pop())
            else:
                 s1.push(s2.pop())
    
        return s1.show()
    
    def show(self):
        curr = self.top
        s3 = Stack()
        while curr != None:
            s3.push(curr.data)
            curr = curr.next
        return s3.traverse()


    

    

    ##############  Problem 4 #########
    # celebrety problem :briliant problem
    #     A B C D      
    # A [ 0 0 1 1 ]
    # B [ 0 0 1 1 ]
    # C [ 1 0 0 1 ]
    # D [ 0 0 0 0 ]
    
    # Here celebrety is this who dont know anybody but everybody know him. Here D is clebrety . Output = 3


    l = [
        [0,0,1,1],
        [0,0,1,0],
        [0,0,0,0],
        [0,0,1,0]
    ]
    def find_the_cleb(l):
        s = Stack() 
        for i in range(len(L)):
            s.push(i)

        while s.size() >= 2:
            i = s.pop()
            j = s.pop()
            if l[i][j] == 0:
                # j is not celebrety
                s.push(i)
            else:
                # i is not celebrety
                s.push(j)
            
        celeb = s.pop()
        for i in range(len(l)):
            if i != celeb:
                if l[i][celeb] == 0 or l[celeb][i] == l:
                    print("No one is celebrety")
                    return 
        print("the celebrety is ", celeb)

        
        

L = Stack()

L.text_editor('ABCDE', 'uurru')


################ stack questions################
# Q1. String reversal
# Q2. Text editor
# Q3. Balanced parantheses   - click on video nitesh stacklast
# Q4. celebrety Problem



#########################################################################

############ Stack implementation using Array  ############


class stack:

    def __init__(self, size): # size would be fixed (array impltn)
        self.size = size
        self.__stack = [None] * self.size
        self.top = -1
        
    def push(self, value):
        if self.top == self.size - 1:
            return "overflow"
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            return "empty"
        else:
            data = self.stack[self.top]
            self.top = self.top - 1
            print(data)
    def traverse(self):
        for i in range(self.top + 1):
            print(self.stack[i], end=' ')

s = stack(3)
