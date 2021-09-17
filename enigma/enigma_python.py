# encryption and decryption program, author rezwan ahmod sam

import os


def home():
   print("\n")
   print("-----------------------------------------------------\n")
   print("\t\t   ***Enigma***\n")
   print("\tEncryption And Decryption program\n")
   print("\tAuthor: Rezwan Ahmod Sami\n")
   print("-----------------------------------------------------\n")
   print(" Select a option to do operation: \n\n")
   print("\t1.Encrypt Text.\n")
   print("\t2.Decrypt Text.\n")
   user_input = input("Option>>> ");

   if user_input == '1':
      os.system('cls')
      print("you choosed  encrypt option\n")
      text = input("Enter text>>> ")
      print("\n"+encrypt(text))
      load()
   else:
      os.system('cls')
      print("you choosed  Decrypt option\n")
      text = input("Enter text>>> ")
      print("\n"+decrypt(text))
      load()

def encrypt(text):
   enc_text = '';
   for i in range(len(text)):
      enc_text += chr(ord(text[i]) + 4 + 3)
   return enc_text 


def decrypt(text):
   decrypt_text = '';
   for i in range(len(text)):
      decrypt_text += chr(ord(text[i]) - 4 -3)
   return decrypt_text 

def load():
   cmd = input("\n\nEnter 1 for go home, Enter 0  for Exit program: ")
   if cmd == '1':
     os.system('cls')
     home()
   else:
      exit()

home()
  
