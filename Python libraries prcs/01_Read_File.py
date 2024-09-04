#   open("fileName", "mode", "buffering")
#   'made' that determined to read ot write file
#       'r': read file
#       'rb': read only binary format
#       'w': write file
#       'wb' write only binary format
from fileinput import isfirstline

#   'buffering' that determined how many line to be buffered!
#       can be 0 or more

fileObject =  open("01_ReadFile.txt")

# ... read entire file as it is
# print(fileObject.read())

# ... returns list of lines from the file
# print(fileObject.readlines())

# ... Iterating over file
# for i in fileObject.readlines():
#     print(i)

'''
# ... Using 'with' keyword for opening file because if in case wrong file name or may be
# ... file is removed or deleted then to handle exception '''
# with open("./01_ReadFile.txt") as f:
#     data = f.read()
#     print(data)

'''
    ->  Writing file in py using write(), here we will use 'a' as mode.
    ->  'a' mode will append at the end.
    ->  'w' mode will overwrite entire file!
'''

# with open("01_ReadFile.txt", 'a') as f:
#     f.write(', {\n\t"contentType": "JSON credentials!"\n}')
# print(fileObject.read())

'''
    ->  Reading CSV file, CSV file is a comma-separated values file that uses comma to 
        separate values.
    ->  Each line is a data record, Each record consist of many fields, separated by commas.
'''

with open("01_randomized_data.csv") as f:
    rows = f.readlines()
    isFirstLine = True
    for r in rows:
        if isFirstLine:
            isFirstLine = False
            continue
        cols = r.split(',')
        print('\n\t_ID:\t', cols[0], end=' ')
        print('\n\tname:\t', cols[1], end=' ')
        print('\n\tage:\t', cols[2], end=' ')
        print('\n\tcity:\t', cols[3], end=' ')