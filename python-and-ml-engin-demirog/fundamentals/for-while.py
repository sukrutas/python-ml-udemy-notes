#%% WORKING WITH FOR

# list of numbers
numbers = [6,5,3,8,4,2,5,4,11]

# variable to store the sum
sum = 0

# iterative over the list
for val in numbers:
    sum = sum+val
    
# output
print("sum: ", sum)

cities = ["Ankara", "İstanbul", "İzmir"]
# print(cities[0])
# print(cities[1])
# print(cities[2])

for city in cities:
    print("Cities: " + city)
    
for city in cities:
    print(city + " Code: " + city[0:3])
    
    
x = [1,2,3]

for y in x:
    print(y+5)
    
for city in cities:
    if city != "Ankara":
        print(city + " Code: " + city[0:3])
        print("*****")

#%%  WORKING WITH WHILE

sum = 0
i = 1

while i <= 10:
    sum = sum + i
    i = i + 1 # update counter
    
print(sum)

cities = ["Ankara", "İstanbul", "İzmir"]

for city in cities:
    if city == "İstanbul":
        continue
    print(city + " Code: " + city[0:3])
    print("*****")
    
# break : stop the loop
# continue : skip the loop for the that value

#%% FOR RANGE
for x in range(1,50,3):
    print(x+1)





















    
    
    
    