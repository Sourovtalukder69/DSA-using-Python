# Why is Hashing ?
# Hashing is fast searching.
#      1.linear search = O(n)
#      2.Binary search = O(log n)
#      3.  Hashing     =O(1) 


### Hashing concept is : finding value by index
# array of 1000 item :L = [1 2 3 4 5 6......  ]
# Q. L[150] = ?   process: 1st address + 150 * 4(if integer) 

# so what we will do? 
# Ans : we store our data into index position
# like : array = [. . . . .]      data = {3 5 2 1 5}
#         index=  0 1 2 3 4 

#   finally  array = [1 2 3 4 5]

# But problem in this case that if data = {0 1 3 1000} 
# i have to create a array of 1000 space . but it is lots of waste of memory


# The main concept of hashing is hashing function
#           A = [. . . . . . . . . . ]    size 10
#         index  0 1 2 3 4 5 6 7 8 9 

# store data = {11, 22, 33, 44, 55, 66, 77, 88, 99, 100}
# how will i store this data of array into index position?
# index:(each item)%size
#              (11)%10 = 1   that mean this will store in index 1
#              (44)%10 = 4   that mean this will store in index 4
#             (100)%10 = 0   that mean this will store in index 0

# Finally  A = [100, 11, 22, 33, 44, 55, 66, 11, 88, 99]
# search 101 in this array.
# process 101% size(10) = 1 
# but index 1 != 101 -Does not exist



### Another concept
#         B = [    .       .        .    ]  size=3

#       index      0       1       2        
# store data = { cat   dog    rat}
# how will i store this data of array A  into index position?
# index:
#         for cat [as(c) + as(a) + as(t)] % size
#                   99   +  97   +  116 = 312
#                   312%3 = 0(index)

#         for dog [as(d) + as(o) + as(g)]
#                   100  +   111 + 103 = 313
#                    314 % 3 = 2(index)

#         for rat [as(r)+ as(a) + as(t)]
#                   47  + 116   + 114  = 226
#                        226 % 3 = 2(index) but already dog in index 2 how can store it 
#                         But this is colllision

# Finally B = [ cat    rat    dog ]



#Collision :
#     C = [  .  .  .  .  .  ]          # size = 5 ; h(i) = i%5
#     index 0   1  2  3  4  

# store data = {32, 41, 37, 24, 16}
# here 32%5 =index(2) ; 41%5 = index(1); 37%5 = again index(2) (This is collision)
#      C = [  . 41 32 .  .  ]
#    index=   1  2  3 



#### To solve this collision 
#    1. Closed adressing technique (chaining) : store item in same index [use linked list]
#    2. Open adressing technique  : store item where space is empty
#         i.Linear probing
#         ii.Quadratic probing


"####"# Closed Adressing technique  : In this technique array element is not integer or string they are node
#         Array = [  .  .  .  .  .]    size = 5 ;  Hashing func:h(i) = i%5
#        index  =    0  1  2  3  4

# store data = {31, 47, 16, 21, 36}
#    h(31) = index(1) ; h(47) = index(2) ; h(16) = again index(1) 
# So to solve this problem we have to use node . so we use linked list such that we can store data in same index where already a data exist(node data) which next is None, and i put the item in None point like linkedlist

#                         16
# None(N)                  N   N                       
#            Array = [  . 31  47   .  ]     size= 5
#           index =     0  1  2  3  4  
#                          |
#                         [16]->[21]->[36]->None


# But problem in this approach in a particular index there are joining a alot of item thats mean again its searching is linear type. so we also have to fix this problem 
###### There are two ways to solve this problem 

#     1. Rehashing (loadfactor). when loadfactor cros i increase array size
#     
#                         16
# None(N                   N   N                       
#            Array = [  . 31  47   .  ]    size= 5
#           index =     0  1  2  3  4  
#                          |
#                         [16]->[21]->[36]->None  
# load facotor crossed so i will  increase size

#           Array = [  .  .  .  .  .  .  .  .  ]    size= 8    Hash func h(i) = i%8
#               index  0  1  2  3  4  5  6  7


#       (value index set by hash)      index=  0  1  2  3  4  5  6  7
#      H(37) = 37 % 8 = index(5)  | Array = [  .  .  .  .  . 37  .  .  ]
#      H(42) = 42 % 8 = index(2)  | Array = [  .  . 42  .  . 37  .  .  ]
#      H(67) = 67 % 8 = index(3)  | Array = [  .  . 42  67 . 37  .  .  ]
#      H(22) = 22 % 8 = index(6)  | Array = [  .  . 42  67 . 37  22 .  ]
#      H(57) = 57 % 8 = index(1)  | Array = [  . 57 42  67 . 37  22 .  ]

#  Finally : Array = [  . 57 42  67 . 37  22 .  ]    convert O(1)

#     2. Balance tree . time complexity(log(n))


"#######"# Open addressing technique
#       1.Linear probing . (array size >= no of item)
#       g(i) = [h(i) + k(i`)] % size  <-(Hashing function of L.P)
# where h(i) = i%size ;     k(i`) = i`;      i`= 0(for first time hashing)
#                                            i`=1, 2, 3, 4 (for space finding)

# Problem in this approach so manny space is empty
# So to fix this problem there another technique called Quadratic probing
#       2.Quadratic probing 
#       g(i) = [h(i) + k(i`)] % size   <-(Hashing function of Q.P) 
# where h(i) = i%size ;     k(i`) = i`* i`    
# 


########## Hashing Implementation #######


### Linear probing
class Dictionary:
    def __init__(self, size):
        self.size = size
        self.slots = [None]*self.size    # For keys 
        self.data = [None]*self.size     # For values

    def put(self, key, value):
        hash_value = self.hash_function(key)
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:

            if self.slots[hash_value] == key:
                self.data[hash_value] = value
            else:
                new_hash_value = self.rehash(hash_value)
                while self.slots[new_hash_value] != None and self.slots[new_hash_value] != key:
                    new_hash_value = self.rehash(new_hash_value)
                if self.slots[new_hash_value] == None:
                    self.slots[new_hash_value] = key
                    self.data[new_hash_value] = value
                else:
                    self.data[new_hash_value] = value
    
    def rehash(self, old_hash):
        return (old_hash + 1) % self.size
     
    def hash_function(self, key):  # Python has a default hash() function whih can calculate hash value of any types of imutable data(int, str, float, tuple)
        return abs(hash(key)) % self.size   # abs for absolute(non negetive) number
    
    
    

