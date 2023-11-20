from encrypt import EncryptionHandler
# Mot de passe par défaut
DEFAULT_PASSWORD = "mon_password_secret"
def main():
    

    
    # Vérification du mot de passe
    entered_password = input("Entrez le mot de passe : ")
    if entered_password != DEFAULT_PASSWORD:
        print("Mot de passe incorrect. L'encryption et le déchiffrement ne sont pas autorisés.")
        return

    text_to_encrypt = "Hello, World!"
    encrypted_text = encryption_handler.encrypt(text_to_encrypt)
    print(f"Texte chiffré : {encrypted_text}")

    decrypted_text = encryption_handler.decrypt(encrypted_text)
    print(f"Texte déchiffré : {decrypted_text}")

if __name__ == "__main__":
    main()
