#!/usr/bin/env python
# coding: utf-8

# ## Session 3: Assignment 1
# 1.1 Write a Python Program to implement your own myreduce() function which works exactly
# like Python's built-in function reduce()
# 1.2 Write a Python program to implement your own myfilter() function which works exactly like
# Python's built-in function filter()
# 2. Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
# 3. Implement a function longestWord() that takes a list of words and returns the longest one.

# In[18]:


#1.1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()

#define a function like reduce() which take first two values from list and do operation with next
def myreduce(list1):
    j=2
    i = len(list1)
    temp = list1[0]+list1[1]
    while(j < i):
        temp = temp +list1[j]
        j +=1
    print("Sum of total values in the list: %d" %temp)
      
    
#calling function with passing values from list

my_list=[10,10,16]
myreduce(my_list)


# In[22]:


#1.2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()

#define a function which will filter out the numbers divisible by 7.
def myfilter(num):
    even_num =[]
    for i in num:
        if i%7== 0:
            even_num.append(i)
    print(even_num)
    
#call the function with passing values from a list        
l=[1,14, 21, 34, 49, 23, 28, 35, 76, 70]
myfilter(l)


# In[94]:


## 2. Implement List comprehensions to produce the following lists.
#Write List comprehensions to produce the following Lists
#------------------------------------------------------------------------
#['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
l= 'ACADGILD'
alphabet_list = [ alphabet for alphabet in l ] 
print ("List1 : " + str(alphabet_list)) 

#------------------------------------------------------------------------

#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
l2 = ['x','y','z'] 
result = [ item*num for item in l2 for num in range(1,5)  ] 
print("List2 :" +   str(result)) 

#------------------------------------------------------------------------

#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']

l3 = ['x','y','z'] 
result1 = [ item*num for num in range(1,5) for item in l3  ] 
print("List3 : " +   str(result1)) 


#------------------------------------------------------------------------
#[[2], [3], [4], [3], [4], [5], [4], [5], [6]]

l4 = [2,3,4] 
result = [ [item+num] for item in l4 for num in range(0,3)] 
print("List5 :" +  str(result)) 

#------------------------------------------------------------------------
#[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
l5 = [2,3,4,5] 
result = [ [item+num for item in l5] for num in range(0,4)  ] 
print("List6 :" +  str(result)) 


#------------------------------------------------------------------------
#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

input_list=[1,2,3] 
result = [ (b,a) for a in input_list for b in input_list]
print("List7 : " +  str(result)) 



# In[101]:


#3. Implement a function longestWord() that takes a list of words and returns the longest one.

from functools import reduce 
#initialise the list
words_list= ["January","Feburary","March","April","May","June","July"]
#define a function
def longestWord(list_words):
    return reduce( (lambda x,y:y if len(y) > len(x) else x), list_words ) 

print ('Longest word in the list : %s'  %longestWord(words_list) ) 

