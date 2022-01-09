# input number by user
# if number = 0 so print number is 0
# if number bigger than 0 print number is positive
# if number smaller than 0 print number is negative

while True :
    
    print("Welcome to my system!. In this place you ll input a number that's why system ll work on background!")
    number1 = int(input("Input a number to system!!!: "))

    if type(number1) == int:
    
        if number1 == 0:
            print("your number is notr so 0")
            print("Your number: " + str(number1))
        elif number1 >= 0:
            print("your number is positive. Be positive all time!")
            print("Your number: " + str(number1))
        else:
            print("your number is negative. I'm sad")
            print("Your number: " + str(number1))

    else:
        print("Pls! input a number!!!")



