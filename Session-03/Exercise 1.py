# fibonacci series
# a constant is a value that doesn´t change
N = 11 #a normal variable
n1 = 0
n2 = 1
print(n1, end= " ")
print(n2, end= " ")
for i in range(2, N): # we already have 2 numbers and we want to print 11
    num = n1 + n2
    print(num, end= " ")
    n1 = n2
    n2 = num
print()