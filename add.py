## Implement the addition Function 
def addition():
    a=int(input("Enter first number : " ))
    b=int(input("Enter Second nmt3er : "))
    print(f"Addition of {a} and {b} is : ",a+b)

## Implement the subtracting function  
def subtract():
    # Take two input from user 
    a=int(input("Enter first number : " ))
    b=int(input("Enter Second nmt3er : "))
    ## Print the result a+b = result 
    print(f"Addition of {a} and {b} is : ",a-b)
    
# Execution option 
def show():
    print("1. addition ")
    print("2. Subtract")
    print("3. Exit ")
    
## Main functoin that's calling to do it.
if __name__=='__main__':
    while True:
        
        show()
        option=int(input("Enter your option : "))
        if option == 1:
            res=addition()
        elif option==2:
            res=subtract()
        elif  option ==3:
            break
        else:
            print("provide the valid input ......")
    