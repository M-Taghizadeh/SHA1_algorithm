import hashlib 
  
# initializing string 
str2hash = "Secret Message"
print("str2hash: ", str2hash)
  
# encoding str2hash using encode() 
result = hashlib.sha1(str2hash.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of hash is : ", end ="") 
print(result.hexdigest()) 