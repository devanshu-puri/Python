'''
f = open('test.txt', 'r')

print(f.name)

f.close() # require to close the file '''

# Using context manager (no close is required)

"""
with open('test.txt', 'r') as f:
    f_contents = f.read() 
    # or f.readlines() convert into element every line
    # f.readline() print line by line everytime but gives extra new line to avoid : print(f_contents,end='')

    # iterate : prints line by line in one go
    ''' for line in f:
            print(line, end='')'''

    # f_contents = f.read(100) reads only first 100 character
    # better way : size_to_read = 100
    # f_contents = f.read(size_to_read)
    print(f_contents, end='')

"""

'''
#loop of these content

with open('test.txt', 'r') as f:
    size_to_read = 10
    contents = f.read(size_to_read)

    while len(contents) > 0:
        print(contents, end='*') * will tell us when loop part ended
        content = f.read(size_to_read)

'''

# what if we want the iterator range text to start at beginning

'''

with open('test.txt', 'r') as f:
    size_to_read = 10

    contents = f.read(size_to_read)
    print(contetns, end='')

    f.seek(0) the next 10 character will get added in beginning

    contents = f.read(size_to_read)
    print(contents)

    

'''

# ================== WRITE ===========================

'''
with open('test2.txt' , 'w') as f:
    f.write('Test')  # if file dont exist it creates it
    f.seek(0) 
    f.write('Test2') # this overrote the existing word at 0
    # if f.write('R') then it will beocme Rest in main file 
'''

with open('test.txt', 'r') as rf: 
    with open('test_copy.txt', 'w') as wf: # copy test content to this file
        for line in rf:
            wf.write(line)
    