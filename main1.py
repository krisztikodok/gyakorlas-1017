a=b=c=0

def add(a,b):
    return a+b

print(add(a,c))
x=2
y=6
atl=(x+y)/2

temp=x*y  
mert=temp**0.5
print("Számtani közép:",atl)  # átlag
print("Mértani közép:",temp)  # √x*y

for i in range(0,11,2):
  print(i)
  #print(i+1)

print("Visszafelé:")
for i in range(10,-1,-1):
  if(i>0):
    print(i, end=", ")
  else:
    print(i)

print("5-10-ig:")
var=range(5,10)
for i in var:
  print(i,end=" ")


j=0
while j<=10:
  print(j)
  j+=1