import sys

# set the year / month to the input
if (len(sys.argv) > 1):
    inputNum = int(sys.argv[1])

    if inputNum > 1: 
        # Iterate from 2 to n / 2  
        for i in range(2, inputNum//2): 
                
            # If num is divisible by any number between  
            # 2 and n / 2, it is not prime  
            if (inputNum % i) == 0: 
                print(inputNum, "is not a prime number") 
                break
        else: 
            print(inputNum, "is a prime number") 
        
    else: 
        print(inputNum, "is not a prime number") 

else:
    print("Please enter a number")