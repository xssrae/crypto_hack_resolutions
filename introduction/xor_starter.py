# xor == conjunção:
# 1 ^ 1 = 0
# 1 ^ 0 = 1
# 0 ^ 1 = 1
# 0 ^ 0 = 0

#  0110 ^ 1010 = 1100

given = "label"

print("crypto{", end="")
for x in given:
  print(chr(ord(x)^13), end="")
print("}")

    