import LWE4 as lwe
import json
import secrets

# Load the private key from the JSON file
with open("private_key.json", "r") as f:
    private_key = json.load(f)

# Load the public key from the JSON file
with open("public_key.json", "r") as f:
    public_key = json.load(f)

# Generating a test string to encrypt
original_string = 'SoloPython!'

# Encrypt the test string using the public key
encrypted_string = lwe.encrypt.encrypt(original_string, public_key)

print("Original string: ", original_string)
print("Encrypted string: ", encrypted_string)


# Decrypt the encrypted string using the private key
decrypted_string = json.loads(lwe.decrypt.decrypt(json.loads(encrypted_string), private_key))

print("Decrypted string: ", decrypted_string)

# Check if the decrypted string is equal to the original string
if original_string == decrypted_string:
    print("Encryption and decryption successful!")
else:
    print("Error: Decrypted string does not match the original string.")