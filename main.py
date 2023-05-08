from add_key import append_key_to_authorized_keys
from get_users import get_usernames_from_authorized_keys
import utils
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage


def add_key():
    # Get the path to the public key file
    pub_key = filedialog.askopenfilename(title="Select Public Key", filetypes=[("Chave pública", "*.pub")])
    if not pub_key:
        return

    # Call the function to append the key to authorized_keys file
    message = append_key_to_authorized_keys(pub_key, utils.authorized_keys)
    
    update_message(message)

    # Update the list of users
    update_user_list(user_listbox)

def update_message(message):
    label.config(text=message)


def update_user_list(user_listbox):
    # Clear the listbox
    user_listbox.delete(0, tk.END)
    
    # Get the list of users
    users = get_usernames_from_authorized_keys(utils.authorized_keys)
    
    # Add the users to the listbox
    for user in users:
        user_listbox.insert(tk.END, user)

# Create the main window
root = tk.Tk()
root.title("Intellica - Utilizador Git")
icon = PhotoImage(file = 'img/icon.png')
# Icon set for program window
root.iconphoto(False, icon)
# Set the default window size
root.geometry("500x500")

# Set the background color to white
root.configure(bg="#FFFFFF")

# Add the "Add Public Key" button
add_key_button = tk.Button(root, text="Adicionar chave pública", bg="#0C8CE9", fg="#FFFFFF", command=add_key)
add_key_button.pack(padx=10, pady=20)

# Add a label to display messages
label = tk.Label(root, text="", bg="#FFFFFF", fg="#FF0000")
label.pack()


# Add the listbox to display the users
user_listbox = tk.Listbox(root, bg="#EFEFEF", fg="#4C4C4C")
user_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Add the users to the listbox
update_user_list(user_listbox)

# Start the main event loop
root.mainloop()


