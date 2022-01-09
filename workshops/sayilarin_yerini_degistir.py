x = 10
y = 20

# how to change value of variable?

# Way1
x = x + y # x becomes 30
y = x - y # y becomes 10
x = x - y # x becomes 20

print("swap_x : " + str(x))
print("swap_y : " + str(y))

#Way2
x,y = y,x
print("swap_x : " + str(x))
print("swap_y : " + str(y))

#Way3
temp = x
x = y
y = temp

print("swap_x : " + str(x))
print("swap_y : " + str(y))



