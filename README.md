# 🔐 Cipher Suite

Cipher Suite is a modern desktop application developed in **Python** using **CustomTkinter** that allows users to encrypt and decrypt text or files through an intuitive graphical interface. It combines multiple classical encryption algorithms with a clean, user-friendly design, making it an excellent educational project for learning cryptography and desktop application development.

---

## ✨ Features

* 🔒 Encrypt and decrypt text instantly
* 📁 Open and encrypt text files
* 💾 Save encrypted or decrypted output
* 🔑 Supports multiple encryption algorithms
* 🌙 Light and Dark theme support
* 📜 Scrollable encryption history panel
* 🕒 Timestamped activity log
* 🎨 Modern and responsive CustomTkinter interface
* ⚡ Fast and lightweight desktop application

---

## 🔑 Supported Algorithms

### Caesar Cipher

A substitution cipher that shifts each alphabetic character by a user-defined number of positions.

### Vigenère Cipher

A polyalphabetic cipher that uses a keyword to encrypt and decrypt text, offering greater security than the Caesar Cipher.

### XOR Cipher

A simple symmetric encryption algorithm that uses a key and bitwise XOR operations for encryption and decryption.

---

## 📂 File Operations

Cipher Suite supports file encryption by allowing users to:

* Open text files (`.txt`)
* Encrypt or decrypt file contents
* Save the processed output as a new text file

---

## 📜 Encryption History

The built-in History panel records each operation, including:

* 🔤 Manual text operations
* 🔒 Encryption / 🔓 Decryption status
* 🔑 Selected algorithm
* 🕒 Timestamp of the operation

---

## 🛠️ Technologies Used

* Python 3
* CustomTkinter
* Tkinter
* Object-Oriented Programming (OOP)

---

## 📁 Project Structure

CipherSuite/
│
├── main.py
│
├── UI/
│   ├── app.py
│   └── theme.py
│
├── algorithms/
│   ├── ceaserCipher.py
│   ├── vignere.py
│   └── xor.py
│
├── utils/
│   └── file_handler.py
│
├── screenshots/
│   ├── dark.png
│   ├── light.png
│
├── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/CipherSuite.git
cd CipherSuite
```

### Install dependencies

```bash
pip install customtkinter
```

### Run the application

```bash
python main.py
```

---

## 📖 Usage

1. Launch the application.
2. Enter text manually or open a text file.
3. Choose an encryption algorithm.
4. Enter the required key or shift value.
5. Click **Encrypt** or **Decrypt**.
6. View the processed output.
7. Save the result to a file if desired.
8. Review previous operations in the History panel.

---

## 🎯 Future Enhancements

* AES Encryption
* DES & Triple DES
* RSA Encryption
* Fernet Encryption
* Password Generator
* Password Strength Analyzer
* Copy Output button
* Drag & Drop file support
* Export encryption history
* Persistent history between sessions
* Support for additional file formats

---

## 📸 Screenshots

![alt text](dark.png) ![alt text](light.png)

---

## 🤝 Contributing

Contributions, suggestions, and feature requests are welcome. Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is released under the MIT License. You are free to use, modify, and distribute it for educational and personal purposes.

---

## 👨‍💻 Author

**Humair Ali**

A cybersecurity and software engineering student passionate about cryptography, ethical hacking, and Python application development.

If you found this project useful, consider giving the repository a ⭐ to support its development!
