#Program to find prime number in a list
list1 = [10,501,22,37,100,999,87,351]
prime_list =[]
def PrimeOrNot(lst):    
    for num in lst:
        # if the number is 0 or 1 its not prime, so its getting skipped
        if num == 0 or num == 1:
            continue
        # here number will be divided from 2 to half of the number. 
        for i in range(2, int(num//2)+1):
                if num%i == 0:
                    break
#if the number is not satisfying any of above conditions, then its prime. It will be added to prime list
        else:
            prime_list.append(num)
    return prime_list
prime_list = PrimeOrNot(list1)
print("The count of prime numbers is:", len(prime_list))
print("The prime numbers are:",prime_list)