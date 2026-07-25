# DecodeLabs Cyber Security Internship — Project 2

## Basic Encryption and Decryption Using the Caesar Cipher

This project is a command-line Caesar Cipher application created for **DecodeLabs Cyber Security Internship Project 2**. It demonstrates the fundamental and reversible processes of encryption and decryption.

> **Important:** The Caesar Cipher is suitable for education only. It is not secure enough for protecting real-world sensitive information.

## Project Requirements Covered

- Encrypt user-provided text using Caesar Cipher logic
- Decrypt ciphertext using the same shift key
- Display encrypted and decrypted output
- Accept a custom shift key
- Preserve uppercase and lowercase letters
- Preserve spaces, digits, and punctuation
- Demonstrate alphabet wrap-around using modulo arithmetic
- Verify that decryption restores the original message

## Extra Features

- Professional coloured terminal interface
- Input validation and crash protection
- Message statistics
- Encrypt-and-verify mode
- Brute-force demonstration using all 25 possible keys
- Session history
- Save results to `results.txt`
- Unit tests

## Project Structure

```text
DecodeLabs_CyberSecurity_Project_2/
├── main.py
├── test_caesar_cipher.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

## How the Caesar Cipher Works

Each letter is moved by a fixed number of positions in the alphabet.

Example with a shift key of `3`:

```text
A → D
B → E
C → F
...
X → A
Y → B
Z → C
```

Example:

```text
Plaintext : HELLO
Shift key : 3
Ciphertext: KHOOR
```

Encryption formula:

```text
encrypted_position = (original_position + shift) % 26
```

Decryption formula:

```text
original_position = (encrypted_position - shift) % 26
```

The modulo operator `% 26` wraps positions back to the beginning of the 26-letter English alphabet.

## Requirements

- Python 3.10 or newer recommended
- No external Python packages are required

## Run the Program

Open a terminal inside the project folder:

```bash
python main.py
```

On some systems:

```bash
python3 main.py
```

## Program Menu

```text
1. Encrypt a message
2. Decrypt a message
3. Encrypt and verify
4. Brute-force a ciphertext
5. View session history
6. Exit
```

## Example

Input:

```text
Message   : Hello Ahmed!
Shift key : 3
```

Output:

```text
Encrypted message : Khoor Dkphg!
Decrypted message : Hello Ahmed!
Verification      : Successful
```

## Run the Tests

```bash
python -m unittest -v
```

Expected result:

```text
Ran 11 tests
OK
```

## GitHub Upload Commands

Create a new empty GitHub repository, then run:

```bash
git init
git add .
git commit -m "Complete DecodeLabs Cyber Security Project 2"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the repository URL with your actual GitHub repository URL.

## Learning Outcomes

This project demonstrates:

- Plaintext and ciphertext
- Encryption and decryption
- Symmetric-key concepts
- Character processing with `ord()` and `chr()`
- Modulo arithmetic
- Input validation
- Functions and type hints
- File handling
- Unit testing
- Basic cryptanalysis through brute force

## Security Limitation

The Caesar Cipher has only 25 meaningful keys, so an attacker can test every possible shift quickly. Modern applications should use established cryptographic libraries and strong algorithms such as AES rather than designing custom encryption.

## Author

**Ahmed Rasheed**  
DecodeLabs Cyber Security Internship — Batch 2026
