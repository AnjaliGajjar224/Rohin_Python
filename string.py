"""
Sequence Data Types

1. Strings - immutable & ordered
2. Lists - mutable & ordered
3. Tuples - immutable & ordered
"""

# ch = 'a'
# print(type(ch))

# str1 = "hello Good Morning"
# str2 = 'Hey there'

# print(type(str1))
# print(type(str2))
# print(str1)
# print(str2)

"""
String is a sequence of characters
String is immutable and ordered.
"""
# s = "Python"

"""
    Positive Indexing   Negative Indexing
P           0               -5
y           1               -5
t           2               -4
h           3               -3
o           4               -2 
n           5               -1 
"""

# print("First character:", s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])
# # print(s[6])

# print("Last Character: ",s[-1])
# print(s[-2])
# print(s[-3])
# print(s[-4])
# print(s[-5])
# print(s[-6])
# print(s[-7])

# print("Length of the String: ",len(s))

"""
Take string as an input and take index as an input and print the character at that index.and also print the length of the string.
"""

"""
Slicing - Extracting a portion of the string

1) s[start:end]
2) s[start:]
3) s[:end]
4) s[:]
5) s[start:end:step]
"""

# my_str = "Royal_Technosoft_Pvt_Ltd"

# print("Length of the String: ", len(my_str))

# print("Original String: ", my_str)

# print("After Slicing: ")

# print(my_str[0:15])            # 0 - 14 (15th character not included)
# print(my_str[15])

# # print(my_str)

# print(my_str[5:20])

# print(my_str[:20])        # 0 - 19 (20th character not included)

# print(my_str[2:])        # 20 - end (21st character not included)
 
# print(my_str[:])

# print(my_str[-20:-10])       # -20 - -9 (10th character not included)

# print(my_str[:-5])        # -24 - -4 (5th character not included)

# print(my_str[-19:])     # -19 - -1 (20th character not included)

# print(my_str[1:20:1])

# print(my_str[1:20:2])

# print(my_str[::2])

# print(my_str[::5])

# print(my_str[-20:-5:3])

# print(my_str[-1:-15])
# print(my_str[20:1])

# print(my_str[-15:-1])
# print(my_str[-1:-15:-1])

# print(my_str[20:1:-1])

# print(my_str[::-1])
# print(my_str[::-2])

"""
1) Take string as an input and print the string in reverse order.
2) Take string as an input and take start,end and step as an input and print the subtring.
3) Take string as an input and check if it is a palindrome or not.
"""

my_str = "Python is a Programming Language"

print("Original String: ", my_str)
print("Length of the String: ", len(my_str))
print(my_str.capitalize())          # Capitalize the first character
print(my_str.casefold())            # Convert to lower case
print(my_str.count("o"))            # Count the number of occurrences of the character
print(my_str.center(52))            # Center the string

# 52 - len(my_str) = 52 - 32 = 20/2 = 10  = 10 spaces on both sides

print(my_str.center(52, "*"))
print(my_str.center(39, "#"))