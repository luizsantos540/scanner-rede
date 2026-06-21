# Network Port Scanner / Scanner de Portas de Rede

<p align="center">
  <a href="#en-us-english">English</a> | 
  <a href="#pt-br-português">Português</a>
</p>

---

## EN-US (English)

A lightweight and robust Command Line Interface (CLI) network port scanner built with Python. This tool allows users to verify which ports (from 1 to 100) are open on a specific IP address or domain, automatically saving the successful connections into a local report file.

This is the second project in my personal portfolio, aimed at mastering core programming concepts, networking fundamentals, and secure coding practices.

### 🚀 Features

- **Automated Scanning:** Scans multiple ports consecutively using loops.
- **Data Persistence:** Automatically writes all discovered open ports into a `resultado.txt` file.
- **Error Handling:** Robust exception management to handle invalid IP addresses, missing domains, or sudden network disconnections without crashing.
- **Clean Architecture:** Modular code structured into specialized functions for better readability and maintenance.

### 🛠️ Technologies Used

- **Python 3**
- **Socket Library** (Native networking module)
- **Git & GitHub** (Version control and repository management)

### 📖 What I Learned From This Project

- **Network Sockets:** Understanding how TCP/IP connections work, managing timeouts, and handling system resources properly by closing sockets (`conexao.close()`).
- **File I/O:** Implementing data appending (`with open("...", "a")`) to build local scan logs efficiently.
- **Defensive Programming:** Using `try/except` blocks to anticipate user errors and environment instabilities, ensuring software resilience.
- **Code Organization:** Separating visual components (banners), user input logic, and network logic into distinct functions.

### 🔧 How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/luizsantos540/scanner-rede.git](https://github.com/luizsantos540/scanner-rede.git)

 2. Navigate to the project directory:
   cd scanner-rede

 3. Run the Script:
  ´´´bash
  python main.py      