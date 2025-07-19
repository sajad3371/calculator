while True :
    print("Choose number of the operator :\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Power\n6.Mod\nTell me here : ")
    operator = int(input())
    num_1 = float(input("Enter the first number : "))
    num_2 = float(input("Enter the second number : "))
    if operator == 1 :
        print(f"{num_1} + {num_2} = ",(num_1+num_2))
    elif operator == 2:
        print (f"{num_1} - {num_2} = ",(num_1-num_2))
    elif operator == 3:
        print (f"{num_1}  {num_2} = ",(num_1*num_2))
    elif operator == 4:
        print (f"{num_1} / {num_2} = ",(num_1/num_2))
    elif operator == 5:
        print (f"{num_1} to power of {num_2} = ",(num_1**num_2))
    elif operator == 6:
        print (f"{num_1} mod {num_2} = ",(num_1%num_2))
    else :
        print("The operator is not founded..!!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")