#This code computes perfect numbers. Perfect number is a number sum of which divisors, divided by 2, 
#is equal to the number itself. For example 6 is a perfect number because (1+2+3+6)/2 = 6. Next perfect number is 28
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
