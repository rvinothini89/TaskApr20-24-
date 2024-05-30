#Program to find triplet which give sum as 59 
List1 = [10,20,30,9]
def findTriplets(A,size,value):
    #For setting first element as A[i]
    for i in range(0,size-2):
        #For setting second element as A[j]
        for j in range(0,size-1):
            #For setting third element as A[k]
            for k in range(0,size):
                if A[i]+A[j]+A[k] == value:
                    print("The triplet is:",A[i],",",A[j],",",A[k])
                    return True
    return False
ListSize = len(List1)
findTriplets(List1,ListSize,59)
    