import os

# Define the file paths for the SSH public keys file and the key to be added
authorized_keys = os.path.expanduser("~/.ssh/authorized_keys")
pub_key = os.path.expanduser("~/Projects/Python/id_rsa.pub")