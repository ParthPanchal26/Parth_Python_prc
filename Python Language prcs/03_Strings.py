
# In python, Strings are immutable so we can not actually modify original string
# Instead every string methods returns new string.
# Any string method does not modify actual string

mySting = "This is a string!"

print("\nOriginal String: " + mySting)
print("\nIn uppercase: " + mySting.upper())
print("In lowercase: " + mySting.lower())
print("\nIndex of letter \'a\' in sting is: ", mySting.find('a'))
print("Index of letter \'w\' in sting is: ", mySting.find('w')) # -1, because did not exist
print("Index of word \"string\" in string is: ", mySting.find('string'))
print("\nNew string is: ", mySting.replace('a', '\'the\''))
print("\nThe string contains word \'the\': ", 'the' in mySting)

