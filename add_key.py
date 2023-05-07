def append_key_to_authorized_keys(pub_key, authorized_keys):
    # Read the user key from a file
    with open(pub_key, 'r') as file:
        user_key = file.readline()

    with open(authorized_keys, 'r') as file:
        auth_keys_content = file.read()

        # Check if the public key is already in the authorized_keys file
        if user_key not in auth_keys_content:

            # Append the user key to the authorized_keys file
            with open(authorized_keys, 'a') as file:
                file.write(user_key + '\n')

            return ""
        else:
            return "Oops! Esta chave já foi registada!"