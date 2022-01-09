# user input 3 numbers
# which one is bigest number print this one

# first way
first_number = int(input("First number : "))
second_number = int(input("Second number : "))
third_number = int(input("Third number : "))

if first_number >= second_number and first_number >= third_number :
    largest_number = first_number
    
elif second_number >= first_number and second_number >=  third_number :
    largest_number = second_number

else:
    largest_number = third_number
    print("Largest Number : " + str(largest_number))





# second way
first_number = int(input("First number : "))
second_number = int(input("Second number : "))
third_number = int(input("Third number : "))

input_numbers = []
input_numbers.append(first_number)
input_numbers.append(second_number)
input_numbers.append(third_number)

print("Input Numbers: " + str(input_numbers))
largest_number = max(input_numbers)
print("Largest Number : " + str(largest_number))


# third way
first_number = int(input("First number : "))
second_number = int(input("Second number : "))
third_number = int(input("Third number : "))

x = [first_number,second_number,third_number]
x.sort()
print("Largest Number:" + str(x[2]))


