import hashlib

md5 = input("Enter the string that you wanna hash:")

result = hashlib.md5(md5.encode())

print("The result is: ", end ="")
print(result.hexdigest())
