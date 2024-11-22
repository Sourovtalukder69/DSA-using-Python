### QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card


### SOLUTION

# 1. State the problem clearl, identify the input and output formats.

# problem: we need to write a program to find the position of given number in a list of numbers arranged in decreasing order . We also need to minimize the number of times we acess elements from the list

#Input

    #1.cards: A list of numbers sorted in decreasing order. E.g. [13, 11, 10, 7, 4, 3, 1, 0]
    #2.query: A number, whose position in the array is to be determined. E.g. 7

#Output

    #position: The position of query in the list cards. E.g. 3 in the above case (counting from 0)

def locate_card(card, query):
    pass

# Tips:

    # Name your function appropriately and think carefully about the signature
    # Discuss the problem with the interviewer if you are unsure how to frame it in abstract terms
    # Use descriptive variable names, otherwise you may forget what a variable represents

######################################################################

# # # 2. Come up with some example inputs & outputs. Try to cover all edge cases.

# Before we start implementing our function, it would be useful to come up with some example inputs and outputs which we can use later to test out problem. We'll refer to them as test cases.

# Here's the test case described in the example above.
test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
}

# Our function should be able to handle any set of valid inputs we pass into it. Here's a list of some possible variations we might encounter:

    # 1.The number query occurs somewhere in the middle of the list cards.
    # 2.query is the first element in cards.
    # 3.query is the last element in cards.
    # 4.The list cards contains just one element, which is query.
    # 5.The list cards does not contain number query.
    # 6.The list cards is empty.
    # 7.The list cards contains repeating numbers.
    # 8.The number query occurs at more than one position in cards.
    

    # Edge Cases: It's likely that you didn't think of all of the above cases when you read the problem for the first time. Some of these (like the empty array or query not occurring in cards) are called edge cases, as they represent rare or extreme examples.

# While edge cases may not occur frequently, your programs should be able to handle all edge cases, otherwise they may fail in unexpected ways. Let's create some more test cases for the variations listed above. We'll store all our test cases in an list for easier testing.



# tests = [{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
#  {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
#  {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
#  {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
#  {'input': {'cards': [6], 'query': 6}, 'output': 0},
#  {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
#  {'input': {'cards': [], 'query': 7}, 'output': -1},
#  {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
#   'output': 7},
#  {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
#    'query': 6},
#   'output': 2}]


###############################################################################

# # # 3. Come up with a correct solution for the problem. State it in plain English.

# Our first goal should always be to come up with a correct solution to the problem, which may necessarily be the most efficient solution. The simplest or most obvious solution to a problem, which generally involves checking all possible answers is called the brute force solution.

#In this problem, coming up with a correct solution is quite easy: Bob can simply turn over cards in order one by one, till he find a card with the given number on it. Here's how we might implement it:

    # 1.Create a variable position with the value 0.
    # 2.Check whether the number at index position in card equals query.
    # 3.If it does, position is the answer and can be returned from the function
    # 4.If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
    # 5.If the number was not found, return -1

# Tip: Always try to express (speak or write) the algorithm in your own words before you start coding. It can be as brief or detailed as you require it to be. Writing is a great tool for thinking clearly. It's likely that you will find some parts of the solution difficult to express, which suggests that you are probably unable to think about it clearly. The more clearly you are able to express your thoughts, the easier it will be for you to turn into code.

###############################################################################
#----------------------------------Linear search-----------------------------
# # # 4. Implement the solution and test it using example inputs. Fix bugs, if any.

def locate_card1(cards, query):
    # create a variable position with the value 0
    position = 0
   
    #set up loof for repeatation
    while True:

         # increment the positon
        position += 1
        if cards[position]==query:
            return position
       
        # check if we have reached the end of the array 
        if position ==len(cards):
            # Number not found, return -1

            return -1

test1 = {'input':{'cards':[13, 11, 10, 7, 6, 5, 4, 3, 1, 0],'query':7},'output':3}
result1 = locate_card1(test1['input']['cards'], test1['input']['query'])
print(result1)


############################################################################################
#For Below empty set this above function is not work so we have to modify this function   
# test2 = {'input':{'cards':[], 'query':7}, 'output':-1}
# resutl2 = locate_card(test2['input']['cards'], test2['input']['query'])
# print(resutl2)

def locate_card2(cards, query):
    
    print('cards:', cards) # for understand what is happening
    print('query:', query) # for understand what is happening
    position = 0
    while position<len(cards):
        
        # print('position:', position)
        if cards[position]==query:
            return f"position = {position}"
        position += 1 
        if position ==len(cards):
            return -1
     
test2 = {'input':{'cards':[], 'query':7}, 'output':-1}
resutl2 = locate_card2(test2['input']['cards'], test2['input']['query'])
print(resutl2)

test3 = {'input':{'cards':[9, 5, 4, 3, 2, 1],'query':2}, 'output': 4}
resutl3 = locate_card2(test3['input']['cards'], test3['input']['query'])
print(resutl3)

test4 = {'input':{'cards':[23, 23, 21, 18, 15, 13, 12, 10, 8, -4, -5, -6],'query':-4}, 'output':9}
resutl4 = locate_card2(test4['input']['cards'], test4['input']['query'])
print(resutl4)

test5 = {'input': {'cards': [9, 7, 5, 2, -9],'query': 4},'output': -1}
resutl5 = locate_card2(test5['input']['cards'], test5['input']['query'])
print(resutl5)

