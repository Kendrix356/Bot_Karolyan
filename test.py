import random
line1 = list('0000000000000000000000000')
n = random.randint(0,24)
print(n)
line1[n] = '1'
line1 = " ".join(line1)
line1 = line1.replace(" ","")
print(line1)