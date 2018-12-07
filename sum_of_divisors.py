def divisors(num):
    divisor_list = []
    for i in range(1,num+1):
        if num % i == 0:
            divisor_list.append(i)
    return divisor_list

def sum_of_divisors(num):
    
    divisors_list = divisors(num)
    return sum(divisors_list)

def num_of_divisors(num):
    divisors_list = divisors(num)
    return len(divisors_list)

def totatives(num):
    totatives_list = []
    divisors_list = divisors(num)[1:] 

    for element in range(1,num):
        check = False
        for i in divisors_list:
            if check == False:
                if element % i == 0:
                    check = True
        if check == False:
            totatives_list.append(element)
    
    return totatives_list

def totient(num):
    return len(totatives(num))
            
       
       


print(divisors(60))
print(sum_of_divisors(60))
print(num_of_divisors(60))
print(totatives(60))
print(totient(60))