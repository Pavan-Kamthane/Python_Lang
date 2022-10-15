k = [chr(ord("A")+i) for i in range(26)]
v = [i for i in range(26)]
d = {k[i] : v[i] for i in range(26)}

def get_key(val):
  for key,value in d.items():
      if(value == val):
        return key
  
def encrypt(pt):
  key = 7
  li = []
  for i in pt:
    li.append((d[i] + key)%26)
  
  for i in range(len(li)):
    li[i] = get_key(li[i])
  
  # print(li)
  
  st = ""
  for i in li:
    st += i
  # print(st)
  return st

def decrypt(pt):
  st = ""
  for i in range(len(pt)):
    a = d[pt[i]] - 7
    if(a < 0):
      a += 26
    st += get_key(a)
  # print(st)
  return st

pt = input("Enter plain text(Don't Add Space): ")
pt = pt.upper()
a = encrypt(pt)
print("Encrypted Message:",a)
print("Decrypted Message:",decrypt(a))