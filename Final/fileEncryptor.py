from cryptography.fernet import Fernet

class FileEncryptor:
    def __init__(self, key):
        self.key = key
        self.fernet = Fernet(self.key)

    def encrypt_file(self, filename):
        """Encrypts a file and saves the encrypted content under a new filename with '.enc' extension.

        Args:
            filename (str): The name of the file to encrypt.

        Returns:
            str: The filename of the encrypted file.
        """

        with open(filename, 'rb') as file:
            data = file.read()
        encrypted_data = self.fernet.encrypt(data)

        new_filename = filename + '.enc'
        with open(new_filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        return new_filename

    def decrypt_file(self, filename):
        """Decrypts an encrypted file and saves the decrypted content under the original filename.

        Args:
            filename (str): The name of the encrypted file to decrypt.

        Returns:
            str: The filename of the decrypted file.
        """

        if not filename.endswith('.enc'):
            raise ValueError("File does not appear to be encrypted")
        

        with open(filename, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
        decrypted_data = self.fernet.decrypt(encrypted_data)

        original_filename = 'dec_' + filename[:-4]  # Remove '.enc' extension
        with open(original_filename, 'wb') as file:
            file.write(decrypted_data)

        return original_filename
