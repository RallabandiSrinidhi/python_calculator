def calculator(operation,n1,n2):
    if operation == "+":
        return n1+n2
    elif operation == "-":
        return n1 - n2  
    elif operation == "/":
        if n2!= 0:
            return n1 / n2
        else:
            return "division with zero is not valid"
    elif operation == "*":
        return n1*n2
    elif operation == "sq":
        return n1**2
    elif operation == "sqrt":
        if n1>= 0 :
            return n1**(0.5)
        else:
            return "root of negative number doesnt exist"
    elif operation == "%":
        if n2!= 0:
            n1 = int(n1)
            n2 = int(n2)
            return(n1)%(n2)
        else:
            return 'division with zero is not valid'
    

print('\n\n\nwelcome to calculator\n')
while True:
    try:
        operation = input("choose the input:\nexit to exit the calculator \n+ for addition \n- for subtraction \n* for multiplication \n/ for division " 
            "\nsq for square \nsqrt for square root \n'%' for remainder after division \ngive operation:").strip().lower()
        if operation == "exit":
            print("thanks for using \n have a nice day")
            break
        num1 =float(input( "\n for modulo/remainder num1 should be int \n give num1 :"))
        num2 = 0
        if operation!= 'sq' and operation!= 'sqrt':
            num2 = float(input( "\n for modulo/remainder num2 should be int \ngive num2 :"))
        result = calculator(operation,num1,num2)
        print(f"answer = {result}\n\n\n")
    except ValueError:
        print("enter a numeric value please")
