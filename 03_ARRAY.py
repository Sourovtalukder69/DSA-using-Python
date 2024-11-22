# What is array ?
# Array is a linear data structure which is use to store multiple items of same type in continuous memory location.
# continuous memory loacation means [  2 |  4 |  5  |  6 ]
#                        M location    701  705   707   713
#   exm: store marks of 100 student
#   Best use : Read, traverse, index  Compexcity=O(1)
#     


# # # Disadvantage of array :
#1.Fixed size(Memory waste). static array

#   To overcome this problem we have to change it fixed size to dynamic size 
#   * Dynamic Array : it adjuct by requrement not need to adjuct first
      
#     1  [1]          size-1
#     2  [1, 2]       size-2
#     3  [1, 2, 3, _] size--4
#     4  [1, 2, 3, 4] size-4
#     5  [1 ,2, 3, 4, 5, _, _, _]  size-8
#     6  [1, 2, 3, 4, 5, 6, _, _]  size-8
#     now it will increase 8 8 8 times
#     This concept is called dynamic array:
#     Dynamic array is not actually exist. its a concept,  a way to make static array 
#     Python list internally dynamic array




#2.Homogeneous -->  You can only store one type data like, integer, float, str......
#                     lack of flaxibility
#   To overcome this problem to make hectogeneous(means store different type of data ) use 
#   Refencial arrays

#   A normal array A=[1    2     3     4    5]
#                   1000   1004  1008  1012 1016       : call by array

#   Feferencial array A = [1     2     hi    4    5]  : it store data different type of memory loc
#                          201   301    401  502   605   : call by array reference
#       examle : Python builtin list
#       problem: space need hi, and work some slowly
#       easily create an website, app . But to create game time issue happen


# Now we will create our own class which will actually behave like python list. using dynamic array concept. and use c array
# by create list[D], len[D], append[D], print(), indexing, pop, clear, find, insert, delet, remove
# import ctypes  # A foreign function  library for python

import ctypes
# to create C type ka array
     

class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C type ka array with size -> self.size
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def append(self,item):
        # check if vacant
        if self.n == self.size:
            # array is full -> resize
            self.__resize(self.size*2)

        self.A[self.n] = item
        self.n = self.n + 1
    
    # def pop(self):
    #     if self.n != 0:
    #         self.A = self.A[:-1]
    #         return self.A
    #     else:
    #         return  'not in list'
    def pop(self):
        if self.n == 0:
            return 'Empty List'
        print(self.A[self.n-1])
        self.n = self.n - 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'ValueError - not in list'

    def insert(self,pos,item):
        
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n = self.n + 1

    def remove(self,item):
        # search and get pos
        pos = self.find(item)
        if type(pos) == int:
            # delete
            self.__delitem__(pos)
        else:
            return pos
        
    def replace(self, pos, item):
        if 0<= pos <self.n:
            self.A[pos] = item

    def sort(self):
        for i in range(self.n -1):
            for j in range(self.n -1 -i):
                if self.A[j]> self.A[j+1]:
                    self.A[j], self.A[j+1] = self.A[j+1], self.A[j]
        print(self.A)
    
    def min(self):
        ar = self.sort()
        return L[0]
    def max(self):
        arr = self.sort()
        return arr[self.n-1]
    
    def sum(self):
        total = 0
        for i in range(self.n):
            total = total + self.A[i]
        return total
    def extand(self, arr):
        for i in arr:
            self.append(i)
        return self.__str__()

    def __resize(self,new_capacity):
        # create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content of old array to new one
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B

    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return '[' + result[:-1] + ']'

    def __getitem__(self,index):

        if 0<= index < self.n:
            return self.A[index]
        else:
            return 'IndexError'

    def __delitem__(self,pos):
        # delete pos wala item
        if 0<= pos < self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]

        self.n = self.n - 1

    def __make_array(self,capacity):
        # referential array(C type)
        return (capacity*ctypes.py_object)()
     

L = MeraList()
     

L.append(1)
L.append('hello')
L.append(False)
L.append(4.5)
print(L)
    
L.remove(4.5)
L = [10,20,30]


# You try to solve : adding 
# sort(), min(), max, sum, extand, slicing, indexing, mergee






















