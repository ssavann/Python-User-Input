#Reverse the number

numberA = input("Enter a number for 'A': ")
numberB = input("Enter a number for 'B': ")

print("A = " + numberA)
print("B = " + numberB)

numberC = numberA
numberA = numberB
numberB = numberC

print("Reverse the numbers")
print("A = " + numberA)
print("B = " + numberB)