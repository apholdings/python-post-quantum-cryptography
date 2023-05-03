# Python Post Quantum Cryptography NTRU Algorithm

This repository provides an implementation of the NTRU post-quantum cryptographic algorithm in Python. *The NTRU algorithm is resistant to attacks from quantum computers*, providing a secure solution for future-proof encryption.

## Getting Started

### 1. Create virtual environment and Install required packages:

To create a virtual environment and install the necessary packages, open a terminal or command prompt, navigate to the project directory, and run the following commands:

`python -m venv env`

`source env/bin/activate  # On Windows, use: env\Scripts\activate`


`pip install -r requirements.txt`

### 2. Run the CreateKeys.py file

To generate the public and private encryption keys, run the **CreateKeys.py** script:

`python CreateKeys.py`

### 3. Test the encryption keys using

To test the functionality of the generated encryption keys, run the **TestKeys.py** script:

`python TestKeys.py`

This script will demonstrate the encryption and decryption process using the generated keys. If successful, you should see the original message being recovered after decryption.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/apholdings/python-post-quantum-cryptography/blob/main/LICENSE) file for details.