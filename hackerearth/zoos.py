'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

word = input()
x = 0
y = 0
for letter in word:
    if letter == 'z':
        x += 1
    if letter == 'o':
        y += 1

print(x)
print(y)
if 2 * x == y:
    print('Yes')
else:
    print('No')
