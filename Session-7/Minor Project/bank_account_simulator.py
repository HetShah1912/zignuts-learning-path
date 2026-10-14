# Create an OOP-based program to simulate bank account
# operations (deposit, withdrawal, check balance) with error handling for invalid
# operations. Make sure to use CRUD operations with MySQL to persist data, instead of just
# runtime.

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
class BankAccount:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "127.0.0.1",
            port = 3306,
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database="bank_db"
        )
        self.cursor = self.conn.cursor()

    def create_account(self):
        name = input("Enter account holder name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        try:
            balance = float(input("Enter initial deposit: "))

            if balance < 0:
                print("Balance cannot be negative.")
                return

            query = "INSERT INTO accounts (account_holder, balance) VALUES (%s, %s)"
            self.cursor.execute(query, (name, balance))
            self.conn.commit()

            print("Account created successfully!")
            print("Account ID:", self.cursor.lastrowid)

        except ValueError:
            print("Please enter a valid amount.")

    def check_balance(self):
        try:
            account_id = int(input("Enter account ID: "))
            query = "SELECT account_holder, balance FROM accounts WHERE account_id = %s"
            self.cursor.execute(query, (account_id))
            account = self.cursor.fetchone()

            if account:
                print("Account Holder:", account[0])
                print("Current Balance:", account[1])
            else:
                print("Account not found.")

        except ValueError:
            print("Account ID must be a number.")

    def deposit(self):
        try:
            account_id = int(input("Enter account ID: "))
            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                print("Deposit amount must be greater than zero.")
                return

            query = "UPDATE accounts SET balance = balance + %s WHERE account_id = %s"
            self.cursor.execute(query, (amount, account_id))
            self.conn.commit()

            if self.cursor.rowcount > 0:
                print("Amount deposited successfully!")
            else:
                print("Account not found.")

        except ValueError:
            print("Please enter valid numbers.")

    def withdraw(self):
        try:
            account_id = int(input("Enter account ID: "))
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Withdrawal amount must be greater than zero.")
                return

            query = "SELECT balance FROM accounts WHERE account_id = %s"
            self.cursor.execute(query, (account_id,))
            account = self.cursor.fetchone()

            if account is None:
                print("Account not found.")
            elif amount > account[0]:
                print("Insufficient balance.")
            else:
                query = "UPDATE accounts SET balance = balance - %s WHERE account_id = %s"
                self.cursor.execute(query, (amount, account_id))
                self.conn.commit()
                print("Amount withdrawn successfully!")

        except ValueError:
            print("Please enter valid numbers.")

    def show_accounts(self):
        self.cursor.execute("SELECT * FROM accounts")
        accounts = self.cursor.fetchall()

        if not accounts:
            print("No accounts found.")
            return

        for account in accounts:
            print(account)

    def delete_account(self):
        try:
            account_id = int(input("Enter account ID to delete: "))

            query = "DELETE FROM accounts WHERE account_id = %s"
            self.cursor.execute(query, (account_id,))
            self.conn.commit()

            if self.cursor.rowcount > 0:
                print("Account deleted successfully.")
            else:
                print("Account not found.")

        except ValueError:
            print("Account ID must be a number.")

    def close(self):
        self.cursor.close()
        self.conn.close()


try:
    bank = BankAccount()

    while True:
        print("\n--- BANK ACCOUNT MENU ---")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. View All Accounts")
        print("6. Delete Account")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.check_balance()
        elif choice == "3":
            bank.deposit()
        elif choice == "4":
            bank.withdraw()
        elif choice == "5":
            bank.show_accounts()
        elif choice == "6":
            bank.delete_account()
        elif choice == "7":
            print("Thank you for using our bank!")
            break
        else:
            print("Invalid choice. Please try again.")

    bank.close()

except mysql.connector.Error as error:
    print("Database error:", error)
