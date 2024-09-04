print('\n')
numbers = [1, 2, 3, 4, 5, 6]
print("numbers: ")
for item in numbers:
    print(item)

'''
    ->  Python for loop is little more different then other languages loops.
    ->  Here, item is variable that gonna assign in every iteration.
    ->  Here, we not need to declare a new variable, condition increment operation,
        not need to find length of list.
'''


'''
    => Range():
    ->  In python we have a range function.
    ->  We use range function to generate sequence of numbers.
    ->  This is a built-in function just like print and input functions.
        
        print(range(5))
        output: range(0, 5)
        
    ->  Here we can pass value for example a number 5.
    ->  It will return a range object, that will store a sequence of numbers.
    ->  Its not actual numbers because its the default representation of range object.
    ->  We need to iterate over this range object using a for loop.
    
        print(range(5, 10))
        output: range(5, 10)
        
    ->  This will generate range from including 5 to excluding 10.
    ->  So when we will iterate over this object, it will print numbers from 5 to 9.
'''

nums = range(5)
print("\nNumbers in range of 5: ")
for num in nums:
    print(num)

nums = range(5, 10)
print("\nNumbers in range from 5 to 10")
for num in nums:
    print(num)

'''
    ->  Well we can even pass 3rd parameter that is step.
    ->  Means we want to jump two numbers at a time.
'''

nums = range(5, 10, 2)
print("\nNumbers in range from 5 to 10 by skipping 2 at a time: ")
for num in nums:
    print(num)
