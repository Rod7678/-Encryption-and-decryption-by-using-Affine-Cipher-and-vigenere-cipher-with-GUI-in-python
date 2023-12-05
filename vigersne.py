import tkinter as tk
import math

def encrypt_word(pt, key):#Function to encrypt a given plaintext 'pt' using a key 'key'
    ct = ''
    n = len(pt)
    cell_val = math.ceil(n / len(key))
    key = cell_val * key
    for i in range(n):
        if pt[i].islower():
            pi = ord(pt[i]) - 97
            ki = ord(key[i]) - 97
            enc_word = chr(97 + (pi + ki) % 26)
            ct += enc_word
        else:
            pi = ord(pt[i]) - 65
            ki = ord(key[i]) - 65
            ei = chr(65 + (pi + ki) % 26)
            ct += ei
    return ct

def decrypt_words(ct, key): # Function to decrypt a given ciphertext 'ct' using a key 'key'
    pt = ''
    n = len(ct)
    cell_val = math.ceil(n / len(key))
    key = cell_val * key
    for i in range(n):
        if ct[i].islower():
            ei = ord(ct[i]) - 97
            ki = ord(key[i]) - 97
            di = (ei - ki)
        else:
            ei = ord(ct[i]) - 65
            ki = ord(key[i]) - 65
            di = (ei - ki)
        if di >= 0:
            di = di % 26
        else:
            di = (di + 26) % 26
        pt += chr(di + 97)
    return pt

def encrypt():               # Function to perform encryption or decryption based on user input
    plain_text = input_text.get("1.0", "end-1c")
    key = key_entry.get()
    enc_text.delete("1.0", "end")
    encrypted_text = encrypt_word(plain_text, key)
    enc_text.insert("1.0", encrypted_text)

def decrypt():
    cipher_text = enc_text.get("1.0", "end-1c")
    key = key_entry.get()
    dec_text.delete("1.0", "end")
    decrypted_text = decrypt_words(cipher_text, key)
    dec_text.insert("1.0", decrypted_text)


root = tk.Tk()
root.title("Vigerene cipher")
root.geometry("600x500")
root.resizable(width=False,height=False)
#These lines create a label and a text widget for the user to input the plaintext or ciphertext.
input_label = tk.Label(root, text="Enter the text:")
input_label.pack()
input_text = tk.Text(root, height=5, width=40)
input_text.pack()
#These lines create a label and an entry widget for the user to input the encryption key.
key_label = tk.Label(root, text="Enter the key:")
key_label.pack()
key_entry = tk.Entry(root)
key_entry.pack()

#This code creates a button that allows the user encryption and decryption.with encrypted text and decrypted text output
encrypt_decrypt_button = tk.Button(root, text="Encrypt", command=encrypt)#This button triggers the encrypt function when clicked.
encrypt_decrypt_button.pack(pady=10)
encrypt_label = tk.Label(root, text="Encrypted text :")
encrypt_label.pack()
enc_text = tk.Text(root, height=5, width=40)
enc_text.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt,bg="MediumPurple1")#This button triggers the decrypt function when clicked
decrypt_button.pack(pady=10)
dec_label = tk.Label(root, text="Decrypted text :")
dec_label.pack()
dec_text = tk.Text(root, height=5, width=40)
dec_text.pack()



root.mainloop()
