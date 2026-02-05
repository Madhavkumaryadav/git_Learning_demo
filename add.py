def addition():
    a=int(input("Enter first number : " ))
    b=int(input("Enter Second nmt3er : "))
    print(f"Addition of {a} and {b} is : ",a+b)
    
def show():
    print("1. addition ")
    print("2. Exit ")
    
if __name__=='__main__':
    while True:
        
        show()
        option=int(input("Enter your option : "))
        if option == 1:
            res=addition()
            
        if  option ==2:
            break
        else:
            print("provide the valid input ......")
    