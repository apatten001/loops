import random
# while loops let you loop through while a condition is true

num1 = 1

while num1 <= 15:
    print("I like to code using python")
    num1 += 1



num2 = random.randrange(0,75)

while num2 != 74:
    print(num2)
    num2 = random.randrange(0, 75)


# you can also break a while loop so that it does not go on forever


num3 = 0

while num3 < 1000000:
    if num3 % 2 == 0:
        print(num3)
    elif num3 == 21:
        break
    else:
        num3 += 1
        continue
    num3 += 1


transport_list = ["cars","trucks",'helicopters','airplanes','motorcycles','boat','bicycle']

while transport_list != "cars":
    print(transport_list)
    transport_list += 1









