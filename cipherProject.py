import tkinter as tk

def encrypt_words(plain_text, a, b):# Function to encrypt a given plaintext 'plain_text' using keys 'a' and 'b'
    cipher_text = ''
    for word in plain_text:
        for i in word:
            if i.isupper():
                val = ord(i) - 65
                enc_word = (a * val + b) % 26
                cipher_text += chr(enc_word + 65)
            else:
                val = ord(i) - 97
                enc_word = (a * val + b) % 26
                cipher_text += chr(enc_word + 97)
    return cipher_text

def decrypt_words(cipher_text, a, b):# Function to decrypt a given ciphertext 'cipher_text' using keys 'a' and 'b'
    c = 0
    for i in range(1, 27):
        if (a * i) % 26 == 1:
            c = i

    plain_text = ''
    for word in cipher_text:
        for i in word:
            if i.isupper():
                y = ord(i) - 65
                enc_val = chr(65 + (c * (y - b)) % 26)
            else:
                y = ord(i) - 97
                enc_val = chr(97 + (c * (y - b)) % 26)
            plain_text += enc_val
    return plain_text

def encrypt(): # Function to perform encryption and update the GUI
    a = int(a_entry.get())
    b = int(b_entry.get())
    plain_text = input_text.get("1.0", "end-1c")
    enc_text.delete("1.0", "end")
    encrypted_text = encrypt_words(plain_text, a, b)
    enc_text.insert("1.0", encrypted_text)

def decrypt():# Function to perform decryption and update the GUI
    a = int(a_entry.get())
    b = int(b_entry.get())
    cipher_text = enc_text.get("1.0", "end-1c")
    dec_text.delete("1.0", "end")
    decrypted_text = decrypt_words(cipher_text, a, b)
    dec_text.insert("1.0", decrypted_text)

root = tk.Tk()
root.title("Affine cipher Text")
root.geometry("600x550")
root.resizable(width=False,height=False)

input_label = tk.Label(root, text="Enter the text:",font="Helvetica 15 bold")
input_label.pack()
input_text = tk.Text(root, height=4, width=40, font="Helvetica 12 bold")
input_text.pack()

a_label = tk.Label(root, text="key a:")
a_label.pack()
a_entry = tk.Entry(root)
a_entry.pack()

b_label = tk.Label(root, text="key b:")
b_label.pack()
b_entry = tk.Entry(root)
b_entry.pack()


encrypt_button = tk.Button(root, text="Encrypt", command=encrypt, bg="MediumPurple1")
encrypt_button.pack(pady=10)
encrypt_label = tk.Label(root, text="Encrypted text :",font="Helvetica 10 bold")
encrypt_label.pack()
enc_text = tk.Text(root, height=5, width=40, )
enc_text.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack(pady=10)
dec_label = tk.Label(root, text="Decrypted text :",font="Helvetica 10 bold")
dec_label.pack()
dec_text = tk.Text(root, height=5, width=40)
dec_text.pack()




root.mainloop()
