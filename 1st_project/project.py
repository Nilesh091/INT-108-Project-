import random
def project(a,b):
    return random.randrange(a,b)
def isEven(k):
   return k%2==0
def isNeg(k):
    return k<0
def isPrime(k):
    k_b=0
    for j in range(2, k):
        if k % j == 0:
            k_b = k_b + 1
    return k==2 or k_b ==0
a=int(input("Enter Lower Range: "))
b=int(input("Enter Upper Range: "))
rendom_no=project(a,b)
print("The number is:",rendom_no)
if isEven(rendom_no):
    print(rendom_no,"is a even number")
else:
    print(rendom_no,"is an odd number")

if isNeg(rendom_no):
    print(rendom_no,"is a negative number")
else:
    print(rendom_no,"is a positive number")
if rendom_no==1 or rendom_no==0:
    print(rendom_no,"is neither prime nor composite")
elif isNeg(rendom_no):
    print(rendom_no,"is a composite number")
elif isPrime(rendom_no):
    print(rendom_no,"is a prime number")
else:
    print(rendom_no,"is a composite number")

    
    
    
