import LWE4 as lwe
import json

# Generating the keys for the encryption process
private_key, public_key = lwe.keygen.keygen(30, 8096)

# Save the private key to a JSON file
with open("private_key.json", "w") as f:
    json.dump(json.loads(private_key), f)

# Save the public key to a JSON file
with open("public_key.json", "w") as f:
    json.dump(json.loads(public_key), f)

print("Keys generated and saved to private_key.json and public_key.json.")