from cryptography.fernet import Fernet
from encrypt import encrypt

# Mot de passe par défaut
DEFAULT_PASSWORD = "mon_password_secret"

def main():
    key = Fernet.generate_key()
    password = "mon_password_secret"
encryption_handler = EncryptionHandler(password)

text_to_encrypt = "Hello, World!"
encrypted_text = encryption_handler.encrypt(text_to_encrypt)
print(f"Texte chiffré : {encrypted_text}")

decrypted_text = encryption_handler.decrypt(encrypted_text)
print(f"Texte déchiffré : {decrypted_text}")
    
    # Vérification du mot de passe
    # entered_password = input("Entrez le mot de passe : ")
    # if entered_password != DEFAULT_PASSWORD:
    #     print("Mot de passe incorrect. L'encryption et le déchiffrement ne sont pas autorisés.")
    #     return

    # # Le mot de passe est correct, poursuivre avec l'encryption/déchiffrement
    # text_to_encrypt = input("Entrez le texte à chiffrer : ")

    # encrypted_text = encrypt(text_to_encrypt, key)
    # print(f"Encrypted text: {encrypted_text}")

    # decrypted_text = decrypt(encrypted_text, key)
    # print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()