

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
         
         
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")

    
## Using the 'and' operator
x = 5
y = 10
z = 15
if x < y and x < z:
    print("Both conditions are True")
    
## Using the 'or' operator
x = 5
y = 10
z = 15
if x < y or x < z:
    print("At least one of the conditions is True")
    
## Using the 'not' operator
x = 5
print(not(x > 3 and x < 10))


    