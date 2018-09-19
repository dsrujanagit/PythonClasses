#Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. 
#Lists might contain items of different types, but usually the items all have the same type.

squares = [1, 4, 9, 16, 25]
squares

#SLICING
#Like strings (and all other built-in sequence type), lists can be indexed and sliced:

squares[0]  # indexing returns the item
squares[-3:]  # slicing returns a new list

#All slice operations return a new list containing the requested elements. This means that the following slice returns a new (shallow) copy of the list:

squares[:]
squares + [36, 49, 64, 81, 100]

#Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:

word = 'python'
word[1]='c'  # Will not work

cubes = [1, 8, 27, 65, 125]  # something's wrong here
cubes[3] = 64  # replace the wrong value
cubes

#APPEND
#You can also add new items at the end of the list, by using the append() method (we will see more about methods later):

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes

We can add one item to a list using append() method or add several items using extend() method.

odd = [1, 3, 5]
odd.append(7)
print(odd)

#EXTEND
odd.extend([9, 11, 13])
print(odd)

Furthermore, we can insert one item at a desired location by using the method insert() or insert multiple items by squeezing it into an empty slice of a list.

#INSERT
odd = [1, 9]
odd.insert(1,3)
odd
odd.insert(0,99)
odd

#JUST OVERWRITE. name[INDEX:NUM OF ELEMENTS TO REPLACE]
odd[2:2] = [5, 7]
odd
letters[2:5] = ['C', 'D', 'E']
letters
letters[2:5] = []
letters

# clear the list by replacing all the elements with an empty list
letters[:] = []
letters


Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
a in letters
'a' in letters

a = [5, 10, 15, 20]
10 in a

if ('b' in letters):
    print('Yes I see it')
else:
    print('No I dont')
   

print('c' not in my_list)

for singleletter in letters:
    print (singleletter)
    

for fruit in ['apple','banana','mango']:
    print("I like",fruit)
    
    
#The built-in function len() also applies to lists:
letters = ['a', 'b', 'c', 'd']
len(letters)




#NESTED LISTS
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
x[0]
x[0][1]
'b'

# list with mixed datatypes
my_list = [1, "Hello", 3.4]
my_list2 = ["mouse", [8, 4, 6], ['a']]
my_list3 = my_list + my_list2
my_list3

#DELETING
del my_list3[3]
my_list3

del my_list3[3][2]
my_list3

#REMOVE
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

print(my_list)







# Output: 'o'
print(my_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'm'
print(my_list.pop())

# Output: ['r', 'b', 'l', 'e']
print(my_list)

my_list.clear()

# Output: []
print(my_list)

>>> my_list = ['p','r','o','b','l','e','m']
>>> my_list[2:3] = []
>>> my_list
['p', 'r', 'b', 'l', 'e', 'm']
>>> my_list[2:5] = []
>>> my_list
['p', 'r', 'm']


my_list = [3, 8, 1, 6, 0, 8, 4]

# Output: 1
print(my_list.index(8))

# Output: 2
print(my_list.count(8))

my_list.sort()

# Output: [0, 1, 3, 4, 6, 8, 8]
print(my_list)

my_list.reverse()

# Output: [8, 8, 6, 4, 3, 1, 0]
print(my_list)



pow2 = [2 ** x for x in range(10)]

# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)


pow2 = []
for x in range(10):
   pow2.append(2 ** x)
   


>>> pow2 = [2 ** x for x in range(10) if x > 5]
>>> pow2
[64, 128, 256, 512]
>>> odd = [x for x in range(20) if x % 2 == 1]
>>> odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> [x+y for x in ['Python ','C '] for y in ['Language','Programming']]
['Python Language', 'Python Programming', 'C Language', 'C Programming']




append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list




all()	Return True if all elements of the list are true (or if the list is empty).
any()	Return True if any element of the list is true. If the list is empty, return False.
enumerate()	Return an enumerate object. It contains the index and value of all the items of list as a tuple.
len()	Return the length (the number of items) in the list.
list()	Convert an iterable (tuple, string, set, dictionary) to a list.
max()	Return the largest item in the list.
min()	Return the smallest item in the list
sorted()	Return a new sorted list (does not sort the list itself).
sum()	Return the sum of all elements in the list.


