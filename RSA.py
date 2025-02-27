import randNum
import millerrabin
import extendedeuclidean
import gmpy2

p = 0
q = 0
upper = int(input("Highest number to generate: "))
lower = int(input("Lowest number to generate: "))
n = 0
totient = 0
e = 0
d = 0

rand_num = randNum.random(upper, lower)

while millerrabin.is_prime(rand_num) == False:
    rand_num = randNum.random(upper, lower)

p = rand_num
#print(p)

rand_num = randNum.random(upper, lower)
while millerrabin.is_prime(rand_num) == False or rand_num == p:
    rand_num = randNum.random(upper, lower)

q = rand_num
#print(q)

n = p*q

totient = (p - 1) * (q - 1)
#print(totient)

#if (totient % 3 == 0):
#    e = 5
#else:
#    e = 3
e = 65537

#print(e)

d = extendedeuclidean.mod_inverse(e, totient)

print("Public key: " + str(e) + ", " + str(n))
print("Private key: " + str(d) + ", " + str(n))

message = input("What is the message you would like to encrypt? ")
#encrypt: C = m^e % n
#decrypt: m = C^d % n
msg = 0

try:
    msg = int(message)
    print("int")
except ValueError:
    for i in message:
        ascii = ord(i.upper())
    #print(ascii)
        msg = msg * 100
        msg += ascii
    #print(msg)

C = gmpy2.powmod(msg, e, n)
m = gmpy2.powmod(C, d, n)

print(msg)

print("Encrypted message: " + str(C))
print("Decrypted message: " + str(m))