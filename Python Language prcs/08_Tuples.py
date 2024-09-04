print("\n")

'''
    ->  Tuples are defined using parenthesis
    ->  Tuples are used to store sequence of objects.
    ->  Tuples are immutable means once we declare it we can not change it.
    ->  We only have the count and index methods with tuples.
    ->  The count method counts total occurrence of element inside tuple. 
    ->  The index method return first occurrence index of element inside
        tuple.   
'''

numbers = (1, 2, 3, 3, 2, 2, 4, 5)
print("The element \'2\' occurs total \'" + str(numbers.count(2)) + "\' times")
print("\nFirst occurrence of element \'2\' is at index \'" + str(numbers.index(2)) + "\'")