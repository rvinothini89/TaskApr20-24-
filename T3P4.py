#Program to find sum of digits
def getSum(n):
    sum = 0
#here converting integer to string, so that it can be traversed as a list
    for x in str(n):
#here converting string to integer and adding the digits
        sum += int(x)
    return sum
num = input("Enter number:")
print(getSum(num))