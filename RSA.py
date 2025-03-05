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
#print(p, "p")

rand_num = randNum.random(upper, lower)
while millerrabin.is_prime(rand_num) == False or rand_num == p:
    rand_num = randNum.random(upper, lower)

q = rand_num
#print(q, "q")

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
C = 0
m = 0

try:
    msg = int(message)
    #print("int")
    C = gmpy2.powmod(msg, e, n)
    m = gmpy2.powmod(C, d, n)
    print("Encrypted message: " + str(C))
    print("Decrypted message: " + str(m))

except ValueError:
    m = ""
    for i in message:
        ascii = ord(i.upper())
        tempC = gmpy2.powmod(ascii, e, n)
        tempm = gmpy2.powmod(tempC, d, n)
        #print(ascii, tempC, tempm)
        C *= len(str(tempC))
        C += tempC
        m += str(tempm)
    strm = ""
    print (m, C)

    m = str(m)
    while len(m) > 1:
        l = m[-2:]
        #print(l, "l")
        l = int(l)
        strm = chr(l) + strm
        #print(strm)
        m = m[:-2]
        #print(m, "m")
    print("Encrypted message: " + str(C))
    print("Decrypted message: " + strm)   
    

#C = gmpy2.powmod(msg, e, n)
#m = gmpy2.powmod(C, d, n)

#print(msg)
