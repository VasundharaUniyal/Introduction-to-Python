#!/usr/bin/env python
# coding: utf-8

# In[92]:


import this


# ## Python  Introduction

# In[ ]:


# print function


# In[428]:


print("hello world") # String 
print('hello world')


# In[ ]:


# why did we use double quotes?
#To join one or more characters we can use double quotes.


# ### Data Types
# 
# 1.String: Immutable
# 
# Collection of character inside "Double quotes" or 'Single quotes'
# 
# You can use 'single quotes' inside "double quotes"
# 
# or
# 
# "Double quotes" inside 'single quotes
# 
# 
# 2.List: Mutable
# 
# Is a datas tructure that can hold any type of data
# 
# ordered collection of items.
# 
# You can strore anything in lists int,float,string
# 
# 3.Tuples: Immutable
# Tuples can store any type of data.
# 
# example=('one','two',three')
# 
# no append,no insert,no pop,no remove.
# 
# We use tuple when we are aware that our data is not going to change.
# 
# eg: days=('monday','tuesday')
# 
# Tuples are faster than lists
# 
# 4.Set : Unordered collection of unique items.
# 
# eg: s={1,2,3,2}

# In[288]:


print("hello 'world' world")


# In[6]:


print('hello "world" world')


# We cannot use 'single quote' inside 'single quote'

# In[7]:


print('hello 'world' world')

# error 


# In[9]:


