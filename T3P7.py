# Program written to find first non repeated element in the list
list1 = [9,4,9,7,6,4]

def nonRepeatElement(lInp,n):
    #looking for each element
    for i in range(n):
        j = 0
        while j<n:
            # checking if the elements are equal
            if i!=j and lInp[i] == lInp[j]:
                break;
            j += 1
        if j==n:
            return lInp[i]
    return -1
n = len(list1)
print(nonRepeatElement(list1,n))


