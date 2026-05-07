import pdb
pdb.set_trace()
input_number= int(input("Enter a number to find your lucky digit: "))

sum_of_digits=0
while input_number != 0:
    digit = input_number % 10
    sum_of_digits += digit
    input_number //= 10
    if sum_of_digits > 9 and input_number == 0:
        input_number = sum_of_digits
        sum_of_digits = 0

print("The sum of digits is:", sum_of_digits)