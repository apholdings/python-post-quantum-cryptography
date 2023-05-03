# Python Post Quantum Cryptography NTRU Algorithm

This repository provides an implementation of the Lattice based post-quantum cryptographic algorithm in Python. *The Lattice LWE algorithm is resistant to attacks from quantum computers*, providing a secure solution for future-proof encryption.

## Getting Started

### 1. Create virtual environment and Install required packages:

To create a virtual environment and install the necessary packages, open a terminal or command prompt, navigate to the project directory, and run the following commands:

- Create Virtual Environment

`python -m venv env`

- Activate Virtual Environment

    On Mac, use: `source env/bin/activate`

    On Windows, use: `.\env\Scripts\activate`

- Install Required Python Packages

`pip install -r requirements.txt`


### 2. Generate Public and Private Keys

To generate the public and private encryption keys, run the **GenerateKeys.py** script:

`python GenerateKeys.py`


### 3. Test the Encryption Keys

To test the functionality of the generated encryption keys, run the **TestKeys.py** script:

`python TestKeys.py`

This script will demonstrate the encryption and decryption process using the generated keys. If successful, you should see the original message being recovered after decryption.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/apholdings/python-post-quantum-cryptography/blob/main/LICENSE) file for details.