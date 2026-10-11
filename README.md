<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:141e30,100:243b55&height=230&section=header&text=%F0%9F%8F%A6%20My%20Bank&fontSize=60&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=A%20Python%20%2B%20SQLite%20Command-Line%20Banking%20System&descAlignY=58&descSize=18" width="100%" />

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=F7C948&center=true&vCenter=true&width=700&lines=Create+accounts+%26+log+in+with+a+PIN+%F0%9F%94%90;Deposit%2C+withdraw+%26+transfer+money+%F0%9F%92%B8;Every+transaction+recorded+in+SQLite+%F0%9F%97%84%EF%B8%8F;Built+entirely+in+the+terminal+%F0%9F%90%8D" alt="Typing SVG" />
</a>

<br/>

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
<img src="https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge&logo=gnubash&logoColor=white" alt="CLI" />
<img src="https://img.shields.io/badge/Purpose-Educational-blueviolet?style=for-the-badge" alt="Educational" />

<img src="https://img.shields.io/github/stars/yatharth-kaushik/Banking-System-CLI-App?style=flat-square&logo=github&color=yellow" alt="stars" />
<img src="https://img.shields.io/github/forks/yatharth-kaushik/Banking-System-CLI-App?style=flat-square&logo=github" alt="forks" />
<img src="https://img.shields.io/github/last-commit/yatharth-kaushik/Banking-System-CLI-App?style=flat-square&color=blue" alt="last commit" />
<img src="https://img.shields.io/github/repo-size/yatharth-kaushik/Banking-System-CLI-App?style=flat-square&color=orange" alt="repo size" />

</div>

---

## 📖 Overview

**My Bank** is a Python command-line banking system backed by **SQLite** for persistent storage. Create an account, log in with a 4-digit PIN, manage your balance, transfer money to other accounts, and review your full transaction history, all from the terminal.

---

## ✨ Features

| | Feature | Description |
|---|---|---|
| 👤 | **Create Account** | Open a new account with an auto-generated 10-digit account number |
| 🔐 | **PIN Login** | Log in with your account number and 4-digit PIN |
| 💰 | **Check Balance** | View your name and current balance |
| ➕ | **Deposit** | Add money to your account |
| ➖ | **Withdraw** | Withdraw funds (blocked if balance is insufficient) |
| 🔄 | **Transfer** | Send money to another existing account |
| 📜 | **Transaction History** | See every transaction with type, amount and balance |
| 🗄️ | **SQLite Storage** | All data persists between runs |
| ✅ | **Validation** | Input checks and error handling throughout |
| 🚪 | **Logout** | End your session from the dashboard |

---

## 🛠️ Built With

<div align="center">

<img src="https://skillicons.dev/icons?i=python,sqlite,git,github,vscode&perline=5" alt="tech" />

</div>

`Python` • `SQLite3` • `random` • `CLI`

---

## 🚀 Getting Started

**1️⃣ Clone the repository**

```bash
git clone https://github.com/yatharth-kaushik/Banking-System-CLI-App.git
```

**2️⃣ Move into the project folder**

```bash
cd Banking-System-CLI-App
```

**3️⃣ Run the app**

```bash
python main.py
```

> 💡 `bank.db` is created automatically the first time you run the program.

---

## 🏦 How It Works

### Start Menu

```text
1. Login
2. Create Account
3. Exit
```

### 👤 Create Account

Provide your **name** and a **4-digit PIN**. A unique **10-digit account number** is generated for you, and your starting balance is **₹0**.

### 🔐 Login

Enter your **account number** and **PIN**. They are checked against the database before you can access the dashboard.

### 📊 Account Dashboard

```text
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Transfer Money
6. Logout
```

---

## 💳 Banking Operations

<details open>
<summary><b>💰 Check Balance</b></summary>

Displays the account holder's name and the current balance.

</details>

<details>
<summary><b>➕ Deposit Money</b></summary>

Deposit any positive amount. The new balance and the transaction are saved to the database.

</details>

<details>
<summary><b>➖ Withdraw Money</b></summary>

Withdraw money as long as you have enough balance. Withdrawals above your current balance are rejected.

</details>

<details>
<summary><b>🔄 Transfer Money</b></summary>

Before a transfer goes through, the app checks that:

- ✅ The receiver account exists
- ✅ The receiver is not the sender
- ✅ The sender has sufficient balance
- ✅ The amount is greater than zero

Both the sender and the receiver get a matching transaction record.

</details>

<details>
<summary><b>📜 Transaction History</b></summary>

Each record shows:

- Transaction ID
- Transaction type
- Amount
- Balance after the transaction
- Date and time

</details>

---

## 🗄️ Database Design

<table>
<tr>
<td valign="top">

**`accounts`**

- Account number
- Account holder name
- PIN
- Balance

</td>
<td valign="top">

**`transactions`**

- Transaction ID
- Account number
- Transaction type
- Amount
- Balance after transaction
- Transaction date

</td>
</tr>
</table>

---

## 🔒 Validation & Error Handling

The app handles:

- ❌ Empty account holder names
- ❌ Invalid PIN formats
- ❌ Invalid account numbers
- ❌ Invalid transaction amounts
- ❌ Insufficient balance
- ❌ Non-existent receiver accounts
- ❌ Transfers to your own account
- ❌ Invalid menu choices
- ❌ SQLite database errors

Database operations use **commit / rollback** handling so a failed transaction doesn't leave your data in a half-updated state.

---

## 📂 Project Structure

```text
Banking-System/
│
├── main.py      # Application code
├── bank.db      # Auto-generated SQLite database
└── README.md    # Project documentation
```

---

## 🔮 Roadmap

- [ ] PIN hashing instead of storing the PIN directly
- [ ] Admin dashboard
- [ ] Account deletion
- [ ] Account profile updates
- [ ] Transaction search and filtering
- [ ] Interest calculation
- [ ] Improved UI with a Python CLI framework
- [ ] Unit tests
- [ ] More detailed security features

---

## 📄 License

This project is intended for educational and learning purposes.

---

## 👨‍💻 Author

<div align="center">

**Yatharth Kaushik**

<a href="https://github.com/yatharth-kaushik"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
<a href="https://www.linkedin.com/in/yatharth-kaushik-92920a421/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>

<br/><br/>

⭐ **If you find this project useful, consider giving it a star!** ⭐

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:243b55,100:141e30&height=120&section=footer" width="100%" />

</div>
