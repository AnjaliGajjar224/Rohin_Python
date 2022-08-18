"""
List :
------
    - List is a collection which is ordered and changeable(mutable). Allows duplicate members.
    - List can be written as [item1, item2, item3, ...]
    - List is a mutable sequence of elements.
    - List is a sequence of elements.
    - List allows Multiple data types.
"""

# Create a list

# list1 = [1, 2, 3, 4, 5]
# """
# index : 0 1 2 3 4
# value : 1 2 3 4 5
# negative index : -1 -2 -3 -4 -5
# value :           5  4  3  2  1
# """
# print("Type of list1: ", type(list1))
# print("List1: ", list1)

# # Access list items
# print("list1[0]: ", list1[0])
# print("list1[1]: ", list1[1])
# print("list1[-1]: ", list1[-1])
# print("list1[-2]: ",list1[-2])

# # Change list items
# list1[0] = "one"
# print(list1)

# list2 = ["Royal",12,32.45,2+5j]
# print(list2)

# # Get the length of list
# print("Length of list1: ", len(list1))

# myList = [1,2,53,4,15,6,87,8,9,10]

# #slicing

# print("myList[0:5]: ", myList[0:5])

# print("Max value in myList: ", max(myList))
# print("Min value in myList: ", min(myList))
# print("Sum of myList: ", sum(myList))
# print("Sorted myList: ", sorted(myList))            # sorted() returns a new sorted list.It returns Ascending order
# print("Reverse sorted myList: ", sorted(myList, reverse=True))          # reverse=True returns Descending order


# my_list = ["Apple","Banana","Cherry","apple","mango","zero","Airplane"," "]

# print("my_list: ", my_list)
# print("Max value in my_list: ", max(my_list))
# print("Min value in my_list: ", min(my_list))
# # print("Sum of my_list: ", sum(my_list))      # TypeError: sum() can't sum mixed types
# print("Sorted my_list: ", sorted(my_list))            # sorted() returns a new sorted list.It returns Ascending order
# print("Reverse sorted my_list: ", sorted(my_list, reverse=True))          # reverse=True returns Descending order

# List Methods

l = [12,13,54,21,12,45,32,67,89,10]
print("Length of l: ", len(l))


l.append(12)                      # append() : Add an element to the end of the list
print("l after append: ", l)

l3 = l.copy()                                              # copy() : Return a copy of the list
print("l3: ", l3)

l2 = l 
print("l2: ", l2)

print("id of l: ", id(l))
print("id of l2: ", id(l2))
print("id of l3: ", id(l3))

print(l is l2)                # is : Return True if both the objects are same
print(l is l3)

l3.clear()                 # clear() : Remove all the elements from the list
print("l3: ", l3)   

del l3                  # del : Delete the list
# print("l3: ", l3)

print(l.count(12))                 # count() : Return the number of times a specified value occurs in the list

list1 = [43,21,56,87,90]
l.extend(list1)                 # extend() : Add the contents of another list to the end of the current list
print("l: ", l)

print(l.index(12))                 # index() : Return the index of the first occurrence of the value


l.insert(1, "Hello")             # insert() : Insert an item at the specified position
print("l: ", l)

print(l.pop(1))                          # pop() : Remove the item at the specified position
print(l)

l.remove(12)                             # remove() : Remove the first item with the specified value
print(l)

l.reverse()                              # reverse() : Reverse the order of the list
print(l)

print(l[::-1])                                  # [::-1] : Reverse the order of the list

l.sort()                                  # sort() : Sort the list
print(l)

l.sort(reverse=True)                     # sort() : Sort the list in reverse order
print(l)

"""
list programs
    1. add 5 numbers into the list and print the list
    2. add 10 numbers into the list, reverse that list, store the list into another list and print the list
    3. add 10 numbers into the list, sort that list and print the list
    4. add 10 numbers into the list, remove the duplicates and print the list
    5. add 10 numbers into the list, print the maximum and minimum number from the list
    6. add 10 numbers into the list, print the average of the list
    7. add 10 numbers into the list, print the sum of the list
    8. scan 5 numbers from the user and store it into the list, check if both the lists are same or not
    9. Take 10 exotic fruit list and check whether the fruit given by user is present in the list or not
"""

