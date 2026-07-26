# String & numeric values can operate together with *.
A,B = 2 , 3
Txt = "@"
print(2*Txt*3)

#String & String can operate with *.

A,B = "2", 3
Txt = "@"
print((A+Txt)*B)

# Numeric values can operate with all arithmetic operators
A,B = 2,3
C = 4
print(A+B*C)

# Arithmetic expression with integer and float will result in float value.
A,B = 2,3.0
C = A + B
print(C)

# integer division with float and int will give int displayed as float value.
A,B = 5.0,2
C = A//B
print(C)