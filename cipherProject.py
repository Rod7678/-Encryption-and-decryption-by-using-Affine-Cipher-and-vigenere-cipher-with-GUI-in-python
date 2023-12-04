# from tkinter import *
# root = Tk()
# root.geometry("688x600")
# root.title("Vigerence cipher")
# #Vigerence cipher
import math

def encrypt_word(pt,key):
    ct=''
    n=len(pt)
    cell_val=math.ceil(n/len(key))
    key=cell_val*key
    for i in range(n):
        if pt[i].islower():
            pi=ord(pt[i])-97
            ki=ord(key[i])-97
            enc_word=chr(97+(pi+ki)%26)
            ct+=enc_word
        else:
            pi=ord(pt[i])-65
            ki=ord(key[i])-65
            ei=chr(65+(pi+ki)%26)
            ct+=ei
    print('Encrypted Text: ',ct)
    return ct

def decrypt_words(ct,key):
    pt=''
    n=len(ct)
    cell_val=math.ceil(n/len(key))
    key=cell_val*key
    for i in range(n):
        if ct[i].islower():
            ei=ord(ct[i])-97
            ki=ord(key[i])-97
            di=(ei-ki)
           
        else:
           ei=ord(ct[i])-65
           ki=ord(key[i])-65
           di=(ei-ki)
        if (di>=0):
            di=di%26
        else:
            di=(di+26)%26
            
        pt+=chr(di+97)
    print('Decrypted Text : ',pt)

pt=input('Enter the plain text to be encrypted:')
key=input('Enter the key for encryption:')
enc=encrypt_word(pt,key)
decrypt_words(enc,key)

    
##Afine cipher
def encrypt_words(plain_text,a,b):
    cipher_text=''
    for word in plain_text:
        for i in word:
            if i.isupper():
                val=ord(i)-65
                enc_word=chr(a*val+b)%26
                cipher_text+=chr(enc_word+65)
            else:
                val=ord(i)-97
                enc_word=(a*val+b)%26
                cipher_text+=chr(enc_word+97)
    print('Encrypted Text: ',cipher_text)
    return cipher_text

def decrypt_words(cipher_text,a,b):
    c=0
    for i in range(1,27):
        if(a*i)%26==1:
            c=i
            
    plain_text=''
    for word in cipher_text:
        for i in word:
            if i.isupper():
                y=ord(i)-65
                enc_val=chr(65+(c*(y-b))%26)
            else:
                y=ord(i)-97
                enc_val=chr(97+(c*(y-b))%26)
                plain_text+=enc_val
    print('Decrypted Text : ',plain_text)
plain_text=input('Enter the plain text to be encrypted:').split()
a=int(input('Enter the key for shift cipher a:'))
b=int(input('Enter the key for shift cipher b:'))
enc=encrypt_words(plain_text,a,b)
decrypt_words(enc,a,b)




# f1= Frame(root, borderwidth=6, bg="grey" , relief=SUNKEN)
# f1.pack(side=BOTTOM ,anchor="n")

# b1 = Button(f1, fg="red",text="encryption")
# b1.pack( side=TOP,padx=50)



# root.mainloop()