print('I'm Dhara')
# error - cant't perform this function also.


# We cannot use 'double quote' inside 'double quote'

# In[13]:


print("Hello "world" world")
# error - cnat't perfom this function also.


# # List : Can mix words and numbers in list

# In[103]:


number = [1,2,3,4]
print(number)


# In[107]:


number = [1,2,3,4]
print(number[1])


# In[111]:


words=['word1','word2','word3']
print(words)


# In[110]:


words=['word1','word2','word3']
print(words[:1])


# In[106]:


mixed=[1,2,3,4,'five','six',2,3,None]
print(mixed)


# In[112]:


mixed=[1,2,3,4,'five','six',2,3,None]
print(mixed[-1])


# In[113]:


mixed[1]='two'
print(mixed)


# In[114]:


# How to add item in our list 
fruits=['grapes','apple']
fruits.append('mango')
print(fruits)


# In[115]:


fruits=[]
fruits.append('mango')
fruits.append('grapes')
print(fruits)


# In[ ]:


# Some more methods to add data in our list
# Insert method
# How to join concat 2 list
# extend method
# Difference between append and extend method


# ## Insert Method

# In[116]:


fruits=['grapes','apple']
fruits.insert(1,'orange')
print(fruits)


# In[117]:


fruits=['grapes','apple']
fruits.insert(20,'orange')
print(fruits)


# ## How to join concat 2 list

# In[118]:


fruits1=['grapes','apple']
fruits2=['mango','orange']
fruits = fruits1 + fruits2
print(fruits)


# ## Extend Method

# In[120]:


fruits1.extend(fruits2)
print(fruits1)
print(fruits2)


# In[121]:


fruits1.append(fruits2)
print(fruits1)
print(fruits2)


# In[122]:


# COMMON METHOD TO DELETE DATA FROM LIST


# ## Pop method

# In[123]:


fruits =['orange','apple','pear','banana','kiwi']
fruits.pop(1)
print(fruits)


# # Delete operator

# In[126]:


fruits =['orange','apple','pear','banana','kiwi']
del fruits[1]
print(fruits)


# ## Remove Method

# In[127]:


fruits.remove('banana')
print(fruits)


# In[128]:


fruits.remove('mango')
print(fruits)


# ## In keyword with list

# In[129]:


fruits =['orange','apple','pear','banana','kiwi']

if 'apple' in fruits:
    print('apple is present')
else:
    print('not present')


# In[130]:


fruits =['orange','apple','pear','banana','kiwi']

if 'mango' in fruits:
    print('mango is present')
else:
    print('not present')


# ## Some More methods in List

# 1.count()

# In[132]:


fruits =['orange','apple','pear','banana','kiwi','apple','banana']
fruits.count('apple')


# In[133]:


fruits.count('orange')


# 2.sort()

# In[135]:


fruits.sort()
print(fruits)


# In[138]:


numbers =[3,5,1,9,10]
numbers.sort()
print(numbers)


# 3.Sorted()

# In[142]:


numbers =[3,5,1,9,10]
print(sorted(numbers))
print(numbers)


# 4.clear()

# In[144]:


numbers =[3,5,1,9,10]
numbers.clear()
print(numbers)


# 5.copy()

# In[146]:


numbers =[3,5,1,9,10]
numbers_copy = numbers.copy()
print(numbers_copy)


# ## 'IS' vs '==' Comparision

# In[ ]:


# ==, is 


# In[148]:


fruits1 =['orange','apple','pear']
fruits2 = ['banana','kiwi','apple','banana']
print(fruits1==fruits2)


# In[149]:


fruits1 =['orange','apple','pear']
fruits3 =['orange','apple','pear']
fruits2 = ['banana','kiwi','apple','banana']
print(fruits1==fruits3)


# In[150]:


fruits1 =['orange','apple','pear']
fruits3 =['orange','apple','pear']
fruits2 = ['banana','kiwi','apple','banana']
print(fruits1==fruits3)
print(fruits1 is fruits3) # same meomry place or not


# ## Join and Split Method

# 1. Split Method

# In[151]:


user_info = 'Vasundhara 24'.split()
print(user_info)


# In[152]:


user_info = 'Vasundhara,24'.split(',')
print(user_info)


# In[154]:


name,age = 'Vasundhara,24'.split(',')
print(name)
print(age)


# In[155]:


name,age = input('enter your name and age').split(',')
print(name)
print(age)


# 2. Join Method

# In[156]:


user_info = ['Vasundhara' ,'24']
print(','.join(user_info))


# ## List vs Array
# 
# List :  Ordered collection of items (in python)
# 
# -- Store any Data 
# 
# Array : Ordered collection of items (in english) : c,c++,java.
# 
# -- We can store only one data type in array (int,string)

# ## List vs String 
# 
# list: List are mutable
#     
# Strings: Strings are immutable

# In[158]:


s = 'string'
t= s.title()
print(t)


# In[159]:


l = ['word1','word2','word3']
l.append('word3')
print(l)


# In[163]:


l = ['word1','word2','word3']
l.pop()
print(l)


# # Looping in List 

# 1.For loop

# In[164]:


fruits =['orange','apple','pear','banana','kiwi','apple','banana']
for fruit in fruits:
    print(fruit)


# 2. While Loop

# In[165]:


fruits =['orange','apple','pear','banana','kiwi','apple','banana']
i=0
while i < len(fruits):
    print(fruits[i])
    i+=1


# ## List Inside List

# In[168]:


matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix[0]


# In[171]:


matrix = [[1,2,3],[4,5,6],[7,8,9]] # 2d list 
for sublist in matrix:
    for i in sublist:
        print(i) #*


# In[172]:


print(matrix[1][1])


# In[173]:


print(matrix[2][0])


# In[ ]:


# Type Function is used to check the data type 


# In[174]:


s = 'string'
print(type(s))


# In[176]:


print(type(matrix))


# # More About List 
# 
# 1. generate lists with range functions

# In[177]:


numbers = list(range(1,11))
print(numbers)


# In[185]:


nummbers2 = list(range(1,21))
print(numbers)


# 2. something more about pop method

# In[186]:


numbers = list(range(1,11))
numbers.pop()
print(numbers)


# In[ ]:


# poped_item = numbers.pop()
# print(numbers)


# 3. index method

# In[187]:


numbers.index(1)
print(numbers.index(1))


# In[188]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1]
print(numbers.index(1,3))


# In[189]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1,5,7,8,1]
print(numbers.index(1,11))


# In[190]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1,5,7,8,1]
print(numbers.index(1,11,14))


# 4. pass list to a list

# In[191]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(nubers))


# Exercise : Define a function who will take list containing numbers as input and return list containing square of every elements 

# In[192]:


# SOLUTION:
def square_list(l):
    square=[]
    for i in l:
        square.append(i*2)
    return square

numbers = list(range(1,11))
print(square_list(numbers)) #*


# Exercise: : Define a function which will take list as an argument and 
# this function will return a reversed list.

# In[193]:


def reverse_list(l):
    l.reverse()
    return l

numbers=[1,2,3,4,5,6,7]
print(reverse_list(numbers))


# In[194]:


def reverse_list(l):
    return l [::-1]

numbers=[1,2,3,4,5,6,7]
print(reverse_list(numbers))


# In[ ]:


# using apeend and pop method.


# In[276]:


def reverse_list(l):
    r_list = []
    for i in range(len(l)):
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list
numbers=[1,2,3,4,5,6,7]


print(reverse_list(numbers))


# In[277]:


def reverse_list(l):
    r_list = []
    for i in range(1,len(l)+1): # we can do with this also.
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list
numbers=[1,2,3,4,5,6,7]


print(reverse_list(numbers))


# Define a function that take list of words as argument and return with reverse of every element in that list.
# eg: ['abc','tuv','xyz']----> ['cba','vut','zyx']

# In[278]:


def reverse_elements(l):
    elements =[]
    for i in l:
        elements.append(i[::-1])
    return elements

words=['abc','tuv','xyz']
print(reverse_elements(words))
        


# Define a function:
# list---> [1,2,3,4,5,6,7]
# output--->[[1,3,5,7], [2,4,6]]

# In[281]:


def filter_odd_even(l):
    odd=[]
    even=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    output = [odd,even]
    return output
nums=[1,2,3,4,5,6,7]
print(filter_odd_even(nums))
                        


# Define a functions which take 2 list as input and return a list 
# whic contain common element of both lists.
# 
# input---> [1,2,5,8],[1,2,7,6]
# 
# output--> [1,2]

# In[282]:


def comoo_finder(l1,l2):
    output=[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output
print(comoo_finder([1,2,5,8],[1,2,7,6]))


# ## Min Max functions

# In[283]:


numbers=[6,60,2]
print(min(numbers))
print(max(numbers))


# Define a function which take input as list and return greatest 
# difference

# In[285]:


def greatest_diff(l):
    return max(l) - min(l)
    
print(greatest_diff(numbers))


# Define a function which takes input as a list inside list and return integer. 
# 
# [1,2,3,[1,2],[3,4]]---> input
# 
# 2--> output

# In[287]:


def sublist_counter(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count
mixed= [1,2,3,[1,2],[3,4]]
print(sublist_counter(mixed))


# ## List Comprehension

# Create a list of squares from 1 to 10

# In[543]:


squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)


# In[544]:


square2 = [i**2 for i in range(1,11)]
print(square2)


# In[546]:


negative_number = []
for i in range(1,11):
    negative_number.append(-i)
print(negative_number)


# In[548]:


new_negative=[-i for i in range(1,11)]
print(new_negative)


# Define a function that take list of strings. list containing reverse
# of every strings

# In[4]:


l =['abc','tuv','xyz']


# In[6]:


def reverse_strings(l):
    return[name[::-1] for name in l]

print(reverse_strings(['abc','tuv','xyz']))


# ## List comprehension with if statement

# In[ ]:


# [1,2,3,4,5,6,7,8,9,10]
# even numbers=[2,4,6]


# In[11]:


numbers = list(range(1,11))
nums=[]
for i in numbers:
    if i%2==0:
        nums.append(i)
print(nums)

even_nums = [i for i in numbers if i%2==0]
even_nums1= [i for i in range(1,11) if i%2==0]
print(even_nums)
print(even_nums1)

odd_nums =[i for i in numbers if i%2 !=0]
print(odd_nums)


# Define a function which takes 
# 
# input---> ['True', 'False', [1,2,3],1,1.0,3]
# 
# output ---> ['1','1.0','3']

# In[12]:


def num_to_string(l):
    return[str(i) for i in l if (type(i)== int or type(i)==float)]

print(num_to_string(['True', 'False', [1,2,3],1,1.0,3]))


# ## List comprehension with if else

# In[13]:


nums = [1,2,3,4,5,6,7,8,9,10]
# new_list =[-1,4,-3,8]


# In[14]:


new_list=[]
for i in nums:
    if i%2==0:
        new_list.append(i*2)
    else:
        new_list.append(-i)
        
print(new_list)


# In[15]:


new_list2=[i*2 if (i%2==0) else -i for i in nums ]
print(new_list2)


# ## List comprehension in nested list

# In[18]:


example = [[1,2,3],[1,2,3],[1,2,3]]
nested_comp = [[i for i in range(1,4)] for j in range(3)]
print(nested_comp)


# In[ ]:





# In[559]:


names=['Vasu','Teja','Muskaan']
# new_list=[]
# for names in names:
#      new_list.append(names[0])
# print(new_list)


# In[564]:


new_list2 = [name[0] for name in names]
print(new_list2)


# In[562]:


[x[0] for x in names]


# Define a function that takes list of strings. List containing reverse
# of every list

# In[570]:


l = ['abc','tuv','xyz']

def reverse_list(l):
    reverse = l.reverse()
    return reverse

print(reverse_list(l))


# In[ ]:


names=['Vasu','Teja','Muskaan']


# In[642]:


o


# In[627]:


[names[i][::-1] for i in range(0,len(names))]


# In[662]:


for i in range(0,10):
    if i%2==0:
        print(i)


# In[677]:


def even_num(vu):
    for i in range(0,vu):
        if i%2==0:
            even= i
            print(even)


# In[678]:


even_num(vu=10)


# # Tuple : Tuples are faster than lists

# ### Methods:
# 1.count
# 
# 2.index
# 
# 3.Len
# 
# 4.Slicing 

# ## 1.Looping in tuple

# In[290]:


mixed=(1,2,3,4.0)
# for loop and tuple

for i in mixed:
    print(i)
    
# Note: You can use while loop too.


# ## 2.Tuple with one element

# In[299]:


nums =(1)
print(type(nums))

# # if you want to create tuple with one element, you will have to put 
# comma (1,) then only it will be treated as tuple.


# In[300]:


nums =(1,)
print(type(nums))


# In[301]:


words =('word1')
print(type(words))


# In[302]:


words =('word1',)
print(type(words))


# In[298]:


mixed=(1,2,3,4.0)
print(type(mixed))


# ## 3.Tuple without parenthesis

# In[304]:


guitars = 'yamaha','baton rouge','taylor'
# by default it will be treated as tuple
print(type(guitars))


# ## 4.Tuple Unpacking

# In[305]:


guitarists=('Maneli Jamal','Eddie Van Der Meer','Andrew Foy')
guitarist1,guitarist2,guitarist3 = (guitarists)
print(guitarist1)


# In[306]:


guitarists=('Maneli Jamal','Eddie Van Der Meer','Andrew Foy')
guitarist1,guitarist2 = (guitarists)
print(guitarist1)


# ## 5.List inside tuple

# In[307]:


favourites = ('southern mangolia',['Tokyo Ghoul Theme','Landscape'])
favourites[1].pop()
print(favourites)


# In[308]:


favourites = ('southern mangolia',['Tokyo Ghoul Theme','Landscape'])
favourites[1].append('We made it ')
print(favourites)


# ## 6. Some functions that you can use with tuples
# 
# -- MIN
# -- MAX
# -- SUM

# In[311]:


mixed=(1,2,3,4.0)
print(min(mixed))


# In[312]:


mixed=(1,2,3,4.0)
print(max(mixed))


# In[313]:


print(sum(mixed))


# Define function returning two values

# In[314]:


def func(int1,int2):
    add=int1+int2
    multiply= int1*int2
    return add,multiply
print(func(2,3))


# In[315]:


def func(int1,int2):
    add=int1+int2
    multiply= int1*int2
    return add,multiply
add, multipy =func(2,3)
print(add)
print(multipy)


# In[316]:


# Something more about tuples, list, string.


# In[317]:


nums = tuple(range(1,11))
print(nums)


# In[318]:


nums = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(nums)


# In[321]:


nums = str((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(nums)
type(nums)


# In[323]:


num_list = str([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(num_list)
type(num_list)


# # Dictionaries: 
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

# Q. Why do we use dictionaries?
# 
# Because of limitation of lists, lists are not enough to represent
# real data.
# 
# eg. user['Vasundhara',24['coco','kimi no na wa'],['awakening','fairy tale']
# 
# This list contains user name, age, fav movies, fav tunes.
# You can do this but this is not a good way to do this.

# In[326]:


user={'name': 'Vasundhara', 'age':24}
print(user)
print(type(user))


# In[327]:


user1=dict(name='Vasundhara', age=24)
print(user1)


# In[329]:


# How to access data in dictionary?

print(user['name'])
print(user['age'])


# In[330]:


# Which type of data can be stored in dictionary? (anything)
# numbers,strings,list,dictionary


# In[332]:


user_info = {
    'name':'Vasundhara',
    'age': 24,
    'fav_movies': ['coco','kimi no na wa'],
    'fav_tunes': ['awakening','fairy tale'],
}

print(user_info['fav_movies'])


# In[340]:


users = {
    'user1': {
        'name': 'Vasundhara',
        'age': 24,
        'fav_movies': ['coco', 'kimi no na wa'],
        'fav_tunes': ['awakening', 'fairy tale'],
    }
}

print(user1)


# In[341]:


#How to add data to empty dictionary


# In[343]:


user_info2={}
user_info2['name']= 'Teja'
user_info2['age']= 24

print(user_info2)


# ## In Keywords and iterations in dictionary

# In[ ]:


user_info = {
    'name':'Vasundhara',
    'age': 24,
    'fav_movies': ['coco','kimi no na wa'],
    'fav_tunes': ['awakening','fairy tale'],
 }


# In[346]:


# Check if key exists in dictionary
# in keyword check for keys
if 'name' in user_info:
    print('present')
else:
    print('not present')


# In[347]:


if 'names' in user_info:
    print('present')
else:
    print('not present')


# In[355]:


# Check if value exists in dictionary-----> values method

if 'Vasundhara' in user_info.values():
    print('present')
else:
    print('not present')


# In[351]:


if 'Vasundhara' in user_info:
    print('present')
else:
    print('not present')


# In[352]:


if 24 in user_info.values():
    print('present')
else:
    print('not present')


# In[354]:


# To check for complete list
if ['coco','kimi no na wa'] in user_info.values():
    print('present')
else:
    print('not present')


# In[356]:


# Loops in dictionary
for i in user_info:
    print(i)


# In[357]:


for i in user_info.values():
    print(i)


# ### Values Method

# In[359]:


user_info_values= user_info.values()
print(user_info_values)
type(user_info_values)


# ## Keys Method

# In[360]:


user_info_keys= user_info.keys()
print(user_info_keys)
type(user_info_keys)


# In[362]:


#loops in dictionaries
for i in user_info:
    print(user_info[i])


# ## Items Methods

# In[363]:


user_items = user_info.items()
print(user_items)
type(user_items)


# In[367]:


for i,j in user_info.items():
    print(f'key is {i} and value is {j}')


# In[381]:


# How to add and delete data

user_info = {
    'name':'Vasundhara',
    'age': 24,
    'fav_movies': ['coco','kimi no na wa'],
    'fav_tunes': ['awakening','fairy tale'],
 }

# How to add data

user_info['fav_songs']=['song1','song2']
print(user_info)


# In[382]:


# How to delete data (pop method) ***
popped_item = user_info.pop('fav_tunes')
# print(f'poped_item is {popped_item}')
# print(user_info)
# print(type(popped_item))


# In[371]:


# Pop item Method 

popped_item = user_info.popitem()
print(user_info)
print(popped_item)
print(type(popped_item))


# In[383]:


# Update Method

user_info = {
    'name':'Vasundhara',
    'age': 24,
    'fav_movies': ['coco','kimi no na wa'],
    'fav_tunes': ['awakening','fairy tale'],
 }

more_info ={'state':'Haryana','hobbies':['coding','reading','guitar']}
user_info.update(more_info)
print(user_info)


# In[384]:


user_info = {
    'name':'Vasundhara',
    'age': 24,
    'fav_movies': ['coco','kimi no na wa'],
    'fav_tunes': ['awakening','fairy tale'],
 }

more_info ={'name': 'Vasundhara Uniyal','state':'Haryana','hobbies':['coding','reading','guitar']}
user_info.update(more_info)
print(user_info)


# In[385]:


user_info = {
    'name':'Vasundhara',
    'age': 24,
    'fav_movies': ['coco','kimi no na wa'],
    'fav_tunes': ['awakening','fairy tale'],
 }

more_info ={'name': 'Vasundhara Uniyal','state':'Haryana','hobbies':['coding','reading','guitar']}
user_info.update({})
print(user_info)


# In[386]:


# From Keys

d={'name': 'unknown', 'age':'unknown'}
d=dict.fromkeys(['name','age','height'],'unknown')
print(d)


# In[387]:


d={'name': 'unknown', 'age':'unknown'}
d=dict.fromkeys(('name','age','height'),'unknown')
print(d)


# In[388]:


d=dict.fromkeys('abc', 'unknown') # string
print(d)


# In[389]:


d=dict.fromkeys(range(1,11), 'unknown') 
print(d)


# In[391]:


d=dict.fromkeys(['name', 'age'],['unknown','unknown'])
print(d)


# # Get Method 

# In[392]:


d={'name':'unknown',
   'age':'unknown'}
print(d['name'])


# In[396]:


d={'name':'Teja',
   'age':'unknown'}
print(d['names'])


# In[397]:


print(d.get('name'))


# In[398]:


print(d.get('names')) # better


# In[401]:


if 'name' in d:
    print('present')
else:
    print('not present')


# In[400]:


if d.get('names'):
    print('present')
else:
    print('not present')


# # Clear Method

# In[402]:


d.clear
print(d)


# # Copy Method

# In[408]:


#d1=d.copy()
# d1=d
# print(d1)


# In[405]:


# print(d1.popitem())
# print(d)


# In[406]:


print(d1 is d)


# In[407]:


print(d1 == d)


# ## More about get method()

# In[412]:


user={'name': 'Teja', 'age': 24}
print(user.get('names','not found! '))


# In[413]:


user={'name': 'Teja', 'age': 24}
print(user.get('fav','not '))


# In[414]:


user={'name': 'Teja', 'age': 24, 'age':25}
print(user)


# In[415]:


user={'name': 'Teja', 'age': 25, 'age':24}
print(user)


# Define a function that takes a number(n). Return a dictionary 
# containing cube of number from 1 to n

# In[417]:


def cube_finder(n):
    cubes = {}
    for i in range(1,n+1):
        cubes [i] = i**3
    return cubes

print(cube_finder(10))

    


# In[418]:


# Word Counter
# Vasundhara
d = {'a':3, 'h':1,'a':3}
print(d)


# In[419]:


d = {'a':3, 'h':1,'a':4}
print(d)


# In[424]:


def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count
print(word_counter('Vasundhara'))


# Take an input from user and store it in a dict.
# 
# eg: name,age,fav movies and fav songs.

# In[425]:


user = {}

name = input('What is your name :')
age = int(input('What is your age :'))
fav_movies = input('What is your favourite movies :').split(',')
fav_songs = input('What is your favourite songs :').split(',')

user['name']=name
user['age']= age 
user['fav_movies']= fav_movies
user['fav_songs']= fav_songs

print(user)


# In[427]:


user = {}

name = input('What is your name :')
age = int(input('What is your age :'))
fav_movies = input('What is your favourite movies :').split(',')
fav_songs = input('What is your favourite songs :').split(',')

user['name']=name
user['age']= age 
user['fav_movies']= fav_movies
user['fav_songs']= fav_songs

for key, value in user.items():
    print(f'{key}:{value}')


# # Dictionary Comprehension

# In[ ]:


# square = {1:1,2:4,3:9}


# In[20]:


square = {num:num**2 for num in range(1,11)}
print(square)


# In[ ]:


# square of 1:1


# In[22]:


square = {f"square of {num} is":num**2 for num in range(1,11)}
print(square)


# In[23]:


for k,v in square.items():
    print(f"{k}:{v}")


# In[ ]:


# Count the character in string
# VASUNDHARA


# In[25]:


string = 'Vasundhara'
word_count = {char:string.count(char) for char in string}
print(word_count)


# ## Dictionary Comprehension with if else

# In[26]:


d = {1:'odd', 2:'even'}
odd_even = {i:('even'if i%2==0 else 'odd')for i in range(1,11)}
print(odd_even)


# ## Set() : 
# can not store list and dictionary and tuple.
# 
# Number can be store in stet.

# In[513]:


s= {1,2,3,2}
print(s)


# In[ ]:


# No indexing can be done in set 


# In[516]:


l = [1,2,3,4,5,5,5,5,6,7,7,8]
# remove duplicate
s2=set(l)
print(s2)


# In[517]:


# Convert to list 
list(set(s2))


# In[519]:


# Add item in set
s.add(4)
s.add(5)
s.add(4)
print(s)


# In[520]:


# Remove item in set
s.remove(3)
print(s)


# Discard Method same as remove method

# In[522]:


s.discard(5)
print(s)


# Clear method

# In[524]:


s.clear()
print(s)


# Copy method

# In[525]:


s1=s.copy()
print(s1)


# In[530]:


s={1,1.0,2.3,'string'}
print(s)
#1 and 1.0 are same so it will print 1


# In[531]:


s={1,1.1,2.3,'string'}
print(s) #unordered collection


# In[533]:


s={1,1.1,2.3,'string',[1],{1:1}}
# can not store list and dict.


# # In keyword 

# In[534]:


s ={'a','b','c'}
# check if item is present or not 

if 'a' in s:
    print('present')
else:
    print('not present')


# In[535]:


# Loop

for item in s:
    print(item)


# In[536]:


l = [1,2,3,3]
set(l) # to remove duplicate


# ## Set maths

# In[541]:


s1 = {1,2,3,4}
s2={3,4,5,6}


# ## Union

# In[538]:


# union_set= s1|s2
# print(union_set)


# # Intersection

# In[542]:


print(s1 & s2)


# # Set comprehension

# In[29]:


s = {k**2 for k in range(1,11)}
print(s)


# In[31]:


names = ['Muskaan','Vrinda','Teja']
first = {name[0] for name in names }
print(first)


# ## Escape sequences
# 
# 1. \' -- Single quote
# 2. \" -- Double quote
# 3. \\ -- Backslash
# 4. \n -- New line
# 5. \t -- Tab
# 6. \b -- Backspace

# In[ ]:


# Escape sequence - backslash single quote \'


# In[17]:


print('I\'m Dhara')


# In[ ]:


# Escape sequence - backslash doublequote \"


# In[15]:


print("Hello \"world\" world")


# In[ ]:


# Escape sequence - backslash New Line \n


# In[19]:


print("line A")
print("Line B")


# In[23]:


print("line A\nline B\nLine C")


# In[ ]:


# Escape sequence - backslash tab \t


# In[24]:


print("line A\nline B\nLine C")
print('name\tDhara')


# In[ ]:


# # Escape sequence - backslash \\


# In[26]:


print("line A\nline B\nLine C")
print('name\tDhara')
print("this is \ backslash")


# In[27]:


print("line A\nline B\nLine C")
print('name\tDhara')
print("this is backslash\")


# In[32]:


print("line A\nline B\nLine C")
print('name\tDhara')
print("this is backslash\\") # double \\ mean single\.


# In[33]:


print("line A\nline B\nLine C")
print('name\tDhara')
print("this is double backslash\\\\") # this is double backslash.


# In[ ]:


# Escape sequence - backslash bacspace \b


# In[37]:


print("line A\nline B\nLine C")
print('name\tDhara')
print("this is double backslash\\\\")
print("hell\blo")


# ## Comments

# In[ ]:


# comments -- it is for user (for information)


# In[ ]:


print("line A\nline B\nLine C") ## for new line
print('name\tDhara')
print("this is double backslash\\\\") #\\ is for backslash
print("hell\blo")


# In[38]:


# print("")-- control+/(to comment the line)


# ## Escape characters as normal text

# In[45]:


# OUTPUT : Line A \n Line B


# In[40]:


print("line A\nline B")


# In[42]:


print("line A\\nline B") # n will be trated as. normal text.


# In[43]:


print("line B\\tline B")


# In[44]:


print("this is 4 backslash\\\\\\\\")


# In[ ]:


# OUTPUT : \" \'


# In[46]:


print(" \" \' ")  


# In[47]:


print(" \\\" \\\' ")


# In[48]:


# Exercise:

# 1. this  is \\ double backslash
# 2. these are /\/\/\/\/\ mountains
# 3. he is.    awesome (use escape sequence instead of space)
# 4. \" \n \t' (print this as an output)


# In[49]:


print('THIS IS \\\\ DOUBLE BACKSLASH')


# In[51]:


print("THESE ARE /\/\/\/\/\ MOUNTAINS")


# In[52]:


print("he is\tawesome")


# In[63]:


print(" \\\" \\n \\t'")


# # Raw Strings

# In[66]:


print(r"line A\nline  B") # by adding r we can treat any excape sequence as normal text.


# In[67]:


print(r"line A\"line  B")


# In[68]:


# How to print emoji


# In[73]:


print("\U0001F602")


# In[74]:


# How to use python as a calculator


# In[75]:


print(2+3)


# In[76]:


print(2+3*4)


# # Operators
# 
# 1. "+" : Addition
# 2. "- : Subtraction
# 3. "*" : Multiplication
# 4. "/" : Floor Division
# 5. "//" : Integer Division
# 6. "%" : Modulus, gives remainder
# 7. "**" : Exponent

# In[77]:


print(2+3)


# In[78]:


print(2-3)


# In[83]:


print(2+3*3)


# In[80]:


print(2/4) # floating point division


# In[81]:


print(4//2) # integer division


# In[82]:


print(2//4)


# In[84]:


print(2**3)


# In[89]:


print(2**0.5) #square root


# In[91]:


round(2**0.5,4) 


# In[93]:


print(2**3/2*6-4*(3-4/2))


# ### Precendence Rule:
# Operators : Precendence and Associativity Rule
# 
# Parenthese : Highest
# 
# Exponent : Right to left
# 
# *,/,//,%  : Left to right
# 
# +,-  : Left to right 

# In[ ]:


Associativity rule : 


# In[94]:


print((2+3)*2)


# In[95]:


print((2+3)/2)


# In[96]:


print((2+3)*5/2%6)


# In[98]:


# Exponent
print(2**3**2)
# (2**9)


# # Variables 

# In[99]:


number1 = 2
print(number1)


# In[100]:


number1=4  # we can assign number to varaibles.
print(number1)


# In[102]:


name = 'Dhara'
print(name)


# In[103]:


name = 123
print(name)


# ## This called dynamic programming language.
# Here the data is changing, we don need to declare varaibles.

# ## Rules for naming a varaibles
# 1. Varaibles cannot start with number (1Number=4)
# 2. Special symbols cannot be used ($USD=5)

# In[ ]:


# Naming convenctions for variables
user_one_name= 'Rocky' # This is called snak case writing.
userOneName = 'Abhi' # This is called camel case writing.


# ## Sting Concat

# In[104]:


#string concat
first_name = 'Vasundhara'
last_name= 'Uniyal'
full_name = first_name+last_name
print(full_name)


# In[105]:


first_name = 'Vasundhara'
last_name= 'Uniyal'
full_name = first_name + " "+ last_name
print(full_name)


# In[ ]:


# we can not add number with a string


# In[106]:


first_name = 'Vasundhara'
last_name= 'Uniyal'
full_name = first_name + " "+ last_name
print(first_name + 3) #error


# In[107]:


first_name = 'Vasundhara'
last_name= 'Uniyal'
full_name = first_name + " "+ last_name
print(first_name + '3') #no error


# In[108]:


first_name = 'Vasundhara'
last_name= 'Uniyal'
full_name = first_name + " "+ last_name
print(first_name + str(3)) #no error


# In[ ]:


# We can use multiply sign in string.


# In[109]:


print(first_name *3)


# ## User Input Function

# In[111]:


name = input('type your name ')


# In[114]:


name = input('type your name ')
print("Hello " + name )


# In[ ]:


# Input function will take input in string.


# In[115]:


age = input("What is your age ? ")
# input is taken as a string.


# In[116]:


print("your age is " + age)
# input was taken as string. Therfore concat happened.


# # Int() Function

# In[120]:


number_one= input("enter first number")
number_two = input("enter second number")
total = number_one + number_two
print("total is " + total )


# In[122]:


number_one= int(input("enter first number"))
number_two = int(input("enter second number"))
total = number_one + number_two
print("total is " + str(total ))


# ### String function
# 4--> '4' # will change in sting 4
# ### Int function 
# '4'--> 4 # will chane in int
# ### Float function
# '4'--> 4.0 # will change in float

# In[123]:


number1= str(4)
number2= float('44')
number3= int('33')
print(number2 + number3)


# In[ ]:


# We can add int and float and the output will be in float.


#  ## More about varaibles

# In[128]:


name,age = 'Vasundhara', 24
print('Hello ' + name + ' your age is '+ str(age))


# In[125]:


type(name)


# In[126]:


type(age)


# In[ ]:


# In a single line we can declare same values to multiple varaibles.


# In[129]:


x=y=z=1
print(x+y+z)


# ## More than one input in one line

# In[131]:


name = input('Enter your name ')
age = input ('Enter your age ')


# In[135]:


name,age = input('Enter your name and age ').split() # split is a str func
print(name)
print(age)


# In[136]:


name,age = input('Enter your name and age ').split(",") 
# we can chage space by comma.
print(name)
print(age)


# # Sting formatting

# In[137]:


name = 'Vasu' # {} -- Place Holder
age = 24
print('Hello {} your age is {} '.format(name,age)) #python 3 formatting


# In[141]:


print(f'Hello {name} your age is {age} ') # string formating


# In[142]:


# We can do calculation in string formatting.
print(f'Hello {name} your age is {age + 3} ')


# In[ ]:


# Enercise 
Ask user to input 3 numbers and you have t0 print average of 3 numbers 
using string formatting
Bonus: Try to take all three comma seperated inputs in one line.


# In[3]:


# number1= input('enter first number :')
# number2= input('enter second number :')
# number3= input('enter third number :')
number1,number2,number3 = input('enter three number comma seperated').split(',')
print(f'average of three numbers :{(int(number1) + int(number2) + int(number3))/3}')


# # String Indexing

# In[4]:


language ='python' #position(index number), position starts with 0
print(language[2]) # we use [] for indexing


# In[5]:


language ='python' 
print(language[4])


# In[12]:


language = 'java'
print(language[4])


# In[ ]:


#P =0, -6
#Y =1, -5
#T =2, -4
#H =3, -3
#O =4, -2
#N =5, -1


# In[13]:


language ='python' 
print(language[-1])


# In[14]:


language ='python' 
print(language[-6])


# In[15]:


language ='python' 
print(language[-7])


# # Slicing/Selecting Sub sequences

# In[16]:


lang = 'Python'
# syntax- [start argument : stop argument -1]
print(lang[0:2])


# In[17]:


print(lang[2:4])


# In[18]:


print(lang[3:6])


# In[19]:


print(lang[-3:6])


# In[20]:


print(lang[:])


# In[21]:


print(lang[1:])


# In[22]:


print(lang[2:])


# In[23]:


print(lang[:3])


# # Step Argument

# In[24]:


# syntax - [start argument : stop argument -1 : step]
print("Vasundhara"[2:5])


# In[26]:


print("Vasundhara"[0:5:1])


# In[28]:


print("Vasundhara"[0:5:2])


# In[29]:


print("Vasundhara"[0::2])


# In[31]:


print("Vasundhara"[::3])


# In[34]:


# Backwards
print("Vasundhara"[5::-1])


# In[35]:


print("Vasundhara"[::-1]) 


# ### Exercise
# Ask user name and print back user name in reverse order.

# In[40]:


name= input('Enter your name ')
print(name[::-1])
# print(f'reverse of your name is {name[-1::-1]}')


# # String Methods
# 1. len()function : used to count the length
# 2. lower() function: small alphabets
# 3. upper()function:
# 4. title()function:
# 5. count()function:

# In[41]:


print(len('Vasundhara'))


# In[ ]:


name = Vasundhara


# In[42]:


print(len(name))


# In[44]:


name.lower()
# we use dot in methods.


# In[45]:


name.upper()


# In[46]:


name.title()


# In[48]:


print(name.count('a'))


# ## Exercise 
# Take 2 comma seperated input from user
# 1. users name 
# 2. A single character
# 
# output: 2 print lines
# 
# 3. User name length
# 4. count the character that user inputed

# In[59]:


name,character=input('Enter comma seperated name and character').split(",")
print(f'length of your name is {len(name)}')
print(f'character count : {name.count(character)}') # case sensitive


# In[66]:


name,character=input('Enter comma seperated name and character').split(",")
print(f'length of your name is {len(name)}')
print(f'character count : {name.strip().lower().count(character.strip())}')


# In[ ]:


#name.strip().lower().count(character.strip())
#character.strip().lower().count(character.strip())


# # Strip Method

# In[60]:


#lstrip method
name ="      Vasundhara     "
dots = "...................."
print(name + dots)
print(name.lstrip()+dots)


# In[61]:


#rstrip method
name ="      Vasundhara     "
dots = "...................."
print(name + dots)
print(name.rstrip()+dots)


# In[62]:


# strip method
print(name.strip()+dots)


# In[65]:


print(name.replace(" ","")+dots)


# # Replace and Find Method

# In[68]:


#Replace Method
string = 'She is beautiful and she is a good dancer'
print(string.replace("","_"))


# In[69]:


string = 'She is beautiful and she is a good dancer'
print(string.replace("is","was"))


# In[70]:


string = 'She is beautiful and she is a good dancer'
print(string.replace("is","was",3))


# In[71]:


# Find Method is used to find character position
string = 'She is beautiful and she is a good dancer'
print(string.find("is"))


# In[74]:


string = 'Is She is beautiful and she is a good dancer'
print(string.find("is",1))


# In[76]:


string = 'Is She is beautiful and she is a good dancer'
is_position1= string.find("is") # is position-- number
is_position2 = string.find("is",is_position1)
print(is_position1)


# In[77]:


string = 'Is She is beautiful and she is a good dancer'
is_position1= string.find("is") # is position-- number
is_position2 = string.find("is",is_position1 + 1)
print(is_position1)


# # Center Method 

# In[79]:


name = 'Vasundhara'
# **Vasundhara**
name.center(14,"*")


# In[82]:


name=input('Enter your name')
print(name.center(len(name)+8,"*"))


# In[83]:


# Strings are immutable
string='string'
print(string[1])


# In[84]:


string='string'
string[1]='T'
# cannot change


# In[85]:


string='string'
print(string.replace("t","T"))


# In[88]:


string='string'
string.replace("t","T")
print(string) #you cannot change string after defining it


# In[89]:


# More Assignment operator
name ='Vasun'
name = name + "dhara" #name+=
print(name)


# In[92]:


name ='Vasun'
name += "dhara" 
print(name)


# In[93]:


age =24
age=age +1
print(age)


# In[94]:


age =24
age=age *81
print(age)


# In[95]:


age =24
age=age +81
print(age)


# In[96]:


age =24
age=age -81
print(age)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # If statement : is used if condition is true or not
# 
# if conditions
# 
# if conditions is true the this code will execute

# In[ ]:


# eg : game age 14 can play.


# In[103]:


age = input('Enter your age : ')
age=int(age)
if age >=14: # if blog (writing if statement inside the blog)
    print('you are above 14')


# In[104]:


age = input('Enter your age : ')
age=int(age)
if age >=14:
    print('you are above 14')


# In[106]:


age = input('Enter your age : ')
age=int(age)
if age >=14:
    print('line a ')
    print('you are above 14')


# # Pass Statement 

# In[108]:


x = 18
if x>18:
    pass # means you dont want to write anything.


# # Else Statement
# We use else statement always after if statement
# 
# Else statement cant be alone

# In[111]:


age = input('Enter your age : ')
age=int(age)
if age >=14:
    print('line a ')
    print('you are above 14')
else:
    print("sorry, you can't play")


# In[112]:


age = input('Enter your age : ')
age=int(age)
if age >=14:
    print('line a ')
    print('you are above 14')
else:
    print("sorry, you can't play")


# ## Exercise (Number guessing game)
# Make a variable, like winning-number  and assign any number to it 
# if user guessed a number correctly then print you win!!

# In[117]:


winning_number = 27
user_input = input('Guess number between 10 to 100 : ')
user_input = int(user_input)
if user_input==winning_number:
    print('You win')
else: # Nested if else
    if user_input<winning_number:
        print('Too low')
    else:
        if user_input>winning_number:
            print('Too high')


# ## Check two conditions at same time 
#  
# And Operator : Both conditions needs to be true

# In[118]:


name = 'abc'
age=19
if name == 'abc' and age ==19:
    print('condition true')
else:
    print('condition false')


# In[119]:


name = 'abc'
age=19
if name == 'abc' and age ==23:
    print('condition true')
else:
    print('condition false')


# ### OR Operator : if one condition is true then condition is true.

# In[121]:


name = 'abc'
age=19
if name == 'abc' or age ==19:
    print('condition true')
else:
    print('condition false')


# In[122]:


name = 'abc'
age=19
if name == 'abc' or age ==34:
    print('condition true')
else:
    print('condition false')


# In[123]:


name = 'abc'
age=19
if name == 'bcd' or age ==19:
    print('condition true')
else:
    print('condition false')


# ## Exercise:
# Ask user name and age
# if user's name start with (a or A) and age is above 10 then 
# print you can watch coco movie
# Else print 'sorry' you cannot watch movie

# In[128]:


name= input('Enter your name : ')
age = int(input('Enter your age'))
if age>=10 and (name[0]=='a' or name[0]=='A'):
    print('You can watch coco movie')
else: # Nested if else
        print('You cannot watch coco')


# # If Elif Statement : Used to check multiple conditions.
# 
# 
# Eg:
# 
# show ticket pricing 
# 1 to 3 (free)
# 4 to 10(150)
# 11 to 60 (250)
# above 60 (200)

# In[141]:


age = int(input('Enter your age:'))
if age ==0 or age<0:
    print('You can not watch')
elif 0<age<=3:
    print('Ticket price : Free')
elif 3<age<=10:
    print('Ticket price : 150')
elif 10<age<=60:
    print('Ticket price : 250')
else:
    print('Ticket price : 200')


# ## In keyword 
# ## If with in 

# In[144]:


name = 'Vasundhara'
if 'a' in name:
    print('a is present in name')
else:
    print('not present')


# In[145]:


# Check empy or not 
# important

name = 'abc'
if name:
    print('string is not empty')
else:
    print('string is empty')


# In[146]:


name = ''
if name:
    print('string is not empty')
else:
    print('string is empty')


# In[148]:


name = input('enter your name')
if name:
    print(f'your name is {name}')
else:
    print('You didnt type anything')


# # While Loop, For Loop

# In[149]:


# print('hello world') # 10 times


# In[150]:


i= 1 # i = 2, i=3
while i<=10:
    print('Hello world')
    i= i +1
    
# hello world
# hello world
# hello world


# In[ ]:


# sum of numbers using while loop


# In[152]:


total = 0
i=1 # i=2
while i<=10:
    total = total+i # +-=i
    i = i +1
print(total)
# total = 0+1+2+3+4+5


# In[153]:


total = 0
i=1 # i=2
while i<=20:
    total = total+i # +-=i
    i = i +1
print(total)


# ## Exercise
# sum of n natural numbers
# ask user for natural numbers
# print total from 1 to n

# In[158]:


n = int(input('Enter a number:'))
total = 0
i=1 # i=2
while i<=n:
    total +=i # +-=i
    i +=1
print(total)


# Ask user to input a number containing more than one digit.

# In[163]:


number = input('Enter a number')
total = 0
i=0 # i=2 #int(number[1])
while i<=len(number):
    total += int(number[i])
    i +=1
print(total)


# ### Ask a user for name 
# print count of each words 
# output:
# 
#     V-1
#     A-4
#     S-1
#     U-2
#     N-2
#     D-1
#     H-1
#     A-4
#     R-1
#     A-4
#     
#     U-2
#     N-2
#     I-1
#     Y-1
#     A-4
#     L-1
#     

# In[1]:


name = input('Enter your name')
i=0
while i <len(name):
    print(f'{name[i]}: {name.count(name[i])}')
    i += 1


# In[2]:


name = input('Enter your name')
temp_var =''
i=0
while i <len(name):
    if name[i] not in temp_var:
        temp_var+-name[i]
        print(f'{name[i]}: {name.count(name[i])}')
    i += 1


# ## Infinite Loop : Are those loop which never stops.

# In[1]:


#i =0
#while i <=10:
    #print('Hello World')
    
# infinite loop
#while True:
    #print('Hello world')


# In[2]:


i =0
while i <=10:
    print('Hello World')
    i+=1


# ## For loop with range function

# In[3]:


for i in range (10): # 0 to 9
    print('Hello World')
    
# hello world
#hello world


# In[4]:


for i in range (10): # 0 to 9
    print(f'Hello World:{i}')
    
# hello world
#hello world


# In[6]:


for i in range (1,11): # 0 to 9
    print(f'Hello World:{i}')
    print('this is line\n')
    
# hello world
#hello world


# ## For loop Example
# sum from 1 to 10
# 1+2+3............10

# In[7]:


total = 0    #1+2+3+4+..........20
for i in range(1,11):
    total+=i
print(total)  


# In[11]:


n = int(input('enter the number:'))
total = 0
for i in range(1,n+1):
    total+=i
print(total)

Ask user a number like 1256

calculate sum of digits -----> 1+2+5+6

logic :
num ='1256' #length = 4
int(num[0])----> 1
int(num[1])----->2
int(num[2])----->5
int(num[3])----->6
i----> 0 to 3
# In[15]:


total = 0
num =input('Enter a number:')
for i in range (0,len(num)):
    total+=int(num[i])
print(total)

Ask user name and count each character
# Vasundhara Uniyal
# In[16]:


name = input('Enter your name:')
temp=''
for i in range (0,len(name)):
    if name[i] not in temp:
        print(f"{name[i]}:{name.count(name[i])}")
        temp+=name[i]


# # Break and Continue
# Break is used break the loop.

# In[ ]:


# eg: print number (1,10)


# In[18]:


for i in range(1,11):
    if i ==5:
        break
    print(i)


# In[ ]:


# eg: print 1 to 10 , nut not 5


# In[19]:


for i in range (1,11):
    if i ==5:
        continue
    print(i)


# ## Exercise (Number guessing game)
# Make a variable, like winning-number  and assign any number to it 
# if user guessed a number correctly then print you win!!

# In[30]:


import random


# In[26]:


winning_number =43
guess = 1
number = int(input('Guess a number between 1 and 100'))
game_over = False
while not game_over:
    if number==winning_number:
        print(f'You win  and you guess this number in {guess} times')
        game_over=True   
    else:
        if number < winning_number:
            print('Too Low')
            guess +=1
            number = int(input('guess again:'))
        else:
            print('Too High')
            guess+=1
            number = input('guess again:')


# ### Dry principal of coding- don't repeat yourself

# In[27]:


winning_number =43
guess = 1
number = int(input('Guess a number between 1 and 100'))
game_over = False
while not game_over:
    if number == winning_number:
        print(f'You win  and you guess this number in {guess} times')
        game_over=True   
    else:
        if number < winning_number:
            print('Too Low')
        else:
            print('Too High')
            guess+=1
            number = input('guess again:')


# In[29]:


winning_number =43
guess = 1
number = int(input('Guess a number between 1 and 100'))
game_over = False
while True:
    if number == winning_number:
        print(f'You win  and you guess this number in {guess} times')
        Break   
    else:
        if number < winning_number:
            print('Too Low')
        else:
            print('Too High')
        
        guess+=1
        number = input('guess again:')


# ## Step Argument in Range

# In[31]:


for i in range (1,11,2):
    print(i)


# In[32]:


for i in range (10,0,-1):
    print(i)


# In[33]:


for i in range (10,-1,-1):
    print(i)


# ## For loop and string

# In[34]:


name = 'Vasundhara'
for i in range (len(name)):
    print(name[i])


# In[35]:


name = 'Vasundhara'
for i in name:
    print(i)


# In[39]:


# 1256---->1+2+5+6
num = input('enter a number:')
total =0
for i in num:
    total +=int(i)
print(total)


# ## Functions

# In[42]:


def add_two(a,b):
    return a+b

total=add_two(10,4) 
print(total)


# In[43]:


a = int(input('enter first number'))
b= int(input('enter second number'))
total = add_two(a,b)
print(total)


# In[44]:


first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
print(add_two(first_name,last_name))


# # Return Vs Print

# In[46]:


def add_three(a,b,c):
    return a+b+c
    # print can also be used in case of return.
print(add_three(5,5,5))


# In[47]:


add_three(5,5,5)


# ## Function Practice

# In[48]:


def last_char(name):
    return name[-1]
print(last_char('Vasundhara'))


# In[50]:


def odd_even(num):
    if num%2==0:
        return 'Even'
    else:
        return 'odd'
print(odd_even(10))


# In[51]:


def odd_even(num):
    if num%2==0:
        return 'Even'
    else:
        return 'odd'
print(odd_even(9))


# In[55]:


def odd_even(num):
    if num%2==0:
        return 'Even'
   
    return 'Odd'


print(odd_even(9))


# In[56]:


def is_even(num): # PARAMETER
    if num%2==0:
        return True # ARGUMENT
    
print(is_even(10))


# In[58]:


def song():
    return 'happy birthday song'
print(song())


# In[62]:


# Exercise : define the function greater of 2 number

def greater(a,b):
    if a>b:
        return a
    else:
        return b
    
num1= int(input('Enter first number'))
num2= int(input('Enter second number'))
bigger = greater(num1,num2)

print(f"{bigger} is greater")


# In[66]:


# Exercise : define the function greater of 3 number
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    



print(greatest(100,40,30))


# ## Function inside Function

# In[70]:


def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger,c)

print(new_greatest(1000,200,30))


# In[72]:


#Exercise: Is palindrom or not.
def is_palindrom(word):
    reversed_word =word[::-1]
    if word == reversed_word:
        return True
    else:
        return False
print(is_palindrom('naman'))
print(is_palindrom('horse'))


# In[73]:


def is_palindrom(word):
    return word == word[::-1]

print(is_palindrom('naman'))
print(is_palindrom('horse'))


# In[80]:


def is_palindrom(word):
     if word == word[::-1]:
        return True
        return False

print(is_palindrom('naman'))
print(is_palindrom('horse'))    


# # Define Fibonacci : 0 1 1 2 3 5 8 13 21 34

# In[ ]:


# 1---> 0
# 2--->0 1
# 3---> 0 1 1


# In[81]:


for i in range(1,11):
    print(i, end=",")


# In[88]:


def fibonacci_seq(n):
    a=0 #first number
    b=1 #second number
    if n==1:
        print(a)
    elif n==2:
        print(a,b) #a b , 0 1
    else:
        print(a,b, end = " ")
        for i in range(n-2):
            c= a+b
            a= b
            b= c
            print(b, end =" ")
fibonacci_seq(20)


# # Default Parameters

# In[96]:


def user_info(first_name = 'unknown',last_name ='unknown',age = None):
       print(f'your first name is {first_name}')
       print(f'your last name name is {last_name}')
       print(f'your age {age}')
   
user_info('Vasundhara',24)


# # Scope of Variable inside and outside functions

# In[97]:


def func():
    x = 7 # we can not use this varaible outside this function
    # local variable
    return x

def func2():
    print(x)
    
func2()


# In[98]:


def func():
    x = 7 
    return x

print(x)


# In[99]:


def func():
    x = 7 
    return x
print(func())
print(x)


# In[100]:


x=5 #global variable
def func():
    x = 7 
    return x
print(func())
print(x) 


# In[101]:


x=5 #global variable
def func():
    global x
    x = 7 
    return x
print(func())
print(x)


# In[102]:


x=5 #global variable
def func():
    global x
    x = 7 
    return x
print(x)
print(func())
print(x)


# # Intro to *args/*operator

# In[33]:


def total(a,b):
    return a+b
print(total(2,4))


# In[41]:


def all_total(*args):
    print(args)
    print(type(args))
    
# all_total(1,2,3,4,5,65)
# t=(1,2,3,4,5,65)


# In[43]:


def all_total(*args):
    print(args)
    print(type(args))
all_total(1,2,3,4,5,65)   


# In[46]:


def all_total(*args):
    total =0
    for num in args:
        total+=num
    return total



print(all_total(1,2,3,4))


# # *args with normal parameter

# In[49]:


# When we define a function it is called normal parameter
# When we call a function then it is called argument
def multiply_nums(*args):
    multiply = 1
    for i in args:
        multiply*=i
    return multiply
print(multiply_nums(1,2,3,4))


# In[51]:


def multiply_nums(nums,*args):
    multiply = 1
    print(nums)
    print(args)
    for i in args:
        multiply*=i
    return multiply
print(multiply_nums(2,2,3))


# In[52]:


def multiply_nums(*args):
    multiply = 1
    for i in args:
        multiply*=i
    return multiply
print(multiply_nums(2,2,3))


# In[54]:


def multiply_nums(nums,*args):
    multiply = 1
    for i in args:
        multiply*=i
    return multiply
print(multiply_nums())


# In[56]:


def multiply_nums(nums,*args):
    multiply = 1
    print(args)
    for i in args:
        multiply*=i
    return multiply
print(multiply_nums(2,4))


# In[61]:


def multiply_nums(num1,num2,*args):
    multiply = 1
    print(args)
    for i in args:
        multiply*=i
    return multiply
print(multiply_nums(2,4,3,4))


# In[62]:


def multiply_nums(*args,num):
    multiply = 1
    print(args)
    for i in args:
        multiply*=i
    return multiply
print(multiply_nums(2,4,3,4))


# In[63]:


def multiply_nums(num,*args):
    multiply = 1
    print(args)
    for i in args:
        multiply*=i
    return multiply
print(multiply_nums(2,4,3,4))


# # *Args as argument---> gather in tuple

# In[64]:


def multiply_nums(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply*=i
    return multiply
print(multiply_nums(2,3))


# In[65]:


nums = [2,3,4]
print(multiply_nums(nums))


# In[66]:


nums = [2,3,4]
print(multiply_nums(*nums)) # unpack and become tuple.


# Define a function 
# #input 
# #num, iterable (tuple,list)containing number as args.
# 
# example
# nums=[1,2,3]
# to_power(3,*nums)
# 
# output
# #list---> [1,8,27]
# 
# if user didn't pass any args then give a user a message 'hey you
# didn't pass args.
# 
# else 
# return
# 
# Note: Use list comprehension

# In[71]:


def to_power(num,*args):
    if args:
        return[i**num for i in args]
    else:
        return "You didnt pass any args"
nums=[1,2,3]
print(to_power(2,*nums))


# In[72]:


def to_power(num,*args):
    if args:
        return[i**num for i in args]
    else:
        return "You didnt pass any args"
nums=[1,2,3]
print(to_power(2))


# In[73]:


def to_power(num,*args):
    if args:
        return[i**num for i in args]
    else:
        return "You didnt pass any args"
nums=[1,2,3]
print(to_power(3,*[2,3]))


# In[68]:


# if list is empty or not.
l =[1,2,3]

if l:
    print('not empty')
else:
    print('empty')


# In[69]:


l =[]

if l:
    print('not empty')
else:
    print('empty')


# ## **Kwargs (Keyword arguments)

# In[75]:


# **Kwargs as an argument -- gather in dict

def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
func (first_name = 'Vasundhara', last_name ='Uniyal')


# In[77]:


# loop in dict

def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} :{v}")
        
func (first_name = 'Vasundhara', last_name ='Uniyal')


# In[78]:


def func(name,**kwargs):
    for k,v in kwargs.items():
        print(f"{k} :{v}")
        
func (first_name = 'Vasundhara', last_name ='Uniyal')


# In[79]:


def func(name,**kwargs):
    for k,v in kwargs.items():
        print(f"{k} :{v}")
        
func ('Teja',first_name = 'Vasundhara', last_name ='Uniyal')


# In[81]:


def func(name,**kwargs):
    for k,v in kwargs.items():
        print(f"{k} :{v}")
        
func ('Teja',first_name = 'Vasundhara', last_name ='Uniyal')

# Dictionary unpacking

d = {'name':'Vasundhara','age': 24}
func (**d)


# # Function with all type of parameters

# In[83]:


# default parameter
def func(name='unknown', age = 24):
    print(name,age)
func()


# In[84]:


def func(name='unknown', age = 24):
    print(name)
    print(age)
func('Teja')


# In[85]:


def func(name='unknown', age = 24):
    print(name)
    print(age)
func('Teja',25)


# In[86]:


# PADK
# parameters
# *args
# default parameters
# **kwargs


# In[87]:


def func(name,*args,last_name='unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func('Teja',1,2,3, a=1,b=2)


# In[88]:


def func(*args,name,last_name='unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func('Teja',1,2,3, a=1,b=2)


# In[ ]:


# when we use only parameter and default parameter


# In[91]:


#def func2(name,last_name='unknown')


# Define a function which takes input as a list and return a list.
# List should be reversed.
# 
# name['Vasu','Muskaan']
# 
# first letter should be capital

# In[95]:


def func_list(l,**kwargs):
    if kwargs.get('reverse_str')==True:
        return [name[::-1].title() for name in l]
    else:
        return[name.title()for name in l]
names = ['Vasu','Muskaan']
print(func_list(names))


# In[97]:


def func_list(l,**kwargs):
    if kwargs.get('reverse_str')==True:
        return [name[::-1].title() for name in l]
    else:
        return[name.title()for name in l]
names = ['Vasu','Muskaan']
print(func_list(names, reverse_str=True))


# # Lambda Expression
# It is a function which is defined in a single line.

# In[98]:


def add(a,b):
    return a+b

add2= lambda a,b: a+b
print(add2(2,3))


# In[ ]:


# Used with : built in,map,reduce,filter


# In[101]:


multiply = lambda a,b: a*b
print(multiply(2,3))


# In[104]:


print(add)
print(add2)
print(multiply)


# In[ ]:


# Lambda expression practice


# In[106]:


def is_even(a):
    return a%2==0 #a%2==0---> true,false
print(is_even(5))


# In[108]:


is_even2 = lambda a:a%2==0
print(is_even2(6))


# In[110]:


def last_char(s):
    returns[-1]
last_char = lambda s : s[-1]
print(last_char('vasundhara'))


# ## IF ELSE with Lambda

# In[111]:


def func(s):
    if len(s)>5:
        return True
    return False

func = lambda s: True if len(s)>5 else False
print(func('abc'))


# In[114]:


def func(s):
    return len(s)>5
    
func = lambda s: True if len(s)>5 else False
print(func('abcdefgh'))


# In[ ]:


# Enumerate Function : To track position of our item in iterable


# In[122]:


names = ['abc','abcdef','Vasu']
position = 0
for name in names:
    print(f"{position} ---> {name}")
    position +=1


# In[123]:


# With enumerate function
for pos,name in enumerate(names):
    print(f"{position} ---> {name}")


# Define a function that takes two arguments
# 1. list containing string 
# 2. string that want to find in your list
# and this function will return the index of string in your list and 
# if sting is not present then return -1

# In[125]:


def find_position(l,target):
    for position,name in enumerate (l):
        if name == target:
            return pos
    return -1

print(find_position(names,'abc'))


# # Map Function

# In[127]:


numbers = [1,2,3,4]
def square(a):
    return a**2
#[square(1),square(2),square(3)]

squares = list(map(square,numbers))
print(squares)


# In[128]:


squares = list(map(lambda a:a**2,numbers))
print(squares)


# In[130]:


# list comp

square_new = [i**2 for i in numbers]
print(square_new)


# In[131]:


new_list = []
for num in numbers:
    new_list.append(square(num))
    
print(new_list)


# In[135]:


names =['abc','abcd','abcde']
length = list(map(len,names))
for i in length:
    print(i)


# In[134]:


# for i in length:
#     print(i)


# In[136]:


print(length)


# # Filter Function()

# In[138]:


def is_even(a):
    return a%2==0

numbers = [3,4,2,1,5,6,9,8,10]

evens = tuple(filter(is_even, numbers))
print(evens)


# In[140]:


def is_even(a):
    return a%2==0

numbers = [3,4,2,1,5,6,9,8,10]

evens = filter(lambda a: a%2==0, numbers)

for i in evens:
    print(i)


# In[141]:


# for i in evens:
#     print(i)


# In[142]:


new_evens = [i for i in numbers if i%2==0]
print(new_evens)


# # Iterator vs Iterables

# In[144]:


numbers = [1,2,3,4] # tuples,strings---iterables
squares = map(lambda a:a**2,numbers) # iterator

print(squares)

for i in squares:
    print(i)


# In[145]:


numbers = [1,2,3,4] # tuples,strings---iterables
squares = map(lambda a:a**2,numbers) # iterator

for i in numbers:
    print(i)


# In[149]:


# step 1 : call iter function

number_iter = iter(numbers)
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))


# In[150]:


numbers = [1,2,3,4] 
squares = map(lambda a:a**2,numbers) 
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))


# # Zip function()

# In[151]:


user_id = ['user1','user2','user3']
names =['Harshit','mohit','rohit']

print(zip(user_id,names))


# In[153]:


print(list(zip(user_id,names)))


# In[154]:


user_id = ['user1','user2']
names =['Harshit','mohit','rohit']

print(list(zip(user_id,names)))


# In[156]:


user_id = ['user1','user2','user3']
names =['Harshit','mohit','rohit']

print(dict(zip(user_id,names)))


# In[157]:


user_id = ['user1','user2','user3']
names =['Harshit','mohit','rohit']
last_names = ['Uniyal','Bhatt','Dabral']
print(list(zip(user_id,names,last_names)))


# In[158]:


user_id = ['user1','user2','user3']
names =['Harshit','mohit','rohit']
last_names = ['Uniyal','Bhatt','Dabral']
print(dict(zip(user_id,names,last_names)))


# In[155]:


example = [('a',1),('b',2)]
print(dict(example))


# # Star operator with zip

# In[160]:


l1 = [1,3,5,7]
ls = [2,4,6,8]

l = [(1,2),(3,4),(5,6),(7,8)]
# * operator with zip

print(list(zip(*l)))


# In[164]:


l = [(1,2),(3,4),(5,6),(7,8)]
# * operator with zip

l1,l2 = list(zip(*l))
print(list(l1))
print(list(l2))


# In[165]:


l1 = [1,3,5,7]
ls = [2,4,6,8]
new_list =[]

for pair in zip(l1,l2):
    new_list.append(max(pair))
    
print(new_list)


# # Advance Function 1

# In[ ]:


# define a function that take any no of lists containing number
# [1,2,3],[4,5,6],[7,8,9]
# return average 
# (1+4+7)/3, (2,5,8)/3, (3,6,9)/3


# In[1]:


def average_finder(l1,l2):
    average = []
    for pair in zip(l1,l2):
        average.append(sum(pair)/len(pair))
    return average
print(average_finder([1,2,3],[4,5,6]))


# In[2]:


def average_finder(*args):
    average = []
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average
print(average_finder([1,2,3],[4,5,6], [7,8,9]))


# In[3]:


average_finder = lambda *args :[sum(pair)/len(pair) for pair in zip(*args)]

print(average_finder([1,2,3],[4,5,6], [7,8,9]))


# In[6]:


number1 = [2,3,6,8,10]
number2 = [1,2,3,4,5,6]
evens1 = []

for num in number1:
    if num%2==0:
        evens1.append(num%2==0)
        
print(evens1)


# In[7]:


print(all([True, True, True, True]))


# In[11]:


print(all([num%2==0 for num in number1]))


# In[9]:


[num%2==0 for num in number1]


# In[12]:


print(any([num%2==0 for num in number1]))


# # Any All Function

# In[16]:


def my_sum(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for num in args:
            total +=num
        return total
    else:
        return "Wrong Input"

print(my_sum(1,2,3,4,8,9))


# # Advance MIN and MAX fuction()

# In[17]:


names = ['Vasundhara','Muskaan','Teja']
print(max(names))


# In[22]:


def func(item):
    return len(item)
names = ['Vasundhara','Muskaan','Teja','z']
print(max(names, key = func))


# In[23]:


print(max(names, key = lambda item : len(item)))


# In[32]:


students ={
    'vasundhara':{'score':50, 'age': 24},
    'Muskaan':{'score':75, 'age': 19},
    'Teja':{'score': 76, 'age': 23}
}

students2 =[
    {'name':'vasundhara', 'score':90, 'age': 24},
    {'name':'Muskaan','score':75, 'age': 19},
    {'name':'Teja','score': 76, 'age': 25}
]


print(max(students2, key=lambda item:item.get('age'))['name'])


# In[34]:


print(max(students, key=lambda item: students[item]['age']))


# # Doc strings

# In[36]:


def add(a,b):
    return a+b

print(add.__doc__)


# In[37]:


print(len.__doc__)


# In[38]:


print(sum.__doc__)


# In[39]:


help(sum)

