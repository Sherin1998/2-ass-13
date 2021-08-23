#!/usr/bin/env python
# coding: utf-8

# #1
# 
# def rep(x):
#     y=x[-2:5:-1]
#     z=x[:4]+x[-1:3:-1]+x[3:-1]
#     return y,z
# 
# rep('SherinShaji')
# 
# When positive and negative indexing are used simultaneously,it is necessary to give step size.Failing to do so results in a blank string.Using negative numbers as indices causes indexing to start from end.

# In[10]:


#2
a=[100 for i in range(1001)]

List comprehension can be used.


# In[15]:


#3

Use step size to indicate the pattern of slicing

l=['first','second','third','fourth','fifth','sixth','seventh','eighth','nineth','tenth','eleventh']
l[::2]


# #4
# 
# Indexing ==> The process of accessing each element in an iterable using index values.Index value always starts from 0 and end at no. of elements-1.Negative indices indicate accessingfrom end.Indexing returns single elements
# 
# Slicing ==> Slicing is a feature in python that enables us to get a subset of a sequence like string or list.It returns sequence of element in the iterable.It requires start index,end index,step size.
# Syntax :  seq_name[start:end:step]

# In[16]:


#5
l=['first','second','third','fourth','fifth','sixth','seventh','eighth','nineth','tenth','eleventh']
l[1000]


Index Error occurs as the index is not available.


# In[11]:


#6

l=['hen','greshsj','poiiyg','henht']
l.sort()
for i in l:
    if(i[0]=='h'):
        print(i)
    
    


# #7
#     In an assignment problem,whenever the number of sources is not equal to the number of destinations ie no of rows is not equal to number of columns, the assignment problem is called an unbalanced assignment problem and the matrix is called unbalanced matrix.Inorder to make it balanced,dummy rows are added to make it square matrix.It contains elements as 0s.This is done because row reduction can only be done on square matrix.

# #8
# Matrix memory allocation requires loops to provide space.Using nested for loops can iterate over allocating memory .List comprehension reduce the line of code.
