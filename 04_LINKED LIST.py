# what is  Linked List ?
#   Linked list is  a linear Data Structure which is use to store data in non continuous memory location.[replacement of array]. you can create more data structure using linked list. like(stacks, queues,).
#   Best use : Write Heavy operations, insert, delet
#   linked list read operation(searching) take time . but in array use A[5000] like that search index through so array dont take time.

###############################################################################################


# How does it works ?
#   It is the collection of nodes. Nodes is basiacally this structure where i can store 2 things (data, address). Node=[data, address]
#    data = current data
#    address= next node adress
#    first node is 'Head'
#    last node is 'Tail' which address point 'Null'
#    

#   example :  [ 2 |613] , [ 3 |707],   [ 4 |905],    [ 5 |Null]    <-- Linked list
#                 501         613         707           905

#                                      Object
#         Data(int, str, float)                        Adress(memory loc[500, 900]
#                                                      [d | a] - - - [ | 900]  
#                                                         500         700          
#                                                      [d | 700]
#                                                                     [  |  ]
#                                                                      900


###################################################################################

# Why i should not use array, i will use linked list ?
#    In array when is insert, delet, i had to shift items its call(right operation)
#    In array right operation time complexity O(n) means |/__ linear,for this time waste
#    But in linked list right operation time complexity  O(1) constant.
#    And linked list dont waste memory 
# we will create node

###################################################################################

# There are 4 main operations in linked list
#     1.Insert : Head,   Tail(append),   Middle(insert)

#     2.Traverse : (print)

#     3.Delet :  Head,   Tail(pop),   value(remove), index()

#     4.Search :(value, index)

#     some times :reverse, max min, 


###################################################################################


# Here we create a menual linked list  (create indivisuals node and connect them to form a linked list)
# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None

# a = Node(1)
# b = Node(2)
# c = Node(3)
# print(a.data)
# print(b.data)
# a.next = b
# b.next = c
# print(a.next)
# print(b.next)



################################################################################

# # # There are 4 main operations in linked list
#     1.Insert :(Head, Tail(append), Middle(insert))

#     2.Traverse : (print)

#     3.Delet :(Head, Tail(pop), value(remove), index())

#     4.Search :(value, index)

#     some times :reverse, max min, 



# # #CORE Linked list
# Create :Node[D], a LL[D], len, insert from head, traverse/print, insert from  tail(append), insert in middle(after), clear, delete from head, delete from tail(pop), delet by value (remove), search by value(find), search by index -> del L(0), search by index(indexing)
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        # create empty linked list (Head=None)
        self.head = None
        self.n = 0     # count how much node in linked list

    # insert from Head
    def insert_head(self, value):
        # new node
        new_node = Node(value)
        # create connection
        new_node.next = self.head
        # reassign head
        self.head = new_node
        # increment n
        self.n = self.n + 1
    
    # traversing 

    # def traverse(self):

    #     curr = self.head
    #     while curr!=None:
    #         print(curr.data)
    #         curr = curr.next

    def __str__(self):
        curr = self.head
        
        result = ''
        while curr != None:
            result = result + str(curr.data) + "->"
            curr = curr.next
        return result[:-2]
    

    # insert from tail :
    # traverse to the last node (tail) and set the next of tail to new
    #   [1]        [2]         [3]            [4]              None
    #                 current.next.next   curr.next!=None      curr!=None
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n = self.n+1
            return 
       
        curr = self.head
        while curr.next != None:
            curr = curr.next
            # you are at the last node 
        curr.next = new_node
        self.n = self.n + 1


    # inset in middle(my try)
    # def insert_after(self, pos, value):
    #     new_node = Node(value)
    #     curr = self.head
    #     while curr != None:
    #         if curr.data == pos:
    #             curr.next == new_node
    #             new_node.next = curr.next
    
    def insert_after(self, after, value):
        new_node = Node(value)

        curr = self.head
        while curr!=None:
            if curr.data == after:
                break
            curr = curr.next

        # case 1 break - item peyegesi  curr -> Not nun
        if curr !=None:
            # logic
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            return 'Item not found'
        # case 2 loop pura colse - item not exist - curr -> None

    
    #############################################################################
    # deleting linked list
    # clear linked list
    def clear(self):
        self.head = None
        self.n = 0
     
    # delet from  head linked list(my try)
    # def delet_head(self):
    #     curr = self.head
    #     self.head = None
    #     self.head = curr.next
    #     self.n = self.n -1
    def del_head(self):
        if self.head == None:
            return "Empty List"

        self.head = self.head.next
        self.n = self.n - 1

    
    # delet from tail (linked list)
    def pop(self):

        if self.head == None:
            return 'None'
    
        curr = self.head
        # is the linked list have one item
        if curr.next == None:
            # it will delet from head
            return self.delet_head()

        while curr.next.next !=None:
            curr = curr.next
        
        # curr is the second last
        curr.next = None
        self.n = self.n - 1

    # delet from middle() linked list
    def remove(self, value):
        if self.head == None:
            return "Empty list"

        if self.head == value: 
            return self.del_head() # Not working
        curr = self.head

        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next

        # case ! item found
        if curr.next == None:
            return "not found"
        else:
            curr.next = curr.next.next
            self.n = self.n - 1

    ###################################################################
    # searching in linked list 

    # search by value
    def search(self, item):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == item:
                return pos
        
            curr = curr.next
            pos = pos + 1
        
        return "not found"
    
    # search by indexing
    def __getitem__(self, index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos + 1
    def search_index(self,index):
        count = 0
        curr = self.head
        while curr != None:
            if count == index:
                break
            curr = curr.next
            count = count + 1
        if curr != None:
            return curr.data
        else:
            return 'IndexError'
    
    # Find max value repalce by given value
    def all_value(self):
        arr = []
        curr = self.head
        while curr != None:
            arr.append(curr.data)
            curr = curr.next
        return arr
    def max_value(self):
        arr = self.all_value()
        max_sorted = self.selection_sort(arr)
        max = max_sorted[0]
        return max
        
    def max_replace(self, item):
        max_value = self.max_value()
        curr = self.head
        while curr != None:
            if curr.data == max_value:
                break
            curr = curr.next

        if curr != None:
            curr.data = item
        else:
            return 'Empty'
            

            
            


    def selection_sort(self, arr):
        for i in range(len(arr)-1):
            min = i
            for j in range(i+i, len(arr)):
                if arr[j]>arr[min]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
        return arr


    ########## Problem 2 #########
    # find max value and replace by given value
    def replace_max(self, value):
        temp = self.head
        max = temp
        while temp != None:
            if temp.data > max.data:
                max = temp
            temp = temp.next
        max.data = value

    ########## problem 3#######
    #### find odd number and sum them 
    def odd_sum(self):
        result = 0
        curr = self.head
        while curr != None:
            if curr.data %2 ==1:
                result = result + curr.data
            curr = curr.next

        return result
    
    ######## Problem 4 ######
    ### Reverse linked list (without creating new) do inplace reversal
    def reverse(self):
        prev_node = None
        curr_node = self.head
        
        while curr_node!= None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        self.head = prev_node

    ################ Problem 5 #############
    def del_duplicate(self):
        curr = self.head
        while curr != None:
            if curr.data == curr.next.data:
                curr.data = curr.next.data
                curr.next = curr.next.next
                
            curr = curr.next


            

#5.Write a python program to remove all duplicate elements from a sorted linked list containing integer data
#Example:
# Input LinkedList: 10 10 20 20 30 30 30 40 50
# Output LinkedList: 10 20 30 40 50

    
L = LinkedList()

L.append(10)
L.append(10)
L.append(20)
L.append(20)
L.append(30)
L.append(30)
L.append(30)
L.append(40)
L.append(40)
L.del_duplicate()

print(L)


##################### Problem on linked list ##########

### Q1.What is the output of following function when head node of following linked list is passed as input
# 1->2->3->4->5

def fun(head):
    if (head==None):
        return
    if head.next.next != None:
        print(head.data,"", end='')
        fun(head.next)
    print(head.data,"",end='')

# ans = 1 2 3 4 3 2 1



### Q2. Write a python program to find the maximum  value in a linked list and replace it with a given value:

# Assume that the linked list containing whole numbers and there is only one maximum value in linked list

# def replace_max(self, value):
#         temp = self.head
#         max = temp
#         while temp != None:
#             if temp.data > max.data:
#                 max = temp
#             temp = temp.next
#         max.data = value




# Q3. Given a linked list containing whole numbers. Write a python function which finds and return s teh sum of all teh elements at dd position in the given linked list.


# def odd_sum(self):
#     result = 0
#     curr = self.head
#     while curr != None:
#         if curr.data %2 ==1:
#             result = result + curr.data
#         curr = curr.next

#     return result



### Q4.Write a python program to reverse a linked list containg integer data
# def reverse(self):
#     prev_node = None
#     curr_node = self.head
        
#     while curr_node!= None:
#         next_node = curr_node.next
#         curr_node.next = prev_node
#         prev_node = curr_node
#         curr_node = next_node
        
#     self.head = prev_node




#4.Given a linked list of characters.Write a python function to return a new string that is created by" 
# #appending all the characters given in the linked list as per the rules given below.
#Rules->
#Replace '*' or '/'by a single space
#In case of two consecutive occurrences of '*' or'/',replace those two occurrences by a single space and
# convert the next character to upper case
#Assume that->
#There will not be more than two consecutive occurrences of or/
#The linked list will always end with an alphabet
#Sample Input
# A,n,*,/,a,p,l,e,*,*,k,e,e,p,s,/,*,a,/,/,d,o,c,t,o,r,*,A,w,a,y

#Expected Output
#"An Apple a day Keeps A Doctor Away






#5.Write a python program to remove all duplicate elements from a sorted linked list containing integer data
#Example:
# Input LinkedList: 10 10 20 20 30 30 30 40 50
# Output LinkedList: 10 20 30 40 50