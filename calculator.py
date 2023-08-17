print("CALCULATOR")

n1=float(input("Enter First number : "))
n2=float(input("Enter Second number : "))

print("\nFor Addition Press 1 \nFor Subtraction Press 2 \nFor Multiplication Press 3 \nFor Division Press 4 ")

operation=int(input("\nPress number : "))

if operation == 1:
    print("Addition is : ",n1+n2)
    
elif operation == 2:
    print("Subtraction is : ",n1-n2)
    
elif operation == 3:
    print("Multiplication is : ",n1*n2)
    
elif operation == 4:
    print("Divison is : ",n1/n2)
    
else:
    print("You Press wrong number")
