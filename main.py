# jelszó jó-e
# megfelelő jelszó: van benne kis-és nagybetű, szám és legalább 8 karakter hosszú

jelszo="Ahh12345"
db_nagy=0
db_kicsi=0
db_szam=0
for i in range(0,len(jelszo)):
  ch=jelszo[i:i+1]
  if ch>='A' and ch<='Z':
    db_nagy+=1
  elif ch>='a' and ch<='z':
    db_kicsi+=1
  elif ch>='0' and ch<='9':
    db_szam+=1
  else:
    pass
jo=db_nagy>0 and db_kicsi>0 and db_szam>0 and len(jelszo)>=8
if jo:
  print("Jó jelszó")
else:
  print("Rossz jelszó")