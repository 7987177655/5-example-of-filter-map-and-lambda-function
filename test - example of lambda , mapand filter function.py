#!/usr/bin/env python
# coding: utf-8

# # 1. Example of Lambda Function : - 

# In[5]:


# 1. addition of two number  by lambda function :- lambda function can take any number of arguments , 
# but can have only have one argument. 

x = lambda a,b : a + b
print("Addition of two number is = " , x(5,5))


# In[11]:


# 2. Addition of user defined number .
x = lambda a,b : a + b
print( " Addition of two number is :" , x(int(input("Enter first number : ")),int(input("Enter Second number : "))))


# In[12]:


# 3.division of two number : - 

y = lambda a,b : a/b
print("division of two number is : " , y(10,2) )


# In[14]:


# 4 . Multiplication of two number 

z = lambda a,b : a*b
print("Multiplication of two number : "  , z(5,5))


# In[24]:


# 5. Addition of three number

a = lambda x,y,z : x+y+z
print("Addition of three number is :" , a(10,5,7))


# # 2 . Example of map function in python 

# In[1]:


# Defination : - The map() executes a specified function for each item in an iterable . 
# the item is sent to the function as paramters .


# In[2]:


# 1. Convert all integer into string
a = [1,3,4,5,6]
b = list(map(str , a))
print(b)


# In[3]:


# 2.convert all integer value into their square . 
a = [1,2,3,4,5,]
def squ(a):
    return a*a
b = list(map(squ , a))
print(b)


# In[6]:


# 3. conver all integer value into their cube by using lambda function
a = [1,2,3,4,5]
b = lambda a : a*a*a
c = list(map (b,a))
print(c)


# In[7]:


# 4 . Return double of number . 

a = [10,20,30,40,50]
b = lambda a : a+a
c = list(map(b,a))
print(c)



# In[11]:


# 5. add two list by using lambda function 

a = [ 2,3,4,5,6,7]
b = [8,9,10,11,12,13]
c = lambda x,y : x + y 
d = list(map(c,a,b))
print(d)


# # 3 . Example of Filter Function in python 

# In[12]:


# Defination : - The filter function returns an iterator where the items are filtered through a function to test ,
# if the item is accepted return True or False .


# In[13]:


# 1.Return adult from given list ages

ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
    return True
adults = list(filter(myFunc, ages))
print(adults)


# In[5]:


# 2. Return even and odd number from given list of number

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
b = lambda a : a%2 != 0
c = list(filter(b,a))
print("odd number is = " , c)
d = lambda a : a%2 == 0
e = list(filter(d,a))
print("even number is = " , e)


# In[7]:


# 3. define a function to check if a number is multiple of three or not .

a = [1,2,3,4,5,6,7,8,9,12,15]
b = lambda x : x % 3 == 0
c = list(filter(b , a ))
print("Number of multiplication of three is " , c )


# In[10]:


# 4 . Remove negative number from the list . 

a = [ 1,2,3,4,-5,-6,-7,-8,-9]
b = lambda x : x >= 0 
c = list(filter(b,a))
print("positive number is : " , c)


# In[12]:


# 4 . Remove positive number from the list . 

a = [ 1,2,3,4,-5,-6,-7,-8,-9]
b = lambda x : x <= 0 
c = list(filter(b,a))
print("Negative number is : " , c)


# In[ ]:




