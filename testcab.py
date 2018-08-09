'''generate random from 1000 to 9999

bull correct number with wrong position
cow correct number with correct position '''

import random as ra

a = ra.randint(1000, 9999)

print(a)

List1 = []
#List1 = ['7','2','1','2']
b = str(a)
itr_count=0
List1.extend(b)
while True:
    num = input("Enter the number:")
    itr_count=itr_count+1

    num_list = []
    b = str(num)
    num_list.extend(b)

    #print(num_list)
    i = 0

    cow_list = []
    bull_list = []
    j = 0
# Cow validation
    d=0
    e=0
    for x in List1:
        e=0
        for y in num_list:
            #print("x:",x)
            #print("y:",y)
            #print("List1.index(x)",d)
            #print("num_list.index(y)",e)
            #if List1.index(x) == num_list.index(y) and x == y:
            if d == e and x == y:
                j = j + 1
                #print("J:",j)
                cow_list.extend(x)
                e=e+1
                break
            e=e+1
        d=d+1


    print("Cow:", j)
    #print("Cow list:",cow_list)



# Bull Validation

    i = 0
#print("List1:",List1)
    for a in num_list:
        for b in List1:
            if a == b:
                i=i+1
                break

    len_bull_list = i
    len_cow_list = len(cow_list)
    if len_cow_list >= len_bull_list:
        len_bull_list1 = len_cow_list - len_bull_list
    else:
        len_bull_list1 = len_bull_list - len_cow_list

    print("Bull:", len_bull_list1)
    

    if len_cow_list==4:
        print("Congrats! you found the number:",str(num_list))
        print("Number of attempts you made:",itr_count)
        break





