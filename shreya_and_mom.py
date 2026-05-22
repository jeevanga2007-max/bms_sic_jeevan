import random
def earnings(total_no_of_shoes,number_of_shoes_can_carry):
    prices_of_shoes = []
    for i in range(total_no_of_shoes):
        prices_of_shoes.append(random.randint(-100, 100))
    flag = 0
    sum=0
    prices_of_shoes.sort()
    print("Prices of shoes are: ", prices_of_shoes)
    
    for i in prices_of_shoes:
        if i<0 and flag<number_of_shoes_can_carry: 
            flag+=1
            sum+=i
    return(abs(sum))

total_no_of_shoes = int(input("Enter total number of shoes: "))
number_of_shoes_can_carry = int(input("Enter number of shoes that can be carried: "))
print("Earnings  is: ", earnings(total_no_of_shoes, number_of_shoes_can_carry)) 