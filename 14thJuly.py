"""
Assignment Operators:

=     Assignment
+=    Add and assign(a += 5 ---> a = a + 5)
-=    Subtract and assign(a -= 5 ---> a = a - 5)
*=    Multiply and assign(a *= 5 ---> a = a * 5)
/=    Divide and assign(a /= 5 ---> a = a / 5)
%=    Modulus and assign(a %= 5 ---> a = a % 5)
//=   Floor division and assign(a //= 5 ---> a = a // 5)
**=   Exponent and assign(a **= 5 ---> a = a ** 5)
"""

# a = 10
# print(a)

# a += 5  # a = a + 5 --->  a = 10 + 5 = 15
# print(a) 

# a -= 6 # a = a - 6 --->  a = 15 - 6 = 9
# print(a)

"""
Bitwise Operators:

    &     Bitwise AND
    |     Bitwise OR
    ^     Bitwise XOR
    <<   Left shift
    >>   Right shift

Decimal to Binary Conversion:
45 - 101101

2 | 45
2 | 22 ----> 1
2 | 11 ----> 0
2 | 5  ----> 1
2 | 2  ----> 1
  | 1  ----> 0

Binary to Decimal Conversion:

Binary Number:  1        0      1       1     0      1         
                32      16      8       4     2      1 
                2^5    2^4     2^3    2^2    2^1    2^0

    32*1 + 16*0 + 8*1 + 4*1 + 2*0 + 1*1
  =  32  + 0 + 8 + 4 + 0 + 1
  =  45

43 - 101011

& - Bitwise AND

Truth Table
---------------
a   b   a&b
0   0    0
0   1    0
1   0    0
1   1    1


45  - 1  0  1  1  0  1
&     &  &  &  &  &  &
43  - 1  0  1  0  1  1
----------------------------
      1  0  1  0  0  1 (41)
"""
# print(45&43)
"""
| - Bitwise OR

Truth Table
---------------
a   b   a|b
0   0    0
0   1    1
1   0    1
1   1    1


45  - 1  0  1  1  0  1
|     |  |  |  |  |  |
43  - 1  0  1  0  1  1
----------------------------
      1  0  1  1  1  1
"""
# print(45|43)

"""
^ - Bitwise XOR

Truth Table
----------------------
a   b   a^b
0   0    0
0   1    1
1   0    1
1   1    0

45  - 1  0  1  1  0  1
^     ^  ^  ^  ^  ^  ^
43  - 1  0  1  0  1  1
----------------------------
      0  0  0  1  1  0 (6)
"""
# print(45^43)
"""
Shift Operators

    <<   Left shift
    >>   Right shift

1) Right Shift:

45 - 101101
45>>2 

45    1   0   1  1  0  1 
      32  16  8  4  2  1
45>>1     1   0  1  1  0      
45>>2         1  0  1  1  
"""
# print(45>>2)
"""
2) Left Shift:

45 - 101101
45<<3

45                         1   0  1  1  0  1  
      512   256  128  64  32  16  8  4  2  1
45<<1                 1   0   1   1  0  1  0 
45<<2            1    0   1   1   0  1  0  0  
45<<3        1    0   1   1   0   1  0  0  0
"""
# print(45<<3)

"""
Logical Operators:
1) and
2) or
3) not
"""
# print(15>10 and 10>18)           # True and False = False
# print(15>10 and 10>8)            # True and True = True

# print(15>10 or 10>18)            # True or False = True
# print(15>10 or 10>8)             # True or True = True

# print(not(15>10))             # not True = False
# print(not(15>18))             # not False = True

"""
Membership Operators:
1) in
2) not in
"""

# print('b' in 'banana')            # True
# print('k' in 'banana')            # False

# print('b' not in 'banana')        # False
# print('k' not in 'banana')        # True

# my_str = input("Enter a string: ")
# my_char = input("Enter a character: ")

# if my_char in my_str:
#     print("Character is present in the string")
# else:
#     print("Character is not present in the string")

"""
Identity Operators:
1) is
2) is not
# """
# a = 15
# b = 15
# c = 10

# print(id(a))
# print(id(b))
# print(id(c))


# print(a is b)
# print(a is c)

# print(a is not b)
# print(a is not c)