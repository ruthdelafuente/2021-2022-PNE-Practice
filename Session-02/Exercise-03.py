#Write a function called fibosum(n) that calculates the sum of the n first fibonacci terms.
# The main program should call this function twices, with the arguments n=5 and n=10

def fibosum(n):
    n1 = 0
    n2 = 1
    sum = 1
    for i in range(2, n + 1):
        num = n1 + n2
        n1 = n2
        n2 = num
        sum += num
    return sum

print("The sum of the first 5 numbers is:", fibosum(5))
print("The sum of the first 10 numbers is:", fibosum(10))

