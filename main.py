import sqlite3
import random

def connect_db():
    return sqlite3.connect("bank.db")

def accounts_table_create():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_number INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            pin INTEGER NOT NULL,
            balance REAL DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


def transaction_history_table_create():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_number INTEGER NOT NULL,
            transaction_type TEXT NOT NULL,
            amount REAL NOT NULL,
            balance_after REAL NOT NULL,
            transaction_date TEXT NOT NULL,
            FOREIGN KEY (account_number)
            REFERENCES accounts(account_number)
        )
    """)

    conn.commit()
    conn.close()

def create_account():

    print("\n" + "=" * 40)
    print("          CREATE ACCOUNT")
    print("=" * 40)

    account_name = input("Enter Account Holder Name :- ").strip()

    if not account_name:
        print("\nName cannot be empty!")
        return

    try:
        account_pin = int(input("Enter Your Pin :- "))
    except ValueError:
        print("\nPIN must contain numbers only!")
        return

    if account_pin < 1000 or account_pin > 9999:
        print("\nPIN must be exactly 4 digits!")
        return

    conn = connect_db()
    cursor = conn.cursor()

    while True:
        account_number = random.randint(1000000000, 9999999999)

        cursor.execute(
            """
            SELECT account_number
            FROM accounts
            WHERE account_number = ?
            """,
            (account_number,)
        )

        if cursor.fetchone() is None:
            break

    try:

        cursor.execute(
            """
            INSERT INTO accounts
            (account_number, name, pin, balance)
            VALUES (?, ?, ?, ?)
            """,
            (account_number, account_name, account_pin, 0)
        )

        conn.commit()

    except sqlite3.Error as error:

        conn.rollback()
        print("\nAccount creation failed!")
        print("Database Error:", error)
        conn.close()
        return

    conn.close()

    print("\nAccount Created Successfully!")
    print(f"Your Account Number: {account_number}")
    print("Initial Balance: ₹0")

def login():

    print("\n" + "=" * 40)
    print("              LOGIN")
    print("=" * 40)

    try:
        account_number = int(
            input("Enter your Account Number :- ")
        )
    except ValueError:
        print("\nAccount Number must contain numbers only!")
        return

    if account_number < 1000000000 or account_number > 9999999999:
        print("\nInvalid Account Number!")
        return

    try:
        account_pin = int(
            input("Enter Your Pin :- ")
        )
    except ValueError:
        print("\nPIN must contain numbers only!")
        return

    if account_pin < 1000 or account_pin > 9999:
        print("\nPIN must be exactly 4 digits!")
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT account_number, name, balance
        FROM accounts
        WHERE account_number = ?
        AND pin = ?
        """,
        (account_number, account_pin)
    )

    account = cursor.fetchone()

    if account:

        print("\nLogin Successful!")
        print(f"Welcome, {account[1]}!")

        conn.close()

        dashboard(account[0])

    else:

        print("\nInvalid Account Number or PIN!")
        conn.close()

def dashboard(account_number):

    while True:

        print("\n" + "=" * 40)
        print("          ACCOUNT DASHBOARD")
        print("=" * 40)

        ch = input("""
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Transfer Money
6. Logout
Enter Your Choice :- """)

        if ch == "1":

            check_balance(account_number)

        elif ch == "2":

            deposit_money(account_number)

        elif ch == "3":

            withdraw_money(account_number)

        elif ch == "4":

            transaction_history(account_number)

        elif ch == "5":

            transfer_money(account_number)

        elif ch == "6":

            print("\nLogged out successfully!")
            break

        else:

            print("\nInvalid Choice!")

