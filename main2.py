import math

i=0
while True:
  print(i)
  
  i=i+1
  if i==11:
    i="XX"
    print(i)
    i=12
  if i==20:
    break

# list
X=[1,2,4,6]
for j in X:
  print(j,end=" ")
print("\n\n")
new=['Anna','Peti',False,43,6.66,43e-5,0x63]
for i in new:
  print(i,type(i))

yy=int(input("Kérek egy számot:"))
if yy%2==0:
  print("A szám páros")
else:
  print("A szám páratlan")

# másodfokú egyenlet megoldóképlete
aa=bb=cc=0.0
aa=float(input("a="))
bb=float(input("b="))
cc=float(input("c="))
D=bb*bb-4*aa*cc
if D>=0:
  x1=(-bb+math.sqrt(D))/(2*aa)
  x2=(-bb-math.sqrt(D))/(2*aa)
  print("x1=",x1,"x2=",x2)
else:
  print("Nincs megoldás")