
while True :

    num_1 = float (input("Please enter the firt number : "))
    oprator = str(input("Please enter the oprator : "))
    num_2 = float (input("Please enter the second number : "))
    if oprator == '+':
        print (f"{num_1} + {num_2} = ",(num_1+num_2))
    elif oprator == '-':
        print (f"{num_1} - {num_2} = ",(num_1-num_2))
    elif oprator == '*':
        print (f"{num_1}  {num_2} = ",(num_1*num_2))
    elif oprator == '/':
        print (f"{num_1} / {num_2} = ",(num_1/num_2))
    elif oprator == '**':
        print (f"{num_1} power {num_2} = ",(num_1**num_2))
    elif oprator == '%':
        print (f"{num_1} % {num_2} = ",(num_1%num_2))
    else :
        print("The operator is not founded..!!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
