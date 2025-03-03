from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import io
import itertools
import hashlib
import os

UID = 120395246
First_Name="Rithik Sarvesh"
Last_Name="Bharathiraja"


key_with_error='''-----BEGIN DSA PRIVATE KEY-----
MIIBuQIBAAKBgQC973oUk7##7lilY1gwPAtXvTNDWbPbQhlstbax0b6LMyPCE1xf
gwLoercCPm1OWl65pRExUR5g0CJxFZNekWQKh7fNqzMQt5fUKMMwtU4Im05M+sTb
FeVYTiUrEdWjAbF5XvN6RgcEp7rL1ZX4VucElbxoAIvek+Aqfr0Zg/ltBQIVAKoK
+9q7j+T3esxgCTQMI2BQKSQnAn8dphjfU5jwzf+Nst9rkn1tZO0afBuzvNMRS8BF
9LCJ2q2Nly9Orifz8IJqkhIGnEy802QyjUgLJAgYlBWarK1vJTQApgwN3t66mE9J
Oc3gBgi9skZ/AQimaMb8YiHskbhn85ISpgJcvkjnL2KiTA/FtwTbzAj/Z5Sqv0xK
ax2GAoGBAJpAieRPdSlKrM7x5gVlPZiI5vXEdw83IBIsK0W5XTtD5LeDfemLQDO9
Qz49svcBuH6pdINnvQ3CrxaiJyJTMnfNNK9NuBeW2Q4KZJxQflXhcNuXcG0i2m0l
QizOAkzQKKHeIMk5+7KoD3tgm4xzJvPewhaSca6upI3xVUobnjs/AhR7SchExgXv
cJMj8CVGbPRdKkKBUg==
-----END DSA PRIVATE KEY-----
'''

def verify(key):
  try:
        possible_key = DSA.import_key(io.StringIO(key).getvalue())
        print("The key is correct :")
        print(key)
        return True
  except ValueError:
        return False

def bruteforce(key_with_error):
  # Generate all possible iterations for the given characterset for 2 characters
  # You might want to convert the string to list because strings are immutable.
  # For each possible iteration do the following:
  # 1. Modify the positions in the key (## on locations 54,55) with the characters in this iteration
  # 2. Validate the key by using verify() function.
  # 3. Return the full key if it is validated in string format not list.
  # 4. Continue if the key is invalid
  #WRITE CODE HERE
  correct_key = key_with_error
  set_of_char='abcdefghijklmnopqrstuvwxyz1234567890'
  permutations=itertools.product(set_of_char,repeat=2)
  for combo in permutations:
      correct_key=key_with_error[:54]+combo[0]+combo[1]+key_with_error[56:]
      if(verify(correct_key)):
        return correct_key
#Part-2
plain1 = b'\xd1\x31\xdd\x02\xc5\xe6\xee\xc4\x69\x3d\x9a\x06\x98\xaf\xf9\x5c\x2f\xca\xb5\x87\x12\x46\x7e\xab\x40\x04\x58\x3e\xb8\xfb\x7f\x89\x55\xad\x34\x06\x09\xf4\xb3\x02\x83\xe4\x88\x83\x25\x71\x41\x5a\x08\x51\x25\xe8\xf7\xcd\xc9\x9f\xd9\x1d\xbd\xf2\x80\x37\x3c\x5b\xd8\x82\x3e\x31\x56\x34\x8f\x5b\xae\x6d\xac\xd4\x36\xc9\x19\xc6\xdd\x53\xe2\xb4\x87\xda\x03\xfd\x02\x39\x63\x06\xd2\x48\xcd\xa0\xe9\x9f\x33\x42\x0f\x57\x7e\xe8\xce\x54\xb6\x70\x80\xa8\x0d\x1e\xc6\x98\x21\xbc\xb6\xa8\x83\x93\x96\xf9\x65\x2b\x6f\xf7\x2a\x70'

#Incorrect inputblock
plain2 = b'\xd1\x31\xdd\x02\xc5\xe6\xee\xc4\x69\x3d\x9a\x06\x98\xaf\xf9\x5c\x2f\xca\xb5\x00\x12\x46\x7e\xab\x40\x04\x58\x3e\xb8\xfb\x7f\x89\x55\xad\x34\x06\x09\xf4\xb3\x02\x83\xe4\x88\x83\x25\x00\x41\x5a\x08\x51\x25\xe8\xf7\xcd\xc9\x9f\xd9\x1d\xbd\x72\x80\x37\x3c\x5b\xd8\x82\x3e\x31\x56\x34\x8f\x5b\xae\x6d\xac\xd4\x36\xc9\x19\xc6\xdd\x53\xe2\x34\x87\xda\x03\xfd\x02\x39\x63\x06\xd2\x48\xcd\xa0\xe9\x9f\x33\x42\x0f\x57\x7e\xe8\xce\x54\xb6\x70\x80\x28\x0d\x1e\xc6\x98\x21\xbc\xb6\xa8\x83\x93\x96\xf9\x65\xab\x6f\xf7\x2a\x70'

def verify_hash(temp):
  return (hashlib.md5(plain1).digest()==hashlib.md5(temp).digest() and plain1 != temp)

matched_int=[]
our_list=[]

def hash_collision(plain2):
  #WRITE CODE HERE
  positions=[19,45,59]
  possible_hash = plain2
  set_of_char='0123456789abcdef'
  permutations=itertools.product(set_of_char,repeat=2)
  for combo in permutations:
    str=combo[0]+combo[1]
    our_list.append(int(str,16))
  for i in positions:
      cracker(i)
  possible_hash=list(possible_hash)
  for i in range(len(positions)):
      fixer(positions[i],possible_hash,matched_int[i])
  possible_hash=bytes(possible_hash)
  if(verify_hash(possible_hash)):
    return possible_hash

def cracker(position):
  for i in our_list:
      if(plain1[position]==i):
          matched_int.append(i)
          break
def fixer(position,lisst,value):
  lisst[position]=value

if __name__ == "__main__":  
  new_key = bruteforce(key_with_error)
  print(hash_collision(plain2))
