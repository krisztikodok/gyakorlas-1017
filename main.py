"""
x = int(input("x="))
maradek = x % 10
temp = x - maradek
w=0
if maradek == 0 or maradek == 1 or maradek == 2:
    w = 0
elif maradek >= 3 and maradek <= 7:
    w = 5
elif maradek == 8 or maradek == 9:
    w = 10
else:
    w = 10

print(temp + w)
"""

#################

# sets
A = {1,43,2,10,75,13}
print(A)
A.add(999)
print(A)
A.remove(13)
print("\n\n")
print("A:",A)

B=set()
C=set()

for i in range(0,8):
  B.add(i)
for i in range(320,321):
  C.add(i)

print("B:",B)
print("C:",C)

AxB = A.intersection(B)
print("Intersection between A and B:",AxB)
AorB=A.difference(B)
print("Difference between A and B:",AorB)
AandB=A.union(B)
print("A and B",AandB)

symm=A.symmetric_difference(B)
print("Symmetric difference:",symm)

if C.issubset(A):
  print("C is a subset of A")
else:
  print("C is not a subset of A")

if A.issubset(B):
  print("A is a subset of B")
else:
  print("A is not a subset of B")

print(12 in A.union(B))
y = 10 in (A.union(B))
print(y)
C = {2,3}
