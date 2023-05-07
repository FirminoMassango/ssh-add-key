import tkinter as tk
from tkinter import filedialog

def get_usernames_from_authorized_keys(authorized_keys):
    users = []
    # Extract the usernames from the authorized_keys file
    with open(authorized_keys, 'r') as file:
        for line in file:
            split_line = line.split()
            if split_line:
                users.append(split_line[-1])

    return users

