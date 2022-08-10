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

# my_str = "Python is a Programming Language"

# print("Original String: ", my_str)
# print("Length of the String: ", len(my_str))
# print(my_str.capitalize())          # Capitalize the first character
# print(my_str.casefold())            # Convert to lower case
# print(my_str.count("o"))            # Count the number of occurrences of the character
# print(my_str.center(52))            # Center the string

# # 52 - len(my_str) = 52 - 32 = 20/2 = 10  = 10 spaces on both sides

# print(my_str.center(52, "*"))
# print(my_str.center(39, "#"))
# my_str = "Python is a Programming Language"

# print(my_str.encode())         # Encode the string by default UTF-8
# print(my_str.encode("greek"))

# print(my_str.endswith("Language"))        # Returns True if the string ends with the given argument
# print(my_str.endswith("e"))

# print(my_str.endswith("e", 0, 20))

# print("Hello\tWorld".expandtabs(20))

# print(my_str.find("o"))        # Find the first occurrence of the character
# print(my_str.find("o", 5))

# print(my_str.rfind("o"))        # Find the last occurrence of the character

# num1 = 15
# num2 = 10

# add = num1 + num2

# print(num1,"+",num2,"=",add)
# print(f"{num1} + {num2} = {add}")

# # print("My name is {name}. My age is {age}".format(age = int(input("Enter your age:")),name = input("Enter your name:")))

# print(my_str.index("o"))  # Find the first occurence of the character
# print(my_str.index("o",5))
# print(my_str.rindex("o"))

# print(my_str.find("b"))    # Returns -1 if string not found
# print(my_str.index("b"))   # Raise an error if string not found

"""
Task 1:
---------
Input:
fullname: Anjali Rakeshbhai Gajjar

Output:
A.R.Gajjar

Task 2:
----------
Write a program that count the number of vowels, consonents and white spaces in String.
Input:

Python Programming

Output:

vowel : 4
white spaces : 1
consonents : 13
"""
# print("ABC132".isalnum())              #Returns true if String contains alphabets or numeric
# print("ABCD".isalnum())
# print("1234".isalnum())
# print("!@ABC12&".isalnum())

# print("ABCD".isalpha())              # Returns True if String contains only alphabets

"""
isdecimal
isdigit
isnumeric
"""

# s5 = "2022"
# print(s5.isdecimal())   # considers strictly plain digits from 0 to 9 only, nothing else
# print(s5.isdigit())     # considers subscripts, superscripts and circled numbers also as numbers
# print(s5.isnumeric())   # considers vulgar fractions, roman numerals, numbers from other languages

# s6 = "2⁸"
# print(s6)
# print(s6.isdecimal())
# print(s6.isdigit())
# print(s6.isnumeric())

# s7 = "②⓪②②"
# print(s7)
# print(s7.isdecimal())
# print(s7.isdigit())
# print(s7.isnumeric())

# s8 = "¼"
# print(s8)
# print(s8.isdecimal())
# print(s8.isdigit())
# print(s8.isnumeric())

# s9 = "二千二十二"
# print(s9)
# print(s9.isdecimal())
# print(s9.isdigit())
# print(s9.isnumeric())

# s10 = "VI"   
# s11 = "Ⅵ"
# print(s10)
# print(s10.isnumeric())
# print(s11)
# print(s11.isnumeric())

# print("Python123".isascii())
# print("num1".isidentifier())           # True
# print("num 1".isidentifier())
# print("1Num".isidentifier())
# print("&num".isidentifier())

# print("python".islower())          # Returns True if string contains only lower case 
# print("PYTHON".isupper())
# print("Python Is A Programming Language".istitle())

# print("PYTHON".lower())
# print("python".upper())
# print("python is a programming language".title())


# print("Are you #1?".isprintable())
# print("Are you \n#1?".isprintable())

# print("            hey         ".isspace())
# print("        ".isspace())
# print("\t".isspace())
# print("\n".isspace())

# s1 = "Hello!Good Evening"
# s2 = "Nice"

# print(s1.join(s2))

# s = "Hello"

# print(s.ljust(10))
# print(s.ljust(10,"*"))

# print(s.rjust(10))
# print(s.rjust(10,"*"))

# print("               hey".lstrip())
# print("hey              ".rstrip())

# print("$$$$$$$$$$$hey".lstrip("$"))
# print("hello$$$$$$$$$$$$".rstrip("$"))
# print("$$$$$$$$$$$hello$$$$$$$$$$$$$".strip("$"))

# print("Good_Evening_How_are_you?".partition("_"))
# print("Good_evening_Hey".rpartition("_"))

# print("Good Evening".replace(" ","_"))

# print("Good_Evening_How_are_you?".split("_",2))
# print("Good_Evening_How_are_you?".rsplit("_",2))

# print("Good\nEvening\nHow\nAre\nYou?".splitlines())
# print("Good EveninG".swapcase())

# print("Hello".zfill(10))

# d = "9-08-2022"

# print(d.zfill(10))