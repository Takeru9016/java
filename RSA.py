message = int(input("Enter the message to be encrypted: "))

p = 13
q = 11
e = 13

n = p * q
z = (p - 1) * (q - 1)

for i in range(10):
    w = (z * i) + 1
    if (w % e == 0):
        d = w // e
        break

def encrypt(me):
    c = pow(me, e, n)
    print("Encrypted Message is: ", c)
    return c

def decrypt(c):
    dec = pow(c, d, n)
    print("Decrypted Message is: ", dec)
    return dec

print("Original Message is: ", message)
c = encrypt(message)
d = decrypt(c)