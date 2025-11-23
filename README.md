# Unofficial MBBank API (V3)

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/mstrvndev/mbbankapiunofficial)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/Version-V3.0.0-orange)](https://github.com/mstrvndev/mbbankapiunofficial)
[![Telegram](https://img.shields.io/badge/Support-Telegram-blue?logo=telegram)](https://t.me/imlehongphuc)

> **⚠️ Important:** This is an **Unofficial** API wrapper for MBBank. It is **not** endorsed by or affiliated with MBBank. Use responsibly and at your own risk.

## 🚀 Introduction

Welcome to the **V3** release of the Unofficial MBBank API. This version is the **official stable release** for this repository, engineered for speed and continuous updates.

Unlike previous versions, **V3** is actively maintained to ensure compatibility with the latest MBBank app backend changes.

**Key Features:**
* ✅ **Always Updated:** Patched immediately when MBBank updates their backend.
* ✅ **Secure Login:** Handle Captcha and Password authentication securely.
* ✅ **Full Features:** Check balances, get transaction history, and perform transfers (internal/NAPAS).
* ✅ **Maintained:** Direct support via Telegram for bugs.

---

## 🛠️ Installation

To ensure the API functions correctly, you must install all required libraries and use the correct V3 folder.

### 1. Clone the Repository
```bash
git clone [https://github.com/mstrvndev/mbbankapiunofficial.git](https://github.com/mstrvndev/mbbankapiunofficial.git)
cd mbbankapiunofficial
```
2. Install Dependencies
Install the required Python libraries (requests, security modules, etc.):

```bash
pip install -r requirements.txt
```
(If I don't have the requirements file yet, install manually: 
```bash
pip install requests pillow pycryptodome
```
)

💻 Usage
Note: Please use the officialmbbankapiV3 folder for all imports to ensure you are using the maintained version.

```bash
from officialmbbankapiV3 import MBBank

# Initialize the API
# ⚠️ SECURITY WARNING: Never hardcode your password in public scripts.
mb = MBBank(username="YOUR_USERNAME", password="YOUR_PASSWORD")

# Login
if mb.login():
    print("Login Successful!")
    
    # Get Balance
    balance = mb.get_balance()
    print(f"Current Balance: {balance['amount']}")

    # Get Transaction History (Last 30 days)
    history = mb.get_transaction_history(days=30)
    print(history)

else:
    print("Login Failed. Please check your credentials or captcha.")
```
🤝 Support & Maintenance
This repository is actively maintained. If you encounter errors, login issues, or need an update due to bank changes, please contact me directly.

Direct Message (Telegram): https://t.me/imlehongphuc

Issues: Please verify you are using the V3 version before reporting.

⚖️ Disclaimer
This software is provided "as is", without warranty of any kind. The authors are not responsible for any financial loss, account locks, or legal issues arising from the use of this tool.

Do not share your banking credentials with anyone.

Do not use this tool for spamming or malicious activities.


