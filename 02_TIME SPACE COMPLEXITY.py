# Alogorithmic complexcity : There are two types of  complexcity
#    1.Time complexcity     [example:(search anything in google it gives ans in some seconds)]
#    2.Space complexcity    [example: facebook vs facebooklite] 

# some important info
# 1024 kb = 1mb
# 1024 mb = 1gb


#################################### TIME COMPLEXCITY ###############################
# # # Target : make a relation between time and input
# # # Techniques to measure time efficiency
#       1.MEasuring time to execute
#       2.counting operations involved
#       3.Abstract notion of order of growth


##########################################################################################
### 1.Measurign time :
 
# work different time for different algorithms
# This approach is not use because it depend on device power.
# lets suppose measure time for printing 100 numbers

# using for loop
import time
start_f = time.time()
for i in range(1, 100):
    print(i)
For = time.time()-start_f

# using while loop
import time
start_w = time.time()
i = 0
while i<=100:
    print(i)
    i += 1
# see how much time needed this two program 
print(For)
print(time.time()-start_w)


###########################################################################################
### 2. Counting operations :

def c_to_f(c):
    return c*9.0/5 + 32    # 3 operation in this function

def mysum(x):
    total = 0  # 1 operation   
    for i in range(x+1): # 1 operation
        total += i       # 2 operation
    return total

# conclussion is for mysum function  (1 + 3X)
# relationship : T = 1+3X  (X=inputs)
#  that means 1 operation in outside , 3 operation in loop
# if x = 10, operation= (1+3x10)=31


##################################################################################################
### 3.Order of growth
# What do we want 
#     1.we want to evalute the algorithm
#     2.we want to evaluate scalability
#     3.we want to evalute in terms of input size

# Different inputs changes how the program runs
# a function that searches for an element in a list 
def search_for_elmnt(l, e):
    for i in l:
        if i==e:
            return True
    return False

# when (e) is first element in the list = Best case 
# when e is not in list = worst case
# when look through about half of the elements in list = Average case


# order of grouth is most important to measure time complexcity because it gives efficient answer

# # # ORDER OF GROWTH 
#    1.want to evalute programs efficiency when input is very big
#    2.want to express the growth of programs run time as input size grows (rltn time and input)
#    3.want to put a upper bound on growth - as tight as possible
#    4.do not need to be precise :"order of " not "exact" growth
#    5.we will look at largest factors in run time (wich section of the program will take the longest to run) 
#    example : there is a single loop and aslo there is a nested loop we will look on nested loop
# 


###  MESURING ORDER OF GROUTH : BIG OH NOTATION
# Big oh notation measures an upper bound on the asymptotic growth , often called order of growth
# Big oh on O() is used to descrive worst case 
#   > worst case occurs often and is the bottleneck when a program runs
#   > express rete of growth of program relative to the input size
#   > evalute algorithms Not machine or implementation


# look at below program
def fact_iter(n):
    # assumes n an int >=0
    answer = 1 # 1 operation outside loo[]
    
    while n>1:             # 1 operation
        answer =answer * n # 2 operation   
        n = n-1            # 2 operation
    return answer

# Equation : 1 + 5n
# To calculate O()  cut all freedom items -- here cut 1 then
# Equation :0 + 5n
# also cut all multiplicated constant -- here cut 5
# Equation : n
# Ans : O(n) = means linear   T|/__n
# according to Big oh notation time complexicity of this program is order of n



# Calculate Big oh notaion of below equations

#  1.n*2 + 2n + 2  :  | =n*2 + 2n  | =n*2 + n | Ans :O(n*2)
#     here--> n*2 =nested loop,    2n=  2 opetation inside the loop

#  2. n*2 + 1000n + 3*1000  :  | =n*2 + 1000n | =n*2 + n | Ans : O(n*2)

#  3. log(n) + n + 4   : | =log(n)+ n |  Ans: O(n)    # because n>log(n)

#  4. 0.0001*n*log(n) + 300n :  | Ans :O(nlog(n))

#  5. 2n*30 + 3*n   :  |Ans : O(3*n)




# 1.For constant grap : O(1)   t|__i    
#  Exmple :
#         A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,.............. 1000]
#         A[100] = 75      t second
#         A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,.............. 2000] << double array
#         A[100] = 75      t second
#         doesnt depend on len(array)  time = constant


# 2.For logarithmic)  : O(log n)   t|__i      : input X 10x = time X 1x, i X 20x = t X 2x 
#                   input = multiplying, time = adding  
#   Example : Binary search


# 3.For linear graph : O(n)   t|__input
#  Example : linear search

# 4.For nlog(n) : O(nlogn)   t|__i
#  Example : Sorting alogorith, merge sort, quic sort 


# 5.For quadratic : O(n*2)   t|__input       :2i =4t, 4i=8t
#  Example : nested loop


# 6.For  exponential : O(2*n)   t|__i 
#   Example : 

# exponential , quadratic, nlogn, linear, constant,  logarithmic, 



