num = [int(input()) for x in range(10)]

num_mul = []
Max = []

def prime_numrical(x):
    n = 0
    for i in range(2, x):
        if (x%i == 0 and is_prime(i)):    
            n +=1
    return n

def is_prime(x):
    m = 0
    for i in range(1, x):
        if (x%i == 0):
            m+=1
    if (m>1):
        return False
    else:
        return True
    
for i in range(10):
    num_mul.append(prime_numrical(num[i]))

max_num_mul = max(num_mul)

for i in range(10):
    if (num_mul[i] != max_num_mul):
        num_mul[i] = 0

for i in range(10):
    if(not num_mul[i] == 0):
        Max.append(num[i])

print(max(Max), max_num_mul)