def check_balance(account_number):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name, balance
        FROM accounts
        WHERE account_number = ?
        """,
        (account_number,)
    )

    account = cursor.fetchone()

    conn.close()

    if account:

        print("\n" + "-" * 40)
        print(f"Account Holder: {account[0]}")
        print(f"Current Balance: ₹{account[1]:.2f}")
        print("-" * 40)

    else:

        print("\nAccount not found!")

def deposit_money(account_number):

    print("\n" + "=" * 40)
    print("          DEPOSIT MONEY")
    print("=" * 40)

    try:

        amount = float(
            input("Enter amount you want to deposit :- ")
        )

    except ValueError:

        print("\nAmount must be a number!")
        return

    if amount <= 0:

        print("\nAmount must be greater than 0!")
        return

    conn = connect_db()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            UPDATE accounts
            SET balance = balance + ?
            WHERE account_number = ?
            """,
            (amount, account_number)
        )

        cursor.execute(
            """
            SELECT balance
            FROM accounts
            WHERE account_number = ?
            """,
            (account_number,)
        )

        balance = cursor.fetchone()[0]

        cursor.execute(
            """
            INSERT INTO transactions
            (
                account_number,
                transaction_type,
                amount,
                balance_after,
                transaction_date
            )
            VALUES (
                ?, ?, ?, ?,
                datetime('now', 'localtime')
            )
            """,
            (
                account_number,
                "Deposit",
                amount,
                balance
            )
        )

        conn.commit()

    except sqlite3.Error as error:

        conn.rollback()
        conn.close()

        print("\nDeposit failed!")
        print("Database Error:", error)
        return

    conn.close()

    print(f"\n₹{amount:.2f} deposited successfully!")
    print(f"Current Balance: ₹{balance:.2f}")

def withdraw_money(account_number):

    print("\n" + "=" * 40)
    print("          WITHDRAW MONEY")
    print("=" * 40)

    try:

        amount = float(
            input("Enter amount you want to withdraw :- ")
        )

    except ValueError:

        print("\nAmount must be a number!")
        return

    if amount <= 0:

        print("\nAmount must be greater than 0!")
        return

    conn = connect_db()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            SELECT balance
            FROM accounts
            WHERE account_number = ?
            """,
            (account_number,)
        )

        account = cursor.fetchone()

        if not account:

            print("\nAccount not found!")
            conn.close()
            return

        balance = account[0]

        if amount > balance:

            print("\nInsufficient Balance!")
            print(
                f"Your Current Balance: ₹{balance:.2f}"
            )

            conn.close()
            return

        cursor.execute(
            """
            UPDATE accounts
            SET balance = balance - ?
            WHERE account_number = ?
            """,
            (amount, account_number)
        )

        cursor.execute(
            """
            SELECT balance
            FROM accounts
            WHERE account_number = ?
            """,
            (account_number,)
        )

        balance_after = cursor.fetchone()[0]

        cursor.execute(
            """
            INSERT INTO transactions
            (
                account_number,
                transaction_type,
                amount,
                balance_after,
                transaction_date
            )
            VALUES (
                ?, ?, ?, ?,
                datetime('now', 'localtime')
            )
            """,
            (
                account_number,
                "Withdraw",
                amount,
                balance_after
            )
        )

        conn.commit()

    except sqlite3.Error as error:

        conn.rollback()
        conn.close()

        print("\nWithdrawal failed!")
        print("Database Error:", error)
        return

    conn.close()

    print(f"\n₹{amount:.2f} withdrawn successfully!")
    print(f"Remaining Balance: ₹{balance_after:.2f}")

def transaction_history(account_number):

    print("\n" + "=" * 70)
    print("                    TRANSACTION HISTORY")
    print("=" * 70)

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            transaction_id,
            transaction_type,
            amount,
            balance_after,
            transaction_date
        FROM transactions
        WHERE account_number = ?
        ORDER BY transaction_id DESC
        """,
        (account_number,)
    )

    transactions = cursor.fetchall()

    conn.close()

    if not transactions:

        print("\nNo transactions found!")
        return

    print(
        f"\n{'ID':<5} "
        f"{'TYPE':<20} "
        f"{'AMOUNT':<15} "
        f"{'BALANCE':<15} "
        f"{'DATE'}"
    )

    print("-" * 90)

    for transaction in transactions:

        print(
            f"{transaction[0]:<5} "
            f"{transaction[1]:<20} "
            f"₹{transaction[2]:<14.2f} "
            f"₹{transaction[3]:<14.2f} "
            f"{transaction[4]}"
        )

