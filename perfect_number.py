i = 1
while i < 1000:
    array_of_divisors = []
    sum_of_divisors = []
    for j in range(1, i+1):
        if i % j == 0:
            array_of_divisors.append(j)
    sum_of_divisors = sum(array_of_divisors)
    if (sum_of_divisors / 2 == i):
        print("Perfect number:", i)
    i += 1