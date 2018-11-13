message=str(input("enter the message you want to encrypt:"))
key=input("enter the key number between 1 to 26:")
encrypted_message=''
for i in range(len(message)):
    char=message[i]
    if(char.isupper()):
      encrypted_message+=chr((ord(char) + key-65) % 26 + 65) 
    else: 
       encrypted_message = encrypted_message+ chr((ord(char) + key - 97) % 26 + 97) 
print(encrypted_message)

