from encrypt import EncryptionHandler
# Mot de passe par défaut
DEFAULT_PASSWORD = "mon_password_secret"
def main():
    password = "mon_password_secret"
    encryption_handler = EncryptionHandler(password)

    text_to_encrypt = "Hello, World!"
    encrypted_text = encryption_handler.encrypt(text_to_encrypt)
    print(f"Texte chiffré : {encrypted_text}")

    decrypted_text = encryption_handler.decrypt(encrypted_text)
    print(f"Texte déchiffré : {decrypted_text}")

if __name__ == "__main__":
    main()
