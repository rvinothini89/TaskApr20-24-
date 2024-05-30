#Program to find odd, even numbers from the list 
list1 =[10,501,22,37,100,999,87,351]
even_list=[]
odd_list=[]
# if number divisible by 2, adding it to even list. Else adding it to odd list
for x in list1:
    if x%2==0:
        even_list.append(x)
    else:
        odd_list.append(x)
print("Odd list is:",odd_list)
print("Even list is:",even_list)