from time import sleep
def dothemath(number):
    if (number % 2 == 0):
        return number// 2
    elif (number % 2 == 1):
        return number * 3 + 1
    else:
        print("Something went wrong" )
        return None

    
number = int(input("Select the number to process: "))
while (number != 1):
    number  = dothemath(number)
    print(number)
    sleep(2)
print("The collatz sequence ended!")