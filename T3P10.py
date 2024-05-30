#Program to find if any of sublists return the value of 0
List1 = [4,2,-3,1,6]
def subList(lst,listLen):
    # traversing through the list to get the subelements and sum of the sub elements
    for i in range(listLen-1):
        sum = lst[i]
        for j in range(i+1,listLen):
            sum += lst[j]
            if sum == 0 :
                print("There is a sublist which returns 0")
    return False
ListLength = len(List1)
subList(List1,ListLength)