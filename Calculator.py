print("Simple Calculator")
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
print("Select the choice to perform")
choice=int(input("1.sum\n 2.sub\n 3.multi\n 4.div\n 5.exit\n:"))
if choice==1:
    sum=num1+num2
    print("The sum is:",sum)
elif choice==2:
    sub=num1-num2
    print("The subtraction is:", sub)
elif choice==3:
    multi=num1*num2
    print("The multiplication is:",multi)
elif choice==4:
    div=num1/num2
    print("The division is:",div)
else:
    print("Invalid choice")