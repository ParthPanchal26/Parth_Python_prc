#         0  -5      1  -4      2  -3      3  -2      4  -1
names = ['Parth', 'Anamika', 'hSivani', 'Vaidehi', 'Sandip']
print('\n')
print(names)

'''
    ->  We can retrieve elements from list using index, similar to traditional arrays.
    ->  We can also use a negative index that will retrieve 
        elements from the end of list
    ->  In the given example, we can see that the last element is 'sandip'
        and we can easily retrieve it using index -1.
    ->  Similarly, we can retrieve second last element using -2, then -3, and so on. 
'''
print('\n')
print("Element at names[0]: " + names[0])
print("Element at names[1]: " + names[1])
print("Element at names[-1]: " + names[-1])
print('\n')

'''
    ->  Now suppose you have made mistake while declaring into list and you want to update it,
        we can do it by assigning new value to the element to be update.
    ->  In given example, You can see the 3rd element is declared as 'hSivani' and it should be
        corrected as 'Shivani'.
    ->  Now, we can treat the element as a variable and assign new value to it, just pick its
        index and assign correct value!
'''

names[2] = 'Shivani'
print("Element at names[2]: " + names[2])
print('\n')

print("names: " + str(names))
print('\n')

'''
    ->  Now if you want to only iterate some elements, lets say till some range.
    ->  We can specify starting index and range index.
    ->  For example, names [0 : 3]
        Here we will retrieve values from including 0th index to excluding 3rd index
    ->  The output will be 'Parth', 'Anamika' and 'Shivani'.
    ->  But this always return a new list! and don't modifies original list!
'''

print("New list: " + str(names[0: 3]))
print('\n')

numbers = [1, 2, 4, 5]
print('\nnumbers: ' + str(numbers))

# To append new value to list we have append method
numbers.append(6)
print("\nAfter appending 6: " + str(numbers))

# To insert new value somewhere in middle of list we have insert method
numbers.insert(2, 3)
print("\nAfter inserting 3: " + str(numbers))

# We can directly remove an element by specifying it inside remove method
numbers.remove(6)
print("\nAfter removing 6: " + str(numbers))

# To clear the list we have clear method
numbers.clear()
print("\nAfter clearing list: " + str(numbers))

# To check, weather the elements exists in list or not?, then we have in operator
print("\n\'5\' exists in list? " + str(5 in numbers)) # will return boolean

# We can find length of list using len method
print("\nLength of list is: " + str(len(numbers)))