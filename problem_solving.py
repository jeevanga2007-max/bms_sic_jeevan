def permut(l1, l2):

    l1_dict = {}
    l2_dict = {}

    missing_numbers = []

   
    for i in l1:
        if i in l1_dict:
            l1_dict[i] += 1
        else:
            l1_dict[i] = 1

   
    for i in l2:
        if i in l2_dict:
            l2_dict[i] += 1
        else:
            l2_dict[i] = 1

   
    for i in l2_dict:

        if l2_dict[i] != l1_dict.get(i, 0):
            missing_numbers.append(i)

    return sorted(missing_numbers)


l1 = [int(i) for i in input("Enter first list: ").split()]
l2 = [int(i) for i in input("Enter second list: ").split()]

print(permut(l1, l2))