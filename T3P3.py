#Program to find happy number in a list
list1 = [10,501,22,37,100,999,87,351]
Happy_List = []
def checkHappy(a):
    for i in range (len(a)):
        sum = a[i]
        while sum!=1 and sum !=4:
            tempsum = 0
            for digit in str(sum):
                tempsum += int(digit) ** 2   
            sum = tempsum
        if sum == 1:
            Happy_List.append(a[i])
    return Happy_List
print(checkHappy(list1))
