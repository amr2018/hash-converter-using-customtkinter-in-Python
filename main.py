import customtkinter as ctk
from hashlib import md5, sha224, sha256, sha384

algorithims = {
    'md5': md5,
    'sha384': sha384,
    'sha256': sha256,
    'sha224': sha224
}

root = ctk.CTk()
root.wm_title('Text to hash converter')
root.geometry('500x300')

# add text input
text_input = ctk.CTkTextbox(
    root,
    width=250,
    height=150
)

text_input.place(x = 20, y = 20)

# add title for options
t1 = ctk.CTkLabel(
    root,
    text = 'Choice hash algorithem',
    font = ('san-serf', 16)
)

t1.place(x = 280, y = 20)

# add hashes options
hash_options = ctk.CTkOptionMenu(
    root,
    values = list(algorithims.keys())
)

hash_options.place(x = 280, y = 60)


# add output hash
output_hash = ctk.CTkTextbox(
    root,
    height=60,
    width=250
)

output_hash.place(x = 20, y = 200)


# make function to convert text
def convert_to_hash():
    output_hash.delete(0.1, ctk.END)
    algo = hash_options.get()
    text = text_input.get(0.1, ctk.END)
    hash = algorithims[algo](text.encode()).hexdigest()
    output_hash.insert(0.1, hash)

# add convert bt
convert_bt = ctk.CTkButton(
    root,
    text = 'Convert',
    command = convert_to_hash
)


convert_bt.place(x = 280, y = 100)



root.mainloop()