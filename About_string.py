
# All are valid string declaration.

str = "Hello World"
str1 = 'Hello World!'
str2 = """Hello World@"""
print(str)
print(str1)
print(str2)

# count the string length using len() function.
str3 = '''Hello World'''
len1 = len(str)
print("length of String:",len1)

# concatenate two strings using + operator.
str4 = "Hello"
str5 = "World"
print("Show Concatenation of Two Strings:", str4 + " " + str5)

# Slicing of string using index.
str6 = "Hello World"
print("Sliced String:", str6[1:4])
print("string Sliced:", str6[:4])
print("string sliced:", str6[2:])

# All String Functions.

str7 = "hello Everyone I am Coder"

# returns True if the string ends with the specified value, otherwise False.
print(str7.endswith("er"))   
# returns true if the string starts with the specified value, otherwise false.
print(str7.startswith("Hela"))
# Capitalizes the first character of the string.
# returns a string with the first character capitalized and the rest lowercased.
print(str7.capitalize())
# replace all occurrences of a specified phrase with another specified phrase.
print(str7.replace("hello", "Hi"))
# returns the index of the first occurrence of the specified value.
print(str7.find("Everyone"))
# returns the occurrences of substring in the string.
print(str7.count("e"))