def transfer_money(account_number):

    print("\n" + "=" * 40)
    print("          TRANSFER MONEY")
    print("=" * 40)

    try:

        receiver_account = int(
            input("Enter Receiver Account Number :- ")
        )

    except ValueError:

        print("\nAccount Number must contain numbers only!")
        return

    if (
        receiver_account < 1000000000
        or receiver_account > 9999999999
    ):

        print("\nInvalid Receiver Account Number!")
        return

    try:

        amount = float(
            input("Enter amount you want to Transfer :- ")
        )

    except ValueError:

        print("\nAmount must be a number!")
        return

    if amount <= 0:

        print("\nAmount must be greater than 0!")
        return

    if receiver_account == account_number:

        print(
            "\nYou can't transfer money to your own account!"
        )
        return

    conn = connect_db()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            SELECT balance
            FROM accounts
            WHERE account_number = ?
            """,
            (account_number,)
        )

        sender = cursor.fetchone()

        if not sender:

            print("\nSender account not found!")
            conn.close()
            return

        sender_balance = sender[0]

        cursor.execute(
            """
            SELECT name
            FROM accounts
            WHERE account_number = ?
            """,
            (receiver_account,)
        )

        receiver = cursor.fetchone()

        if not receiver:

            print("\nReceiver account not found!")
            conn.close()
            return

        if amount > sender_balance:

            print("\nInsufficient Balance!")
            print(
                f"Your Current Balance: ₹{sender_balance:.2f}"
            )

            conn.close()
            return

        cursor.execute(
            """
            UPDATE accounts
            SET balance = balance - ?
            WHERE account_number = ?
            """,
            (amount, account_number)
        )

        cursor.execute(
            """
            UPDATE accounts
            SET balance = balance + ?
            WHERE account_number = ?
            """,
            (amount, receiver_account)
        )

        cursor.execute(
            """
            SELECT balance
            FROM accounts
            WHERE account_number = ?
            """,
            (account_number,)
        )

        sender_balance_after = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT balance
            FROM accounts
            WHERE account_number = ?
            """,
            (receiver_account,)
        )

        receiver_balance_after = cursor.fetchone()[0]

        cursor.execute(
            """
            INSERT INTO transactions
            (
                account_number,
                transaction_type,
                amount,
                balance_after,
                transaction_date
            )
            VALUES (
                ?, ?, ?, ?,
                datetime('now', 'localtime')
            )
            """,
            (
                account_number,
                "Transfer Sent",
                amount,
                sender_balance_after
            )
        )

        cursor.execute(
            """
            INSERT INTO transactions
            (
                account_number,
                transaction_type,
                amount,
                balance_after,
                transaction_date
            )
            VALUES (
                ?, ?, ?, ?,
                datetime('now', 'localtime')
            )
            """,
            (
                receiver_account,
                "Transfer Received",
                amount,
                receiver_balance_after
            )
        )

        conn.commit()

    except sqlite3.Error as error:

        conn.rollback()
        conn.close()

        print("\nTransfer failed!")
        print("Database Error:", error)
        return

    conn.close()

    print("\nTransfer Successful!")
    print(f"Transferred Amount: ₹{amount:.2f}")
    print(f"Receiver: {receiver[0]}")
    print(
        f"Remaining Balance: ₹{sender_balance_after:.2f}"
    )

accounts_table_create()
transaction_history_table_create()

while True:

    print("\n" + "=" * 40)
    print("       WELCOME TO MY BANK")
    print("=" * 40)

    try:

        ch = int(input("""
1. Login
2. Create Account
3. Exit
Enter Your Choice :- """))

    except ValueError:

        print("\nPlease enter a number!")
        continue

    if ch == 1:

        login()

    elif ch == 2:

        create_account()

    elif ch == 3:

        print("\nThank you for using My Bank!")
        break

    else:

        print("\nInvalid Choice!")
