def decimalToBinary(n):
    return bin(n).replace("0b", "")

##Solutie siruri de biti in python

a = str(decimalToBinary(int(input("Introduceti primul numar: "))))
b = str(decimalToBinary(int(input("Introduceti al doilea numar: "))))

print(a, b, sep="\n")

len_a = len(a)
len_b = len(b)

if len_a > len_b:
    b = "0" * (len_a - len_b) + b

elif len_a < len_b:
    a = "0" * (len_b - len_a) + a

or_result = "".join([str(int(a[i]) | int(b[i])) for i in range(len(a))])
and_result = "".join([str(int(a[i]) & int(b[i])) for i in range(len(a))])
xor_result = "".join([str(int(a[i]) ^ int(b[i])) for i in range(len(a))])

print(or_result + "\tOR")
print(and_result + "\tAND")
print(xor_result + "\tXOR")