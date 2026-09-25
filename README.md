# 🏦 My Bank — CLI Banking System

A **Python-based Command-Line Banking System** that uses **SQLite** for persistent data storage. The application allows users to create accounts, securely log in using a 4-digit PIN, manage their balance, transfer money, and view transaction history.

## ✨ Features

* 👤 Create a new bank account
* 🔐 PIN-based account login
* 💰 Check current account balance
* ➕ Deposit money
* ➖ Withdraw money
* 🔄 Transfer money between accounts
* 📜 View transaction history
* 🗄️ SQLite database for persistent storage
* ✅ Input validation and error handling
* 💾 Automatic transaction recording
* 🚪 Secure logout option

## 🛠️ Technologies Used

* **Python**
* **SQLite3**
* **Random module**
* **CLI (Command-Line Interface)**

## 📂 Project Structure

```text
Banking-System/
│
├── main.py
├── bank.db
└── README.md
```

> `bank.db` is created automatically when the program runs if it does not already exist.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yatharth-kaushik/Banking-System-CLI-App
```

### 2. Navigate to the project directory

```bash
cd Banking-System-CLI-App
```

### 3. Run the application

```bash
python main.py
```

## 🏦 How It Works

When the application starts, the user gets three options:

```text
1. Login
2. Create Account
3. Exit
```

### Create Account

The user provides:

* Account holder name
* 4-digit PIN

A unique 10-digit account number is automatically generated, and the initial balance is set to ₹0.

### Login

Users log in using their:

* Account Number
* 4-digit PIN

The credentials are checked against the SQLite database before access to the account dashboard is granted.

## 📊 Account Dashboard

After successful login, users can access:

```text
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Transfer Money
6. Logout
```

## 💳 Banking Operations

### Check Balance

Displays the account holder's name and current account balance.

### Deposit Money

Users can deposit a positive amount into their account. The updated balance and transaction are stored in the database.

### Withdraw Money

Users can withdraw money if sufficient balance is available. The system prevents withdrawals greater than the current balance.

### Transfer Money

Users can transfer money to another existing account. The system checks that:

* The receiver account exists
* The receiver is not the sender
* The sender has sufficient balance
* The transfer amount is greater than zero

Both the sender and receiver receive corresponding transaction records.

### Transaction History

The application stores and displays:

* Transaction ID
* Transaction type
* Amount
* Balance after transaction
* Transaction date and time

## 🗄️ Database

The application uses SQLite with two tables:

### `accounts`

Stores:

* Account number
* Account holder name
* PIN
* Account balance

### `transactions`

Stores:

* Transaction ID
* Account number
* Transaction type
* Transaction amount
* Balance after transaction
* Transaction date

## 🔒 Validation & Error Handling

The application includes validation for:

* Empty account holder names
* Invalid PIN formats
* Invalid account numbers
* Invalid transaction amounts
* Insufficient account balance
* Non-existent receiver accounts
* Transfers to the user's own account
* Invalid menu choices
* SQLite database errors

Database operations use commit/rollback handling for transaction failures.

## 📌 Future Improvements

Possible improvements for future versions:

* Password/PIN hashing instead of storing the PIN directly
* Admin dashboard
* Account deletion
* Account profile updates
* Transaction search and filtering
* Interest calculation
* Improved UI using a Python CLI framework
* Unit testing
* More detailed security features

## 👨‍💻 Author

**Yatharth Kaushik**

## 📄 License

This project is intended for educational and learning purposes.
