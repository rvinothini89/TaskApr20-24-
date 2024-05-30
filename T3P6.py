#Program to find duplicates in 3 lists
List1 = [2,3,4,5,6]
List2 = [3,4,5,6,7]
List3 = [5,6,7,8,9]
def dupe_list(l1,l2,l3):
    result = []
    for i in l1:
        if i in l2 and i in l3:
            result.append(i)
    print(list(set(result)))
dupe_list(List1,List2,List3)