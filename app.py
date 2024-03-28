

## Checking type of a data variable
int=int(input(f"Enter a number for us to check the type it is: \n"))

int_2=input(f"Enter a name let's see what datatype it is:\n")

print("The type of " + str(int) + " is " + str(type(int)))

print(f"The type of {int_2} is {type(int_2)}")



a=55
print(type(a))


####    CONDITIONAL STATEMENTS
## compare numbers entered by the user

x=input("Enter a number:\n")
y=input("Enter another number:\n")
if x>y:
    print(f"{x} is greater than {y}")
elif x==y:
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is less than {y}")  
         
         
    
    