test6 = {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],'query': 3 },'output': 7}
result6 = locate_card2(test6['input']['cards'], test6['input']['query'])
print(result6)

test7 = {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],'query': 6},'output': 2}
result7 = locate_card2(test7['input']['cards'], test7['input']['query'])
print(result7)

# # tests = []
# # tests.append(test1, test2, test3)
# # for test in tests:
# #     locate_cards(**tests['input'])
#######################################################################################################
#---------------------------------------- Binary search-----------------------------------
def locate_card3(cards, query):
    lo, hi = 0, len(cards)-1
    while lo<=hi:
        mid = (lo + hi)//2
        mid_number = cards[mid]

        print(f"lo :{lo}, hi :{hi}, mid :{mid}, mid_number :{mid_number}")
        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid-1
        elif mid_number > query:
            lo = mid + 1
    return -1


test3 = {'input':{'cards':[9, 5, 4, 3, 2, 1],'query':2}, 'output': 4}
resutl3 = locate_card3(test3['input']['cards'], test3['input']['query'])
print(resutl3)


#############################################################################################
test7 = {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],'query': 6},'output': 2}
result7 = locate_card3(test7['input']['cards'], test7['input']['query'])
print(result7)
# # This test case in not math with output because reapeted number so we have to modify again
# # #In the case where query occurs multiple times in cards, we'll expect our function to return the first occurrence of query.

# # #While it may also be acceptable for the function to return any position where query occurs within the list, it would be slightly more difficult to test the function, as the output is non-deterministic.

# # # FINAL BINARY SEARCH ALGORITH

def test_location(cards, query, mid):
    mid_number = cards[mid]
    print(f"mid is {mid} and mid_number is {cards[mid]}")
    if mid_number == query:
        if mid >=0 and cards[mid-1]==query:
            return "left"
        else:
            return "found"
    elif mid_number < query:
        return "left"
    else:
        return "Right"
      

def locate_card3(cards, query):
    lo, hi = 0, len(cards)-1
    
    while lo<=hi:
        print(f"lo is {lo} hi is {hi}")
        mid = (lo + hi)//2
        result = test_location(cards, query, mid)
        if result =="found":
            return mid
        elif result == "left":
            hi = mid-1
        elif result == "Right":
            lo = mid + 1
    return -1

test7 = {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],'query': 6},'output': 2}
result7 = locate_card3(test7['input']['cards'], test7['input']['query'])
print(result7)    

#####################################################################################################

# # #Generic Binary Search

#Here is the general strategy behind binary search, which is applicable to a variety of problems:

#     Come up with a condition to determine whether the answer lies before, after or at a given position
#     Retrieve the midpoint and the middle element of the list.
#     If it is the answer, return the middle position as the answer.
#     If answer lies before it, repeat the search with the first half of the list
#     If the answer lies after it, repeat the search with the second half of the list.

# Here is the generic algorithm for binary search, implemented in Python:

def binary_search(lo, hi, condition):
    """TODO - add docs"""
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

# The worst-case complexity or running time of binary search is O(log N), provided the complexity of the condition used to determine whether the answer lies before, after or at a given position is O(1).

# Note that binary_search accepts a function condition as an argument. Python allows passing functions as arguments to other functions, unlike C++ and Java.

# We can now rewrite the locate_card function more succinctly using the binary_search function.

def locate_card(cards, query):
    
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
    
    return binary_search(0, len(cards) - 1, condition)

# Note here that we have defined a function within a function, another handy feature in Python. And the inner function can access the variables within the outer function.


##########################################################################################################
##########################################################################################################
##########################################################################################################

## #Question: Given an array of integers nums sorted in ascending order, find the starting and ending position# of a given number.

# This differs from the problem in only two significant ways:

    # The numbers are sorted in increasing order.
    # We are looking for both the first position and last position 


# Here i have to findout starting and ending position of a a given number which is in a list of ascending order

def st_binary_search(lo, hi, condition):
    while lo<=hi:
        mid = (lo+hi)//2
        result = condition(mid)
        if result == 'back':
            return mid-1
        elif result == 'left':
            hi = mid -1
        elif result == 'right':
            lo = mid + 1
        
    return -1
         

def start_position(cards, target):
    def condition(mid):
        if cards[mid]==target:
            if mid>0 and cards[mid-1]==target:
                return 'left'
            else:
                return 'back'
        elif cards[mid] < target:
            return 'right'
        else:
            return 'left'
    return st_binary_search(0, len(cards)-1, condition)




def end_binary_search(lo, hi, condition):
    while lo<=hi:
        mid = (lo+hi)//2
        result = condition(mid)
        if result == 'found':
            return mid + 1
        elif result == 'right':
            lo = mid + 1
        else:
            hi = mid-1
        
    return -1
         

def end_position(cards, target):
    def condition(mid):
        if cards[mid]==target:
            if mid>0 and cards[mid+1]==target:
                return 'right'
            else:
                return 'found'
        elif cards[mid] < target:
            return 'right'
        else:
            return 'left'
    return end_binary_search(0, len(cards)-1, condition)
   

def st_end_position(cards, target):
    st = start_position(cards, target)
    end = end_position(cards,target)
    print(f"The card numbers :{cards}")
    print(f"the target : {target}")
    print(f"start position : {st}")
    print(f"End position : {end}")
    

# c= [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
c = [1, 2, 3, 4, 5,6, 7, 8, 9]
t = 4

x = st_end_position(c, t)
print(x)
