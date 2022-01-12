#%% STARS

number = int(input("Input number of star: "))

star = ""

for x in range(1,number+1):
    star = star+ "*"
    print(star)

#%% PRIME NUMBER CONTROL

number = int(input("input the number: "))
prime = True
for x in range(2,number):
    if (number % x) ==0:
        prime = False
        break

if prime == True:
    print("PRIME")
else:
    print("NOT PRIME")    
