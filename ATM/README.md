# 🏧 ATM System

This is a simple command-line **ATM System** built in Python using Object-Oriented Programming (OOP). It simulates basic ATM operations — setting a PIN, checking balance, depositing, and withdrawing money — with support for multiple independent ATM/account instances.

---

## 🏷️ Project Info

| Label | Detail |
|---|---|
| **Language** | Python 3.x |
| **Type** | Command-Line Interface (CLI) Application |
| **Paradigm** | Object-Oriented Programming |
| **Storage** | In-memory only (no file/database persistence) |
| **Dependencies** | None (standard library only) |
| **Author** | Dev Gothi |

---

## 📁 Folder Structure

```
ATM System/
├── ATM.py       # Atm class — all logic in one file
└── README.md    # Project documentation
```

---

## ✨ Features

- 🔐 **Set Pin** — Create a PIN for the account
- 💰 **Check Balance** — View current balance (PIN protected)
- ⬆️ **Deposit** — Add money to the account (PIN protected)
- ⬇️ **Withdraw** — Withdraw money, blocked if funds are insufficient (PIN protected)
- 🏦 **Multiple Accounts** — Each `Atm` object maintains its own independent PIN and balance

---

## 🧩 Class Overview

### `Atm`

| Attribute | Description |
|---|---|
| `pin` | Stores the account's PIN (empty string until set) |
| `balance` | Stores the current account balance (starts at `0`) |

| Method | Description |
|---|---|
| `menu()` | Runs the menu-driven CLI loop |
| `SetPin()` | Prompts for and stores a new PIN |
| `CheckBalance()` | Verifies PIN, then prints the current balance |
| `Deposit()` | Verifies PIN, then adds the entered amount to the balance |
| `Withdraw()` | Verifies PIN, then subtracts the entered amount if sufficient balance exists |

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.x installed
- No external libraries required

### ▶️ Run the Program
```bash
python atm.py
```

### 📋 Menu Options
```
1. SetPin
2. CheckBalance
3. Deposit
4. Withdraw
5. Exit
```

---

## ⚙️ How It Works

| Action | Behavior |
|---|---|
| **Set Pin** | Overwrites `self.pin` with the entered value — no confirmation or validation |
| **Check Balance** | Compares entered PIN to `self.pin`; prints balance only if they match |
| **Deposit** | Verifies PIN, then adds the entered amount to `self.balance` |
| **Withdraw** | Verifies PIN, then checks `self.balance >= amount` before subtracting; prints an error otherwise |
| **Multiple Instances** | Creating separate `Atm()` objects (e.g. `sbi`, `hdfc`) gives each its own isolated PIN and balance |

---

## 🛠️ Possible Improvements

- [ ] Persist account data to a file (e.g. JSON) so balances survive restarts
- [ ] Prevent PIN from being set to an empty value
- [ ] Add PIN confirmation step (enter twice) when setting a new PIN
- [ ] Validate deposit/withdraw amounts are positive numbers
- [ ] Limit incorrect PIN attempts (lock account after N failures)
- [ ] Add a transaction history log
- [ ] Support multiple accounts identified by account number instead of separate objects

---

## 👤 Author

**Dev Gothi**
B.Tech Electronics and VLSI Engineering, SVNIT Surat
