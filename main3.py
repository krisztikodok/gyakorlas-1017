# prímek

x=0
x=int(input("Enter a number:"))
db=0
for i in range(2,x):
  if x%i==0:
    db=db+1
print("Osztók száma:",db)

if(db==0):
  print(x,"prímszám")
else:
  print("Ez nem prímszám")

# palindrom #1
pal="AMVMA"
print("palindrom #1\n",pal)
n=len(pal)
i=0
j=n-1
while i<j:
  if pal[i]!=pal[j]:
    print("Nem palindrom")
    break
  i=i+1
  j=j-1
else:
  print("Palindrom")

# palindrom #2
new_pal="GAPPAG"
print("palindrom #2\n",new_pal)
length=len(new_pal)
p=True
for i in range(0,length // 2): # //:floor division
  a=new_pal[i:i+1]
  b=new_pal[length-i-1:length-i]
  if(a!=b):
    p=False
if p:
  print("Palindrom")
else:
  print("Nem palindrom")