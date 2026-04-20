num1=float(input("Enter a no:"))
num2=float(input("Enter a no:"))
op=input("choose option(=,-,*,/):")
if op=='+':
    result=num1+num2
elif op=='-':
    result=num1-num2
elif op=='*':
    result=num1*num2
elif op=='/':
    if num2!=0:
        result=num1/num2
    else:
        print("cannot divide by zero!")
        exit()
else:
      print("invalid operator!")
      exit()
print("result:",result)