# ------------|-------------|-------------|--------------|--------------|
#  CLASS      |    N=10     |  =100       |     =1000    |   =1000000   |
#-------------|-------------|-------------|--------------|--------------|
#    O(1)     |      1      |     1       |      1       |      1       |
#             |             |             |              |              |
#-------------|-------------|-------------|--------------|--------------|
#  O(log n)   |     1       |     2       |      3       |      6       |
#             |             |             |              |              |
#-------------|-------------|-------------|--------------|--------------|
#   O(n)      |     10      |   100       |     1000     |  1000000     |
#             |             |             |              |              |
#-------------|-------------|-------------|--------------|--------------|
#  O(nlog n)  |     10      |   200       |     3000     |     6000000  |
#             |             |             |              |              |
#-------------|-------------|-------------|--------------|--------------|
#  O(n*2)     |    100      |   10000     |   1000000    | 1000000000000|
#             |             |             |              |              |
#-------------|-------------|-------------|--------------|--------------|
#  O(2*N)     |    1024     |             |              |              |
#             |             |             |              |              |
#---------------------------|-------------|--------------|--------------|


# # # Examples of Measuring Time Complexity

# Q1.
l = [1, 2, 3, 4, 5]
sum = 0
for i in l:
    sum = sum+i
print(sum)
product = 1
for i in l:
    product = product*i
print(sum)

# Time complexicity = O(n) + O(n) = O(2n) = O(n).



# Q2.
l = [1, 2, 3, 4, 5]
for i in l:
    for j in l:
        print(f'{i}, {j}')


# Time complexcity  : O(n) * O(n) =O(n*2) ."quadratic" |)__


# Q3.linear search : Time coplexcity =   O(n) .  "linear"|/__ 


# Q4.5 
def inttosrt(i):
    digits = '0123456789'
    if i ==0:
        return "0"
    result = ''
    while i>0:
        result = digits[i%10] + result
        i = i//10
    print(result)
inttosrt(123)      # [123%10] =3, [567%100] = [67]

# Time complexity : Here input :  123,  1230,  12300,  123000
#                   loop running:  3,     4,      5,      6
#                   that means  O() = log(n)
# Specially when dividing it will log case



# Q6.





# Q7.Binary search  : time complexity : log(n)

# Q8.
l = [1, 2, 3, 4, 5]
for i in range(0, len(l)):
    for j in range(i+1, len(l)):
        print(f"{i}, {j}")

# Time complexcity : O(n) * O(n-1) = O(n*2 - 1) = O(n*2). "quadratic"

# Qj9:
A = [1, 2, 3, 4]
B = [2, 3, 4, 5, 6]
for i in A:
    for j in B:
        if i<j:
           print(f"{i}, {j}")

# Here time complexity is not O(n*2) because O(n*2) heppen  both loop iterate same time but here its turnign 4 times for A and 5 times for B. so the time complexcity is :O(ab)




# Q10.
A = [1, 2, 3, 4]
B = [1, 2, 3, 4]
for i in A:
    for j in B:
        for k in range(100000):
            print(f"{i}", {j})


# Time Complexity: O(n) * O(n) * O(1) = O(n*2) "quadratic"
# here last loop is constant

#Q11.
l = [1, 2, 3, 4, 5]


for i in range(0, len(l)//2):
    other = len(l)-i -1
    temp = l[i]
    l[i] = l[other]
    l[other] = temp
     
print(l)

# Time complexity : O(n/2) = O(n)


# Q12.recurstion 

def factorial(n):
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

# Time complecity:input :  5, 10, 100
#                  f call :5 , 10, 100
# that means time complecity order of n :O(n) "linear"


# Q13.Recursion
def fib(n):
    if n==1 or n==0:
        return 1
    else:
        return fib(n-1) + fib(n-2) 

print(fib(5))   

# Time complexcity : input = 1, 2, 4, 5, 6
#                    f call= 1, 2, 4, 14, 32
# so the time complexity is : exponential(dangerous):O(2*n)  :<(2*n) :(1.7*n)




# Q14. Recursion
def power(num):
    if num<1:
        return 0
    elif num==1:
        return 1
    else:
        prev = power(num//2)
        curr = prev*2
        print(curr)
        return curr
    
power(145)

# Time complexcity : input 10, 100, 1000
#                   f call 4,  8, 12

# that means  O()= log(n)'''


# Q.15
def mod(a,b):
    if b<=0:
        return -1
    div = a//b
    return a - div*b

print(mod(5, 3))

# Time complexicity : Arithmetic operation always O() = O(1) "constant"



# Q.16.
def sum_digits(num):
    sum = 0
    while(num>0):
        sum = sum + num%10
        num = num//10
    return sum

# Time complexcity : O(log(n))

# Q.17.
# T(n) = {3T(n-1) if n>0)}
#        {1,    otherwise}
# Time complecity =  n(3)= tsec, n(4)=3tsec, n(5)=9t, n(6)=27tsec
# so the time complexicity is exponential :O(2*n) : 



##########
# My own creation fibonacci series

def fibonacci(n, amount):
    x = [] 
    pre = n-1
    ans = pre + n
    x.append(ans)
    # now starting actual fibonacci
    while len(x)<amount:
        result = n + ans
        n = ans
        ans = result
        x.append(result)

    return x           
print(fibonacci(2, 10)) # output[3, 5, 8, 13, 21, 34, 55, 89, 144, 233]