'''

Homework 1
AOE 5404
Jaime Dorado
1/28/2026

'''

# 1a)
a = 1
b = 1e-16
c = -1

if a + b + c == a + c + b:
    print('Problem 1a equality holds true')

else:
    print('Problem 1a equality does not hold true')


# 1b)
if 0.3 + 0.6 == 0.9:
    print("Problem 1a equality holds true")

else:
    print("Problem 1b equality does not hold true")


# 2)
import time, math
start_time = time.time()
elasped_time = 0
error = 0.0005
while True:
    elasped_time = time.time() - start_time
    if abs(math.pi/2 - elasped_time) / (math.pi/2) < error:
        print('Launch!')
        print(f"Launch time:{elasped_time} s")
        break

    else:
        pass