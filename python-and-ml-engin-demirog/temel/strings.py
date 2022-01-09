# STRING

# substring

message = "Hello World"

print(message[2:5])

new_message = message[2:]

print(new_message)

print(len(message))

# len
# if we don't know len of string so how can we find last character in string?

last_char = message[len(message)-1:len(message)]
print(last_char)

# lower-upper

print(message.upper())
print(message.lower())

# replace

# message = message.replace("o", "ö") # if you'd like to change  as permanently
print(message.replace("o", "ö"))
print(message.replace("e", "a"))

# split-sprit
# split : string to array default by space
bilgi = " Sukru Tas 20 Denizli "
print(bilgi.split()) # split by space and trim 
print(bilgi.split(" ")) # split by space and without trim

bilgi = " Sukru;Tas;20;Denizli ".strip() # to trim space
print( "Hometown : " + bilgi.split(";")[3])

# input

name = input("Name : ")
number1 = input("number1: ")
number2 = input("number2: ")
print(int(number1)+int(number2))

